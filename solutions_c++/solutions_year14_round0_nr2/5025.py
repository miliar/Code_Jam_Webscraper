#include <iostream>
#include<stdio.h>
using namespace std;

int main() 
{
	int t;
	scanf("%d",&t);
	int t1=t;double c,f,x,time=0,cookie=2;
	while(t--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		while(true)
		{
			if((x/cookie)<=((c/cookie)+(x/(cookie+f))))
			{
				time+=x/cookie;
				break;
			}
			else
				time+=c/cookie;cookie+=f;
		}
				printf("Case #%d: %.7f\n",t1-t,time);
				time=0;cookie=2;
	}
	return 0;
}