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

#define deb(x) cout << "> " << #x << " : " << (x) << endl;
#define EPS 0.000000001
#define Pi 3.1415926535897932384626433832795028841971
#define hash1 1000003
#define hash2 1000033
#define md 1000000007
#define INF 1000000500ll
#define mp make_pair
#define pb push_back
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < int,int >
#define REP(i,a,n) for(i=a;i<n;i++)
#define sc scanf
#define pt printf
#define big long long
#define VI vector <int>
#define DID (long long)
#define ll long long
#define AL(a) (a).begin(),(a).end()
#define INFF DID INF*INF


using namespace std;

const int T=20 + 5;

int d[T],a[T][T];
int i,j,x;

main(){
    #ifndef ONLINE_JUDGE
            freopen("text.in","r",stdin); freopen("text.out","w",stdout);
    #endif

    int t;
    cin>>t;
    int tt=t;
    while (t--){
        for (i=1;i<=16;i++)
            d[i]=0;
        cin>>x;
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++)
            cin>>a[i][j];

        for (j=1;j<=4;j++)
            d[a[x][j]]++;

        cin>>x;
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++)
            cin>>a[i][j];

        for (j=1;j<=4;j++)
            d[a[x][j]]++;

        int sul=0;
        int last;

        for (i=1;i<=16;i++)
            if (d[i]==2)
            sul++ , last = i;

        string answer;

        if (sul==1){
            cout<<"Case #"<<tt-t<<": "<<last<<endl;
        }else
        if (sul>1)
            cout<<"Case #"<<tt-t<<": "<<"Bad magician!"<<endl;
        else
            cout<<"Case #"<<tt-t<<": "<<"Volunteer cheated!"<<endl;
    }

}
