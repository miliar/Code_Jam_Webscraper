#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int test;
	double C, F, X;
	
	cin >> test;
	for(int cas = 1; cas <= test; cas ++)
	{
		cin >> C >> F >> X;
		
		double best = 1000000000;
		double now = 0;
		double produce = 2;
		
		for(int i = 0; i < 10000; i ++)
		{
			if(X/produce+now < best)
				best = X/produce+now;
			
			now += C/produce;
			produce += F;
		}
		
		printf("Case #%d: %0.7lf\n", cas, best);
	}
	
	return 0;
}