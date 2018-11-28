#include<stdio.h>

FILE *out = fopen("output.txt","w");
double X,C,F;
double now,time;
int low=0,high=100000,T,CC=0;
double dap=0,before=9999999999;
int main()
{
	int i,j,n;
	scanf("%d",&T);
	while(T--)
	{
		CC++;
		scanf("%lf %lf %lf",&C,&F,&X);
		now = 2;
		before = 9999999999;
		dap=0,time=0;
		for(i=0;i<=100000;i++)
		{
			dap = X/now+time;
			if(dap>before){
				printf("Case #%d: %.7lf\n",CC,before);
				break;
			}
			time+=C/now;
			now+=F;
			before = dap;
		}
	}
	return 0;
}