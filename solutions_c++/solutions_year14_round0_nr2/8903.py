#include <iostream>

using namespace std;

void ComputeTest()
{
	double factoryCost;
	double factoryProd;
	double finalValue;
	
	cin >> factoryCost;
	cin >> factoryProd;
	cin >> finalValue;
	
	double currentTime = 0.0;
	double currentProduction = 2.0;
	double cookies = 0.0;
	
	while (true)
	{
		double nextFactoryCost = factoryCost / currentProduction;
		
		double finishCost = finalValue / currentProduction;
		double finishWithNextFactoryCost = nextFactoryCost + (finalValue / (currentProduction + factoryProd));

//cout << "nextFactoryCost " << nextFactoryCost << "\n";
//cout << "finishCost " << finishCost << "\n";
//cout << "finishWithNextFactoryCost " << finishWithNextFactoryCost << "\n";
		
		if (finishWithNextFactoryCost >= finishCost)
		{
			// wypad;
			currentTime += finishCost;
			break;
		}
		else
		{
			currentTime += nextFactoryCost;
			currentProduction += factoryProd;
		}
	}

	cout.precision(7);
	cout << fixed << currentTime;
}

int main()
{
	int tests;
	
	cin >> tests;
	for (int i = 1; i <= tests; ++i)
	{
		cout << "Case #" << i << ": ";
		
		ComputeTest();
		
		cout << "\n";
	}
	
	return 0;
}