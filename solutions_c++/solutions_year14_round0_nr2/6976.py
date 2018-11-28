#include<stdio.h>
int main()
{
 int t,i;
 double c,f,x;
 double time,presRate,time1,time2,time3;
 double totalCookies;
 scanf("%d",&t);
 for(i=1;i<=t;i++)
  {
	scanf("%lf%lf%lf",&c,&f,&x);
	time = 0;
	presRate = 2.0;
	totalCookies = x;
	while(totalCookies>0)
	{
		time1 = totalCookies/presRate;
		time2 = c/presRate;
		time3 = totalCookies/(f+presRate) ;
		if(time1 < (time2+time3))
		{
			time = time + time1;
			totalCookies = 0;
		}
		else
		{
			presRate += f;
			time = time + time2;
		}
	}
	printf("Case #%d: %.7f\n",i,time);
  }		
  return 0;
}
