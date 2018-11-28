#include<stdio.h>
#include<stdlib.h>
int main()
{
	int t,l;
	double f,c,x;
	scanf("%d",&t);
	for(l=1;l<=t;l++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		double T=0.0,r=2.0,chp=0.0;
		while(chp<x)
		{
			double t1=T+x/r;
			double t2=T+c/r+x/(f+r);
			if(t1>t2)
			{
				T=T+c/r;
				r=r+f;
				
			}
			else
			{
				T=T+x/r;
				break;
			}
		}
		printf("Case #%d: %lf\n",l,T);
	}
	}