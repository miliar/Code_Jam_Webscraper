#include<iostream>
#include<stdio.h>

using namespace std;


int main()
{
	double c,f,x,min,time,r;
	int t,p;
	scanf("%d",&t);
	
	for(int i=1;i<=t;i++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
	
		time = 0;
		min = 0;
		
		p=1;
		while(p)
		{
		
			time = 0;
		
			if( p==1)
			{	time = x/2;
				min = time;
			}
			else
			{
				r = 2;
				for(int j=0;j<p-1;j++)
				{	
					time += c/r;
					r = r+f;
				}
				
				time += x/r;
			}
		
			if(time > min)
			{
				p=0;
			}
			else
			{	min = time;
				p++;
			}
		}
		
			printf("Case #%d: %.7lf\n",i,min );
	}

}
