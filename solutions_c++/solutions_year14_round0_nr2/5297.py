#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{

	int ii,tt;
	double c,f,x,time,v,min;
	freopen("B-large.in","r",stdin);
	freopen("000.txt","w",stdout);
	scanf("%d",&tt);
	for(ii=1;ii<=tt;ii++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		min=x/2;
		time=0;
		v=2.0;
		while(1)
		{
			time=time+c/(v+0.0);
			v=v+f;
			if (time+(x+0.0)/v<min) min=time+(x+0.0)/v;
			if (time>min)  break;
		}
		printf("Case #%d: %lf\n",ii,min);
	}
	
}