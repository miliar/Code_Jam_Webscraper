#include <iostream>
#include <cstdio>

using namespace std;

int T;
double C,F,X;

int main()
{
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);

  scanf("%d",&T);

  for(int cas=1;cas<=T;cas++)
  {
    scanf("%lf%lf%lf",&C,&F,&X);
    double tt=0,dmax=X/2.0;
    double ans=X/2.0;

    double v=2.0;
    while(tt+X/v<=dmax)
    {
      tt+=C/v;
      v+=F;
      double temp=tt+X/v;
      if(temp<ans)
        ans=temp;
      else
        break;
    }
    printf("Case #%d: %.7lf\n",cas,ans);
  }
  return 0;
}


