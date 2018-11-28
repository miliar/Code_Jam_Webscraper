#include <stdio.h>

int main()
{
	int testCases;
	scanf("%d",&testCases);
	int t=0,i;
	double time1=0,time2=0,time3=0;
	double c,f,x;
	double times[100];
	double n;
	while(t!=testCases)
	{
		time1=0.0f,time2=0.0f,time3=0.0f;
		n=0.0f;
		scanf("%lf %lf %lf",&c,&f,&x);
		do
		{
			if(n==0.0f)
				time1=x/2.0f;
			else
				time1=time2;
			time3=time3+(c/(2.0f+(n*f)));
			time2=time3+(x/(2.0f+((n+1)*f)));
			n++;
		}while(time1>time2);
	times[t]=time1;
	t++;
	}
	for(i=0;i<testCases;i++)
	{
		printf("Case #%d: %f \n",i+1,times[i]);
	}
	while(1);
}
