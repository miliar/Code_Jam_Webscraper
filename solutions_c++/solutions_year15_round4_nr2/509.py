#include<cstdio>
#include<algorithm>
using namespace std;

double r[2], t[2];

int main()
{
	int T, kase = 0;
	scanf("%d", &T);
	while (T--)
	{
		int n;
		double v, x;
		scanf("%d %lf %lf", &n, &v, &x);
		for (int i = 0; i < n; i++)
			scanf("%lf %lf", &r[i], &t[i]);
		printf("Case #%d: ", ++kase);
		if (n == 1)
		{
			if (t[0] == x)
				printf("%.8lf\n", v / r[0]);
			else
				printf("IMPOSSIBLE\n");
		}
		else
		{
			if (t[0] == t[1])
			{
				if (t[0] == x)
					printf("%.8lf\n", v / (r[0] + r[1]));
				else
					printf("IMPOSSIBLE\n");
			}
			else if (min(t[0], t[1]) > x || max(t[0], t[1]) < x)
				printf("IMPOSSIBLE\n");
			else
			{
				double v2 = (x - t[0]) / (t[1] - t[0]);
				double v1 = (x - t[1]) / (t[0] - t[1]);
				if (v1 < 0 || v2 < 0)
					printf("IMPOSSIBLE\n");
				else
				{
					double t1 = v1 / r[0];
					double t2 = v2 / r[1];
					printf("%.8lf\n", max(t1, t2) * v);
				}
			}
		}
	}
	return 0;
}