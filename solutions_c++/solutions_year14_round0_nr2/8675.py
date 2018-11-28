#include<stdio.h>
int main() 
{
	int t,test;
	double totaltime,rate,f,c,x;
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		rate=2.0;totaltime=0.0;
		if(x<c)
		{
			totaltime = x/rate;
		}
        else
        {
			while(c/rate+x/(rate+f)<x/rate)
			{
				totaltime+=c/rate;
				rate+=f;
			}
			totaltime+=x/rate;
        }
		printf("Case #%d: %0.7f\n",t,totaltime);
	}
	return 0;
}