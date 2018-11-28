#include <iostream>
#include <set>
#include <cstdio>

using namespace std;

int main()
{
	int nrOfCases;
	cin >> nrOfCases;
	for (int c = 1; c <= nrOfCases; c++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		
		double sum = 0.0;
		
		double rate = 2.0;
		
		while (true)
		{
			double timeToPurchase = C / rate;
			double ttfWithoutPurchase = X / rate;
			double ttfWithPurchase = timeToPurchase + X / (rate + F);
			
			if (ttfWithoutPurchase < ttfWithPurchase)
			{
				sum += ttfWithoutPurchase;
				break;
			}
			else
			{
				sum += timeToPurchase;
				rate += F;
			}	
		}
		
		printf("Case #%d: %.7f\n", c, sum);
		
		
	}
}
