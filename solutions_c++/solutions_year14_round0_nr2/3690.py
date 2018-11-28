#include<iostream>
#include<cstdio>

using namespace std;


int main()
{
	int t;
	double cost , fac , x;
	
	scanf("%d",&t);
	for(int k = 1 ; k <= t ; k++)
	{
		scanf("%lf %lf %lf", &cost , &fac , &x);
		
		
		double in = 2;
		double went = 0;
		double have = 0;
		double mini = 100000000;
		bool update = true;
		
		while(update)
		{
			update = false;
			double value = x/in + went;
			if(value < mini)
			{
				mini = value;
				update = true;
			}
			went += cost/in;
			in += fac;
		}
		
		printf("Case #%d: %.7lf\n", k, mini);
	}
	return 0;
}


