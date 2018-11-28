#include <bits/stdc++.h>

#define Max      40000
#define Max2     100010
#define mod      1000000007
#define Maxp     78499
#define pf       printf
#define sf       scanf
#define CLR(a)   memset(a,0,sizeof(a))
#define SET(a)   memset(a,-1,sizeof(a))
#define pb       push_back
#define fs       first
#define sc       second
#define TCASE    int T,t=1;scanf("%d",&T);while(T--)
#define loop(n)  for(int i=0;i<n;i++)
#define lop2(n)  for(int i=1;i<=n;i++)
#define lup(a)   for(int i=0;i<strlen(a);i++)
#define NL       pf("\n")
#define uplo     0b00100000
#define _        ios_base::sync_with_stdio(false); cin.tie(false);
#define check(a,b) a & (1 << b)

using namespace std;

typedef long long ll;
typedef unsigned long long llu;
typedef unsigned long lu;
const double eps = 1e-9;
const double PI  = 3.1415926535897932384626433832795;
const int    inf = 0x7f7f7f7f;

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    TCASE
    {
        int k,c,s;
        sf("%d %d %d",&k,&c,&s);
        pf("Case #%d:",t++);
        if(c==1 || k==1)
        {
            if(s>=k)  for(int i=1;i<=k;i++)  pf(" %d",i);
            else      pf(" IMPOSSIBLE");
            pf("\n");
        }
        else
        {
            if(s>=(k-1)) for(int i=2;i<=k;i++)  pf(" %d",i);
            else         pf(" IMPOSSIBLE");
            pf("\n");
        }
    }
    return 0;
}

