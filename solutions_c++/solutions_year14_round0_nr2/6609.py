#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,ccase=0;
	double c,f,x,current,time;
	scanf("%d",&t);
	while(t--)
	{
		ccase++;
		current=2.0;
		time=0.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		while(1)
		{
			if((c/current)+(x/(current+f))<(x/current))
			{
				time+=c/current;
				//cout<<current<<" "<<time<<"\n";
				current=current+f;
				continue;
			}
			time+=x/current;
			//cout<<current<<" "<<time;
			break;
		}
		printf("Case #%d: %0.7lf\n",ccase,time);
	
	}
	return 0;

}