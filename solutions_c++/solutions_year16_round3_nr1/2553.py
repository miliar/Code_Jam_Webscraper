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

struct pol
{
    int id,sz;
};

bool cmp(const pol &x,const pol &y)
{
    return x.sz > y.sz;
}

int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    TCASE
    {
       int n;
       sf("%d",&n);
       int ar[n];
       pol pol[n];
       for(int i=0;i<n;i++)  pol[i].id=i;
       int tot = 0;
       for(int i=0;i<n;i++)
       {
           sf("%d",&pol[i].sz);
           tot+=pol[i].sz;
       }
       pf("Case #%d:",t++);
       while(true)
       {
           sort(pol,pol+n,cmp);
           if(pol[0].sz==0) break;
           if(tot==2)
           {
               pf(" %c%c",pol[0].id+'A',pol[1].id+'A');
               pol[0].sz-=1;
               pol[1].sz-=1;
               tot-=2;

           }
           else if(pol[0].sz>1 && pol[1].sz<( (tot-2)/2 + (tot-2)%2))
           {
               pf(" %c%c",pol[0].id+'A',pol[0].id+'A');
               pol[0].sz-=2;
               tot-=2;
           }
           else if(pol[0].sz==1)
           {
               pf(" %c",pol[0].id+'A');
               pol[0].sz-=1;
               tot-=1;
           }
           else
           {
               pf(" %c%c",pol[0].id+'A',pol[1].id+'A');
               pol[0].sz-=1;
               pol[1].sz-=1;
               tot-=2;
           }

       }
       pf("\n");
    }
    return 0;
}
