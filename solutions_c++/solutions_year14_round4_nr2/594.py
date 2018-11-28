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

const int T=1e5 + 5;

int p[T],s[T],a[T],d[T];
int dp[2005][2005];

int get(int pos){
    int h=0;
    while (pos){
        h+=s[pos];
        pos=pos&(pos-1);
    }
    return h;
}

void upd(int pos,int delta){
    while (pos<=1005){
        s[pos]+=delta;
        pos=2*pos-(pos&(pos-1));
    }
}

int main(){
    #ifndef ONLINE_JUDGE
        freopen("text.in","r",stdin); freopen("text.out","w",stdout);
    #endif

    int t;
    cin>>t;
    for (int tt=1;tt<=t;tt++){
        int N;
        cin>>N;
        for (int i=1;i<=N;i++)
            cin>>a[i] , d[i] = a[i];

        map <int,int> M;
        sort(d+1,d+N+1);
        for (int i=1;i<=N;i++)
            M[d[i]]=i;
        for (int i=1;i<=N;i++)
            a[i]=M[a[i]];

        for (int i=1;i<=N;i++)
            p[a[i]]=i;

        for (int i=1;i<=N+5;i++)
            s[i]=1;


        int A,B,ans=0;
        for (int i=1;i<=N;i++){
            A=B=0;
            int x=p[i];
            for (int j=1;j<x;j++)
                if (s[j])
                A++;
            for (int j=N;j>x;j--)
                if (s[j])
                B++;
            ans+=min(A,B);
            s[x]=0;
        }

        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }

}
