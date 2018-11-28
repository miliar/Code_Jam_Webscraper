#include <iostream>
#include <cstdio>
using namespace std;

int main() 
{
	double x,c,f,min,sum,prev,nf;
	int t,co;
	scanf("%d",&t);
	co=0;
	while(t--)
	{
		++co;
		scanf("%lf%lf%lf",&c,&f,&x);
		min=x/2;
		if(c<x)
		{
			prev=c/2; nf=2+f;
			while(1)
			{
				sum=prev+x/nf;
				if(sum<=min) min=sum;
				else break;
				prev=prev+c/nf;
				nf=nf+f;
			}
		}
		printf("Case #%d: %0.7lf\n",co,min);
	}
	return 0;
}