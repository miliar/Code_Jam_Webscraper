#include<stdio.h>

int main()
{
	int T;
	double C,F,X,time;
	int i,j,k;
	scanf("%d",&T);
	double sp;
	for(k=1;k<=T;k++)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		time = 0;
		sp = 2;
		while(X!=0)
		{
			time += C/sp;
			
			if(X*sp<(X-C)*(sp+F))
			sp = sp +F;
			else
			{
				time += (X-C)/sp;
				X = 0;
			}
			
			
			
		}
		printf("Case #%d: %.7lf",k,time);
		
	
	}
	return 0;
}
