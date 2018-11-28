#include<stdio.h>
int main()
{
double  cur_rate,C,F,cookies,X;
double  time_total,time1,time2; 
int t,k=0;
scanf("%d",&t);
while(++k<=t)
{

scanf("%lf %lf %lf",&C,&F,&X);
if(C>=X) {printf("Case #%d: %.7lf\n",k,X/2);continue;}
time_total=0;
cur_rate=2.000000;
cookies=0;
while(1)
{
time_total+= (C-cookies)/cur_rate;
cookies=C;
time1= (X-cookies)/cur_rate;
time2=(X-(cookies-C))/(cur_rate+F);
if(time1<=time2)
{
time_total += time1;
printf("Case #%d: %.7lf\n",k,time_total);
break;
}
else
{
 cookies=cookies-C;
 cur_rate+=F;
}
}//inner while ends

}//outer while ends
return 0;
}//main ends
