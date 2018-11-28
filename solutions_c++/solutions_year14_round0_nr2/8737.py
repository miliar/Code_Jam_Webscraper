#include <stdio.h>
double count(double c,double f,double x)
{
	double limit=x/2,speed=2,ans=limit,used=0;
	do
	{
		limit-=c/speed;
		used+=c/speed;
		speed+=f;
		if(ans>used+x/speed)ans=used+x/speed;else break;
	}while(limit>0);
	return ans;
}
int main(void)
{
	int t;
	double c,f,x;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: %.7lf\n",k,count(c,f,x));
	}
	return 0;
}