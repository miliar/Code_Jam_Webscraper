#include <iostream>
#include <fstream>
#include <stdint.h>
#include <stdio.h>

using namespace std;

double ComputeMinTime(double fabricCost, double cookieBoost, double neededCookies, double cookiesPerSec = 2.0)
{
	double timeWithNoFabrics = neededCookies / cookiesPerSec;
	
	double currentCookiesPerSec = cookiesPerSec;
	double currentProduceTime = timeWithNoFabrics;
	double currentTimeOverhead = 0;

	while (true)
	{
		double nextTimeOverhead = currentTimeOverhead + fabricCost / currentCookiesPerSec;
		double nextProduceTime = neededCookies / (currentCookiesPerSec + cookieBoost);
		if (nextTimeOverhead - currentTimeOverhead > currentProduceTime - nextProduceTime)
		{
			break;
		}
		else
		{
			currentTimeOverhead = nextTimeOverhead;
			currentProduceTime = nextProduceTime;
			currentCookiesPerSec += cookieBoost;
		}
	}

	return currentProduceTime + currentTimeOverhead;
}

int main(int argc, char* argv[])
{
	ifstream inputFile;
	inputFile.open(argv[1]);

	uint64_t casesCount = 0;
	inputFile>>casesCount;

	for (uint64_t caseNumber = 1; caseNumber <= casesCount; ++caseNumber)
	{
		double fabricCost = 0.0, cookieBoost = 0.0, neededCookies = 0.0;
		inputFile>>fabricCost;
		inputFile>>cookieBoost;
		inputFile>>neededCookies;
		
		printf("Case #%llu: %.7f\n", caseNumber, ComputeMinTime(fabricCost, cookieBoost, neededCookies));
	}

	inputFile.close();

	return 0;
}