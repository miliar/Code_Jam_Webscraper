// CodeJam 2014: sudip1401
#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		
		double total = 0;
		double rate = 2;
		while(1)
		{
			double a = x/rate;
			double d = c/rate;
			double b = d + x/(rate + f);
			if(a < b)
			{
				total += a;
				break;
			}
			else
			{
				total += d;
				rate += f;
			}
		}
		
		printf("Case #%d: %.7lf\n",t,total);
	}
	return 0;
}
