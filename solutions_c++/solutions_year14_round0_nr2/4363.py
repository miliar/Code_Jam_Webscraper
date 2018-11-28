#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main()
{
double c=0,f=0,x=0,time=0,rate=2;
int t=0,i=0;
scanf("%d",&t);
for(i=1;i<=t;i++)
{
    c=0,f=0,x=0,rate=2;
scanf("%lf",&c);
scanf("%lf",&f);
scanf("%lf",&x);

time=0;
while(1)
{
 if((x/rate)<=((c/rate)+(x/(rate+f))))
    break;
 time+=(c/rate);
 rate+=f;
}
time+=(x/rate);
printf("Case #%d: %lf\n",i,time);

}
return 0;
}
