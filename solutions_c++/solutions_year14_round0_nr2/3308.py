#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;
#define eps 1e-9
#define zero(x) ((fabs(x)<eps?0:x))
int main()
{
    freopen("data.in","r",stdin);
  freopen("data.out","w",stdout);
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
      double c,f,x;
      double minn=100000.0;
      double dan=2.0;
      double a=0;
      scanf("%lf%lf%lf",&c,&f,&x);
      double qian;
      qian=10000000.0;
      while(1)
      {
          double as=x/dan+a;
          minn=min(minn,as);
         // cout<<dan<<" "<<a<<" "<<as<<endl;
          a=a+c/dan;
          dan=dan+f;
          if(as>qian)break;
          else qian=as;
      }
     // printf("%.7lf\n",dan);
      printf("Case #%d: %.7f\n",t,minn+eps);
  }
  return 0;
}
