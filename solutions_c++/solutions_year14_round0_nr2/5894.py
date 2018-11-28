#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

//#define SMALL
#define LARGE

double checkTime(double c, double f, double x)
{
	double totalTime = 0.0, cps = 2.0;
	bool bestCase = false;

	if ((x / 2.0) <= 1.000000000000) return x / 2.0;

	while (bestCase == false)
	{
		//Checks if it is worth buying a farm
		if (totalTime + (x / cps) > totalTime + (c / cps) + (x / (cps + f)))
		{
			//Buys farm
			totalTime += (c / cps);
			cps += f;
		}
		else
		{
			totalTime += (x / cps);
			bestCase = true;
		}
	}

	return totalTime;
}

int main()
{
#ifdef SMALL
	ifstream in("b-small-attempt0.in");
	ofstream out("b-small.out");
#endif
#ifdef LARGE
	ifstream in("b-large.in");
	ofstream out("b-large.out");
#endif

	int testCases, cCase = 1;
	double c, f, x;
	int cCookies = 0;

	in >> testCases;

	while (cCase <= testCases)
	{
		in >> c >> f >> x;

		double totalTime = checkTime(c, f, x);

		out << "Case #" << cCase << ": " << setprecision(10) << fixed << totalTime << endl;

		cCase++;
	}

	in.close();
	out.close();

	return 0;
}