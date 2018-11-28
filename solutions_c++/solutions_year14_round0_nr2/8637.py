#include <iostream>
#include "tasks.h"

using namespace std;

double calculateTime(int factoryCount, double factoryPrice, double factorySpeed, double cookieTarget)
{
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
		double lastTime = INT_MAX;
		bool found = false;

		for (int n = 0;; ++n)
		{
			double time = calculateTime(n, c, f, x);

			if (lastTime < time)
			{
				return lastTime;
			}

			lastTime = time;
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

	//system("pause");
}