#include <iostream>
#include "tasks.h"

using namespace std;

double calculateTime(int factoryCount, double factoryPrice, double factorySpeed, double cookieTarget)
{
	if (factoryCount < 0)
		return INT_MAX;

	double cps = 2;
	double time = 0;

	for (int n = 0; n < factoryCount; ++n)
	{
		time += factoryPrice / cps;
		cps += factorySpeed;
	}

	time += cookieTarget / cps;

	return time;
}

double findOptimal(double c, double f, double x)
{
	if (x <= c)
	{
		return x / 2.0;
	}
	else
	{
		double minTime = calculateTime(0, c, f, x);

		//double minTime = INT_MAX;

		int factoryCount = 0;
		int minFactoryCount = 0;
		int factorySkip = 5000;

		while (true)
		{
			double timeA = calculateTime(factoryCount - factorySkip, c, f, x);
			double timeB = calculateTime(factoryCount + factorySkip, c, f, x);

			double time = timeA < timeB ? timeA : timeB;

			if (minTime <= time)
			{
				if (factorySkip == 1)
					return minTime;
				else
				{
					factorySkip /= 2;

					if (factorySkip < 10)
						factorySkip = 1;
				}
			}
			else
			{
				minTime = time;
				factoryCount += (timeA < timeB ? - factorySkip : factorySkip);
			}
		}
	}
}

void cookieClicker()
{
	cout.precision(10);

	int cases;
	cin >> cases;

	for (int n = 1; n <= cases; ++n)
	{
		double c, f, x;

		cin >> c;
		cin >> f;
		cin >> x;

		double time = findOptimal(c, f, x);

		cout << "Case #" << n << ": " << time << endl;
	}

	system("pause");
}