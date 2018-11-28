#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

#define EPS 1E-9

int fcmp(double x, double y)
{
	if (fabs(x - y) < EPS) return 0;
	return (x > y ? 1 : -1);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int _, cases = 1;
	cin >> _;
	while (_--)
	{
		double C, F, X;
		double res = 0.0;
		cin >> C >> F >> X;
		int n = 0;
		while (true)
		{
			double t1 = X / (2.0 + (n + 1) * F) + C / (2.0 + n * F);
			double t2 = X / (2.0 + n * F);
			if (fcmp(t1, t2) == -1)
			{
				res += C / (2.0 + n * F);
				n++;
			}
			else
			{
				res += X / (2.0 + n * F);
				break;
			}
		}
		printf("Case #%d: %.7f\n", cases++, res);
	}
	return 0;
}