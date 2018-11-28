/*===============*\
|  ID: TMANDZU    |
|    LANG: C++    |
\*===============*/
//Tornike Mandzulashvili
//#pragma comment(linker,"/STACK:256000000")
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <stack>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iostream>
#include <set>
#include <cstring>
#include <deque>

#define deb(x) cout << "> " << #x << " : " << (x) << endl;
#define EPS 0.000000001
#define Pi 3.1415926535897932384626433832795028841971
#define hash1 1000003
#define hash2 1000033
#define md 1000000007
#define INF ((1<<30)-1)
#define mp make_pair
#define pb push_back
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < ll ,ll  >
#define REP(i,a,n) for(i=a;i<n;i++)
#define sc scanf
#define pt prll f
#define big long long
#define VI vector <ll >
#define DID (long long)
#define ll long long
#define AL(a) (a).begin(),(a).end()
#define INFF DID INF*INF


using namespace std;

const int T=100 + 5;

int N,M;
string s[T];
int d[T];
int dp[T*T*T];
int num[T][30],fix[T][30];

void renull(){
    N=M=0;
}

int main(){
    #ifndef ONLINE_JUDGE
        freopen("text.in","r",stdin); freopen("text.out","w",stdout);
    #endif

    int t;
    cin>>t;
    for (int tt=1;tt<=t;tt++){
        renull();

        cin>>M>>N;
        for (int i=0;i<M;i++)
            cin>>s[i];

        for (int mask=0;mask<(1<<M);mask++){
            for (int j=0;j<T;j++)
                for (int k=0;k<30;k++)
                fix[j][k]=0;

            dp[mask]=1;
            int raod=0;
            for (int j=0;j<M;j++)if (mask&(1<<j)){
                int pos = 0;
                for (int k=0;k<s[j].S;k++){
                    if (!fix[pos][s[j][k]-'A'])
                        dp[mask]++ , fix[pos][s[j][k]-'A']=1 , num[pos][s[j][k]-'A']=++raod;
                    pos=num[pos][s[j][k]-'A'];
                }
            }
        }

        int sul=1;
        for (int i=1;i<=M;i++)
            sul*=N;

        int mx=0;
            int raod=0;

        for (int mask=0;mask<sul;mask++){
            int h=mask;
            int l=0;
            for (int i=0;i<M;i++)
            {
                d[i]=h%N;
                h/=N;
            }
            bool ok=true;
            for (int j=0;j<N;j++){
                bool chk=0;
                for (int i=0;i<M;i++){
                    if (d[i]==j)
                    chk=1;
                }
                ok&=chk;
            }

            if (!ok)
                continue;


            int SUM=0;
            for (int i=0;i<N;i++){
                int mask=0;
                for (int j=0;j<M;j++)
                    if (d[j]==i)
                    mask|=(1<<j);

                SUM+=dp[mask];
            }

            if (SUM>mx){
                mx=SUM;
                raod=1;
            }else
            if (SUM==mx)
                raod++;

        }

        cout<<"Case #"<<tt<<": "<<mx<<" "<<raod<<endl;

    }

}
