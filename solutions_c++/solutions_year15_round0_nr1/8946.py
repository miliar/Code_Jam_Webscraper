#include <bits/stdc++.h>

#define Max      2010
#define Maxp     78501
#define pf       printf
#define sf       scanf
#define CLR(a)   memset(a,0,sizeof(a))
#define SET(a)   memset(a,-1,sizeof(a))
#define pb       push_back
#define fs       first
#define sc       second
#define TCASE    int T,t=1;scanf("%d",&T);while(T--)
#define lop1(n)  for(int i=0;i<n;i++)
#define lop2(n)  for(int i=1;i<=n;i++)
#define lup(a)   for(int i=0;i<strlen(a);i++)
#define NL       pf("\n")
#define uplo     0b00100000
#define _        ios_base::sync_with_stdio(false); cin.tie(false);

using namespace std;

typedef long long ll;
typedef unsigned long long llu;
typedef unsigned long lu;
const double eps = 1e-9;
const double PI = 3.1415926535897932384626433832795;
const int inf = 0x7f7f7f7f;

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("output.txt","w",stdout);
    TCASE
    {
        ll n;
        char ar[1005];
        sf("%lld %s",&n,ar);
        ll cont = ar[0]-'0';
        ll ans = 0;
        for(ll i=1;i<strlen(ar);i++)
        {
            ll cur = 0;
            if(i > cont)  cur+=i-cont;
            cont+=ar[i]-'0'+cur;
            ans+=cur;
        }
        pf("Case #%d: %lld\n",t++,ans);
    }
    return 0;
}
