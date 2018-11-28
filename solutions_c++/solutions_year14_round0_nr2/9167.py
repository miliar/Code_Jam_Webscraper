#include<iostream>
#include<stdio.h>
//using namespace std
int main()
{
int t,p;
scanf("%d",&t);
for(p=1;p<=t;p++)
{
	double tym=0,tf,rate=2;
	double c,f,x;
	scanf("%lf %lf %lf",&c,&f,&x);
	tf=x/rate;
	while(1)
	{
		tym+=c/rate;//farm purchased.
		rate+=f;
		if(tf>tym+(x/rate))
		{
	    	 tf=tym+(x/rate);			
		}
		else
		{
			break;
		}	  
		
	}
printf("case #%d: %lf\n",p,tf);
}
return 0;
}
