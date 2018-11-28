#include<stdio.h>
#include<stdlib.h>
int main()
{
	FILE *fp1, *fp2;
	fp1=freopen("input2.txt","r",stdin);
	fp2=freopen("output.txt","w",stdout);
	long t,i;
	scanf("%ld",&t);
	for(i=0;i<t;i++)
	{
		double f, c, x;
		scanf("%lf %lf %lf",&c,&f,&x);
		double time=0.0, rate=2.0;
		while(true)
		{
			double t1=c/rate + x/(rate+f);
			double t2=x/rate;
			if(t1<t2)
			{
				time+=c/rate;
				rate+=f;
			}
			else
			{
				time+=t2;
				break;
			}
		}
		printf("Case #%d: %lf\n",i+1,time);
	}
	return 0;
}
