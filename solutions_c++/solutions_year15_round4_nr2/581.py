#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn = 110;
const double eps = 1e-8;
int t, n;
double v, x;
int dcmp(double x)
{
	return (x > eps) - (x < -eps);
}
struct roo
{
	double r, c;
	void read()
	{
		scanf("%lf%lf", &r, &c);
	}
	bool operator < (const roo &x) const
	{
		return dcmp(c - x.c) < 0;
	}
} p[maxn];
int main()
{
	scanf("%d", &t);
	for(int Case = 1; Case <= t; ++Case)
	{
		scanf("%d%lf%lf", &n, &v, &x);
		for(int i = 0; i < n; ++i)
			p[i].read();
		sort(p, p + n);
		if(dcmp(x - p[0].c) < 0 || dcmp(x - p[n - 1].c) > 0)
		{
			printf("Case #%d: IMPOSSIBLE\n", Case);
			continue;
		}
		if(n == 1)
			printf("Case #%d: %.12f\n", Case, v / p[0].r);
		else if(n == 2)
		{
			if(dcmp(p[0].c - p[1].c) != 0)
			{
				double tmp = v * (x - p[1].c) / (p[0].c - p[1].c);
				printf("Case #%d: %.12f\n", Case, max((v - tmp) / p[1].r, tmp / p[0].r));
			}
			else
				printf("Case #%d: %.12f\n", Case, v / (p[0].r + p[1].r));
		}
	}
	return 0;
}
