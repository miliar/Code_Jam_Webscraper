#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <functional>
#include <stdint.h>

using namespace std;

#define forl(i,a,b) for(int i = a; i < b; ++i)


int main()
{
	int numCases;
	cin >> numCases;

	forl(caseNo, 1, numCases+1)
	{
		double time = 0;
		double c, f, x;
		// c = cookies to buy a farm
		// f = amount to increase cookie rate per farm
		// x = target number of cookies
		cin >> c >> f >> x;
		double cookierate = 2.0;
		double cookies = 0.0;
		double timeSoFar = 0.0;
		double besttime = x / cookierate;
		for(;;)
		{
			double timeToFarm = c/cookierate;
			cookierate += f;
			double timeToEnd = x/cookierate;
			timeSoFar += timeToFarm;
			if (timeSoFar + timeToEnd < besttime)
			{
				besttime = timeSoFar + timeToEnd;
			}
			else
				break;
		}
		cout << "Case #" << caseNo << ": " << fixed << setprecision(7) << besttime << endl;

	}
	return 0;
}
