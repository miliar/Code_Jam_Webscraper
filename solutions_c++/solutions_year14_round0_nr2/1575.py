#include<stdio.h>
int main()
{
  //freopen("B-large.in","r",stdin);
  int T;
  scanf("%d",&T);
  int ca=0;
  double C,F,X;
  double res;
  double rate;
  while(T--)
  {
    scanf("%lf%lf%lf",&C,&F,&X);
    rate = 2.0;
    double last = X/rate;
    res = last;
    int farm = 0;
    while(1)
    {
      double tmp = res - last + C/rate + X/(rate+F);
      //printf("%lf %lf %lf %lf\n", tmp, res,last,C/rate);
      if(tmp>res)
        break;
      rate += F;
      last = X/rate;
      res = tmp;
    }
    printf("Case #%d: ",++ca);
    printf("%lf\n", res);

  }
}
