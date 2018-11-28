#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define INF (1 << 30)
#define SQR(a) ((a) * (a))

using namespace std;

const int N = 1111;

double r[N], c[N], n, v, x;

int main()
{
	freopen("asdf.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for (int t = 1; t <= tests; t++)
	{
		cin >> n >> v >> x;
		bool ls = false, la = false;
		for (int i = 0; i < n; i++)
		{
			cin >> r[i] >> c[i];
			if (c[i] <= x)
				ls = true;
			if (c[i] >= x)
				la = true;
		}
		if (!la || !ls)
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}
		if (n == 1)
		{
			printf("Case #%d: %.9f\n", t, (double)v / r[0]);
		}
		else
		{
			if (fabs(c[0] - x) < 1e-14 && fabs(c[1] - x) < 1e-14)
			{
				printf("Case #%d: %.9f\n", t, v / (r[0] + r[1]));
				continue;
			}
			double lo = 0, hi = v;
			if (c[0] > c[1])
			{
				swap(c[0], c[1]);
				swap(r[0], r[1]);
			}
			while (max(lo, hi) - min(lo, hi) >= 1e-13)
			{
				double m = (hi + lo) / 2;
				double v1 = m;
				double v2 = v - v1;
				double temp = (v1 * c[0] + v2 * c[1]) / (v1 + v2);
				if (temp <= x)
				{
					hi = m;
				}
				else
				{
					lo = m;
				}
			}
			printf("Case #%d: %.9f\n", t, max(lo / r[0], (v - lo) / r[1]));
		}
	}	

	return 0;
}
