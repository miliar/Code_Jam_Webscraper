#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const double eps = 1e-12;

bool doubleEqual(double a, double b)
{
	return fabs(a - b) < eps;
}

bool doubleLess(double a, double b)
{
	return a < b && !doubleEqual(a, b);
}

bool doubleLessOrEqual(double a, double b)
{
	return a < b || doubleEqual(a, b);
}

double c, f, x;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int q;
	scanf("%d", &q);
	for (int t = 0; t < q; t++)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		double f0 = 2.0;
		double sum = 0;
		double ans = x / f0;
		if (doubleLess(c, x))
		{
			for (int i = 1; ; i++)
			{
				double cur = sum + c / f0 + x / (f0 + f);
				if (doubleLess(cur, ans))
				{
					sum += c / f0;
					f0 += f;
					ans = cur;
				}
				else
				{
					break;
				}
			}
		}
		printf("Case #%d: %.9lf\n", t + 1, ans);
	}
	return 0;
}