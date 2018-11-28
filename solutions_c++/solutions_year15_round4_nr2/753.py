#include <bits/stdc++.h>
using namespace std;

const double EPS = 1e-8;

struct tap
{
	double v;
	double x;
	bool operator< (const tap& oth) const
	{
		if (fabs(x-oth.x) > EPS) return (x < oth.x);
		return (v < oth.v);
	}
};

tap t[2];
double v, x;
int n;
int T;

int main()
{
	scanf("%d", &T);
	for (int _ = 1;_ <= T;_++)
	{
		scanf("%d%lf%lf", &n, &v, &x);
		for (int i = 0;i < n;i++)
			scanf("%lf%lf", &t[i].v, &t[i].x);
		sort(t, t+n);
		double best = 1e+50;
		if (abs(t[0].x-x) < EPS)
			best = min(best, v/t[0].v);
		if (n == 2 && abs(t[1].x-x) < EPS)
			best = min(best, v/t[1].v);
		if (n == 2 && t[0].x-EPS < x && t[1].x+EPS > x)
		{
			if (fabs(t[0].x-x) > EPS)
			{
				double a = (x*t[1].v-t[1].v*t[1].x)/(t[0].v*t[0].x-x*t[0].v);
				double b = v/(a*t[0].v+t[1].v);
				a *= b;
				best = min(best, max(a, b));
			} else if (fabs(t[1].x-x) < EPS)
			{
				double req = v/(t[0].v+t[1].v);
				best = min(best, req);
			}
		}
		printf("Case #%d: ", _);
		if (best > 1e+49) printf("IMPOSSIBLE\n");
		else printf("%.9lf\n", best);
	}
	return 0;
}
