#include<stdio.h>
#include<math.h>
double c,f,x;
int t;
int main()
{
    //freopen("ios.in","r",stdin);
    //freopen("ios.out","w",stdout);
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
      scanf("%lf %lf %lf",&c,&f,&x);
      if(c>=x) {printf("Case #%d: %.7lf\n",ca,x/2);continue;}
      double fx=(f*(x-c))/c;
      if(fx<2) {printf("Case #%d: %.7lf\n",ca,x/2);continue;}
      int p=(int)ceil((fx-2)/f);
      double ans=0.0;
      for(int i=0;i<=p;i++)
      ans+=(1.0/(2.0+i*f));
      ans=ans*c;
      ans+=(x-c)/(2.0+p*f);
      printf("Case #%d: %.7lf\n",ca,ans);
    }
}
