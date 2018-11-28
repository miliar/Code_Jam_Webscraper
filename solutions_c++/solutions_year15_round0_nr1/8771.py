#include    <bits/stdc++.h>
#define     sc          scanf
#define     pf          printf
#define     REP(i,a,b)  for(int i=(a);i<(b);i++)
#define     CLR(m,x)    memset(m,x,sizeof(m))
#define     __CASE      int _;for(sc("%d",&_);_;_--)
#define     __nCASE     int _(1),__;for(sc("%d",&__);_<=__;_++)
#define     LOCAL       freopen("test.txt","r",stdin)
#define     _LOCAL      freopen("A-large.in","r",stdin);freopen("output.txt","w",stdout);
using namespace std;
typedef double DB;
typedef long long LL;
/********************************************************/
int main()
{
      int cc, extra, sum, n, t;
      char c;
      __nCASE
      {
            sc("%d", &n);
            extra = 0;
            sum = 0;
            for(int i=0; i<=n; i++){
                  sc(" %c", &c);
                  cc = c - '0';
                  if( sum<i ) {
                        t = i - sum;
                        extra += t;
                        sum += t;
                  }
                  sum += cc;
            }
            pf("Case #%d: %d\n", _, extra);
      }
      return 0;
}
