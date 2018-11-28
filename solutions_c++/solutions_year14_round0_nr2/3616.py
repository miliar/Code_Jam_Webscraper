#include <iostream>
#include <cstdio>

using namespace std;


double farmtime (double c, double f)
{
	return (double)c/f;
}

double endtime (double f, double x)
{
	return (double)x/f;
}

int main (void)
{
	int T, caso = 1;
	cin >> T;

	while (T--)
	{
		double c, f, x;
		cin >> c >> f >> x;
		double persec = 2;
		double res = endtime(2, x);
		double t = 0.0;
		for (int i = 0; i < 100*x; ++i)
		{
			double fini = t + endtime(persec, x);
			if (fini  < res) res = fini;
			t += farmtime(c, persec);
			persec += f;
		}
		printf("Case #%d: %.15lf\n", caso++, res);
	}

	return 0;
}