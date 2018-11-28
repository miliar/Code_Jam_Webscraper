#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

double solve(double c, double f, double x)
{
	double result;
	double coef = 0;
	double best = x / 2.;
	for(double i = 0; true; ++i)
	{
		coef += 1./(2 + i*f);
		result = c*coef + x/(2 + f*(i + 1));
		if (best < result) return best;
		best = result;
	}
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 0; t < T; ++t)
	{
		double c, f, x;
		cin >> c >> f >> x;
		printf("Case #%d: %.7f\n", t+1, solve(c,f,x));
	}
	return 0;
}

