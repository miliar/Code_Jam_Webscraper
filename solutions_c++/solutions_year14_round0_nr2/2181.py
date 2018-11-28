#include <stdio.h>
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int tests;
	scanf("%d",&tests);
	for (int kk = 1; kk <= tests; kk++)
	{
		double c,f,x;
		// scanf("%f %f %f",&c, &f, &x);
		cin >> c >> f >> x;
		// printf("%.2f %.2f %.2f\n", c,f,x);
		double cps = 2.0;
		double bestTime = x/cps;
		// printf("%.2f\n", x);
		double totalTime = 0;
		while(true)
		{
			double tempTime = totalTime + x/cps;
			if(tempTime <= bestTime)
				bestTime = tempTime;
			else
				break;
			totalTime += (c/cps);
			cps += f;
		}
		printf("Case #%d: %.7f\n", kk, bestTime);
	}
	return 0;
}