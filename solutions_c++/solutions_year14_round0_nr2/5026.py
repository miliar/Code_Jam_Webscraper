#include <iostream>
#include<cstdio>
using namespace std;
int main() {
	int t,i,j,k,test;
	double C,F,X,y,rate,time;
	scanf("%d",&t);
	for(test=1;test<=t;test++)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		if(X<=C)
		{
			printf("Case #%d: %0.7lf\n",test,X/2);
		}
		else
		{
			time=0.0;
			y=X;
			rate=2.0;
			while(1)
			{
				if((y-C)/rate>y/(rate+F))
				{
					time+=(C/rate);
					rate+=F;
				}
				else
				{
					time+=y/rate;
					break;
				}
			}
			printf("Case #%d: %0.7lf\n",test,time);


		}
	}


	return 0;
}
