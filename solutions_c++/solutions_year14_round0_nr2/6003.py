#include<stdio.h>
int main()
{
	int t,z,count=0;
	double c,x,f,time=0;
	double rate=2;
	scanf("%d", &t);
	for(z=1;z<=t;z++)
	{
		scanf("%lf%lf%lf", &c,&f,&x);
			
			while(x/rate >= ((c/rate) + (x/(rate + f))))
			{
				time += c / rate;
				rate += f;
											
			}
			time += x/rate;
			
		printf("Case #%d: %0.7lf\n", z, time);
		time = 0; 	
		rate = 2;	
	}
	return 0;
}
