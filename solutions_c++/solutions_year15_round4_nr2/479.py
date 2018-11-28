#include <iostream>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
using namespace std;

const int maxn = 1000;
const double eps = 1e-8;
int n, m;
double v[maxn], c[maxn], sumv, sumc;

void solve()
{
	scanf("%d %lf %lf", &n, &sumv, &sumc);
	for (int i = 0; i < n; ++i)
		scanf("%lf %lf", v+i, c+i);
	if (n == 1)
	{
		if (fabs(c[0]-sumc)<eps)
			printf("%.8lf\n", sumv/v[0]);
		else
			printf("IMPOSSIBLE\n");
		return;
	}
	if (n == 2)
	{
		if (fabs(c[0]-c[1])<eps)
		{
			if (fabs(c[0]-sumc)<eps)
				printf("%.8lf\n", sumv/(v[0]+v[1]));
			else
				printf("IMPOSSIBLE\n");
		}
		else
		{
			if (fabs(c[0]-sumc)<eps)
			{
				printf("%.8lf\n", sumv/v[0]);
				return;
			}
			if (fabs(c[1]-sumc)<eps)
			{
				printf("%.8lf\n", sumv/v[1]);
				return;
			}
			double y = sumv/v[1]*(c[0]-sumc)/(c[0]-c[1]);
			double x = (sumv/v[0] - v[1]/v[0]*y);
			if (x < -eps || y < -eps)
				printf("IMPOSSIBLE\n");
			else
				printf("%.8lf\n", fmax(x, y));
		}
		return;
	}
	printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}