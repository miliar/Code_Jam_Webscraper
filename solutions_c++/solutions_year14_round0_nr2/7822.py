#include<stdio.h>
#include<string.h>
double C,F,X;
double solve(double farm_cost, double per_second, double target) {
//   if(per_second>=target)
//     return per_second;
  double direct_time = target/per_second;
  double not_direct_time = farm_cost/per_second + target/(per_second+F);
  if(direct_time - not_direct_time < 0)
    return direct_time;
  double recursion_time = solve(farm_cost, per_second+F,target);
  recursion_time+=farm_cost/per_second;
  return recursion_time;
}
int main()
{
  freopen("B-small-attempt4.in","r",stdin);
  freopen("B-small-attempt4.out","w",stdout);
  int T; 
  scanf("%d",&T);
  for(int t=1;t<=T;t++) {
    scanf("%lf %lf %lf",&C,&F,&X);
    printf("Case #%d: %.7lf\n",t,solve(C,2.0,X));
  }
  return 0;
}