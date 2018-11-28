#include <iostream>
#include <stdio.h>

using namespace std;

int main(void)
{
	int cases;
	double seconds = 0, cps = 2;
	double C, F, X;
	cin >> cases;
	for(int i = 0; i < cases; i++)
	{
		cin >> C;
		cin >> F;
		cin >> X;
		while((X/cps) > ((C/cps)+(X/(cps+F))))
		{
			seconds += (C/cps);
			cps += F;
		}
		seconds += X/cps;
		printf("Case #%d: %.7f\n", i+1, seconds);
		seconds = 0;
		cps = 2;
	}
	
	
	
	return 0;
}
