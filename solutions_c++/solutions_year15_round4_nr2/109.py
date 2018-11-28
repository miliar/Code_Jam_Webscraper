#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>

using namespace std;

#define EPS 0.0000001

bool equ(double a, double b)
{
	return abs(a - b) < EPS;
}

int wi[200];
double r[200], c[200];

pair<double, double> sei[200];

int main()
{
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; k++)
	{
		int n;
		double v, x;
		scanf("%d%lf%lf", &n, &v, &x);
		double all = 0.0;
		double sa = 0.0;
		double ba = 0.0;
		for (int i = 0; i < n; i++)
		{
			scanf("%lf%lf", r + i, c + i);
			all += r[i];
			if (equ(x, c[i]))
			{
				wi[i] = 0;
			}
			else if (c[i] < x)
			{
				wi[i] = -1;
				sa += (x - c[i]) * r[i];
			}
			else
			{
				wi[i] = 1;
				ba += (c[i] - x) * r[i];
			}
			sei[i] = make_pair(c[i], r[i]);
		}
		sort(sei, sei + n);
		if (sa < ba)
		{
			for (int i = n - 1; i >= 0; i--)
			{
				double s = sei[i].first - x;
				if (ba - sa > sei[i].second * s)
				{
					all -= sei[i].second;
					ba -= sei[i].second * s;
				}
				else
				{
					double y = (ba - sa) / s;
					all -= y;
					ba -= y * s;
					break;
				}
			}
		}
		else if (ba < sa)
		{
			for (int i = 0; i < n; i++)
			{
				double s = x - sei[i].first;
				if (sa - ba > sei[i].second * s)
				{
					all -= sei[i].second;
					sa -= sei[i].second * s;
				}
				else
				{
					double y = (sa - ba) / s;
					all -= y;
					sa -= y * s;
					break;
				}
			}
		}
		if (!equ(sa, ba) || equ(all, 0.0))
		{
			printf("Case #%d: IMPOSSIBLE\n", k + 1);
		}
		else
		{
			printf("Case #%d: %.7lf\n", k + 1, v / all);
		}
	}
	return 0;
}
