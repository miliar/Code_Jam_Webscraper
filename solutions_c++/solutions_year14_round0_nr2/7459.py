#include <cstdio>
using namespace std;
double C,F,X,ans;
int T,cas;
int main()
{
      freopen("B-large.in","r",stdin);
      freopen("B.out","w",stdout);
      scanf("%d",&T);
      for (cas = 1;cas<=T;++cas)
      {

            scanf("%lf%lf%lf",&C,&F,&X);
            ans =0.0;
            int t = 1 ;
            while(X/(2+t*F)+C/(2+(t-1)*F)<X/(2+(t-1)*F))
            {
                  ans+=C/(2+(t-1)*F);
                  ++t;
            }
            ans+=X/(2+(t-1)*F);
            printf("Case #%d: %.7lf\n",cas,ans);

      }
      return 0 ;
}
