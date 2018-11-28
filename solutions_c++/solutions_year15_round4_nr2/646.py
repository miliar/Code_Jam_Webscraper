#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;
typedef long long int64;
#define rep(x, n) for (int x = 1; x <= n; ++x)
#define zrp(x, n) for (int x = n; x; --x)
#define FOR(x, l, r) for (int x = l; x <= r; ++x)
#define foredge(i, x) for (int i = start[x]; i; i = e[i].l)
const int maxN = 105;
int ca, n;
double x[maxN], y[maxN], v, t;

int main()
{
	scanf("%d", &ca);
	rep(tt, ca)
	{
		scanf("%d%lf%lf", &n, &v, &t);
		printf("Case #%d: ", tt);
		if (n == 1)
		{
			scanf("%lf%lf", x + 1, y + 1);
			if (y[1] == t)
			{
				printf("%.9lf\n", v / x[1]);
			}
			else
				puts("IMPOSSIBLE");
		}
		else
		{
			rep(i, n)
			{
				scanf("%lf%lf", x + i, y + i);
			}
			if (y[1] > y[2])
			{
				swap(x[1], x[2]);
				swap(y[1], y[2]);
			}

			if (y[1] > t || y[2] < t)
				puts("IMPOSSIBLE");
			else
			{
				double ans;
				if (y[1] == y[2])
				{
					ans = v / (x[1] + x[2]);
				}
				else if (y[1] == t)
				{
					ans = v / x[1];
				}
				else if (y[2] == t)
				{
					ans = v / x[2];
				}
				else
				{
					double v1, v2;
					v1 = (v * t - v * y[2]) / (y[1] - y[2]);
					v2 = v - v1;
					ans = max(v1 / x[1], v2 / x[2]);
				}
				printf("%.9lf\n", ans);
			}
		}
	}
	return 0;
}
