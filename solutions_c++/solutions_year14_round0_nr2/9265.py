#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

double solve( double c, double f, double x )
{
	double mint = x / 2.0;
	double ft = c / 2.0;
	for (double n = 1.0; /*n < 100000*/; n += 1.0)
	{
		double p = f * n + 2.0;
		double t = ft + x / p;
		if (t >= mint)
			break;
		mint = t;
		ft += c / (f * n + 2.0);
	}
	return mint;
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; ++i)
	{
		double c, f, x;
		cin >> c >> f >> x;
		double t = solve( c, f, x );
		cout.precision(10);
		cout << "Case #" << i + 1 << ": " << t << endl;
	}

	return 0;
}
