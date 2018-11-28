#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

int n;
double v, t;
double r[105], ti[105];

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 0; tt < T; tt++)
	{
		scanf("%d%lf%lf", &n, &v, &t);
		for (int i = 0; i < n; i++)
			scanf("%lf%lf", &r[i], &ti[i]);

		printf("Case #%d: ", tt + 1);
		if (n == 1)
		{
			if (fabs(ti[0] - t) > 1e-5)
				printf("IMPOSSIBLE\n");
			else
				printf("%.9lf\n", v / r[0]);
		}
		else
		{
			if ((ti[0]-t) * (ti[1] - t) > 1e-9)
				printf("IMPOSSIBLE\n");
			else if (fabs(ti[0] - ti[1]) < 1e-5)
				printf("%.9lf\n", v / (r[0] + r[1]));
			else
			{
				double v1 = v * (t - ti[1]) / (ti[0] - ti[1]), v2 = v - v1;
				printf("%.9lf\n", max(v1 / r[0], v2 / r[1]));
			}
		}
	}


	return 0;
}