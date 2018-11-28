#include<iostream>
#include<cstdio>
#define gd(a) scanf("%lf",&a);
using namespace std;
int main()
{
  int t;
  scanf("%d",&t);
  for(int i=1;i<=t;i++)
  {
    double cost,rate,target;
    gd(cost);
    gd(rate);
    gd(target);
    double time = 0;
    double crate = 2;
    while(target/crate > (cost/crate + target/(crate+rate)))
    {
      time += (cost/crate);
      crate += rate;
      //printf("Bought... Rate: %lf Time:%lf\n",crate,time);
    }
    time += (target/crate);
    printf("Case #%d: %.7lf\n",i,time);
  }
}