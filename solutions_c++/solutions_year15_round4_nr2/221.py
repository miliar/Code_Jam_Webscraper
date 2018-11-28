#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
const int maxn = 105;
int n, m, ans;
double v, x, eps = 1e-10;
struct node
{
	double r, c;
	void read()
	{
		scanf("%lf%lf", &r, &c);
	}
}a[maxn];
inline bool cmp(const node &a, const node &b)
{
	return a.c < b.c;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%d%lf%lf", &n, &v, &x);
		bool pl = 0, pr = 0;
		double slow = 0;
		for (int i = 1; i <= n; i++)
		{
			a[i].read();
			slow += a[i].r;
			if (fabs(a[i].c - x) < eps)
				pl = pr = 1;
			else if (a[i].c < x)
				pl = 1;
			else
				pr = 1;
		}
		printf("Case #%d: ", tt);
		if (pl == 0 || pr == 0)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		sort(a + 1, a + n + 1, cmp);
		double l = v / slow, r = 1e12, mid;
		for (int q = 1; q <= 500; q++)
		{
			double mid = (l + r) / 2, nowt = 0, nowv = 0;
			for (int i = 1; i <= n; i++)
				if (nowv + mid * a[i].r + eps > v)
				{
					nowt = (nowv * nowt + (v - nowv) * a[i].c) / v;
					nowv = v;
					break;
				}
				else
				{
					nowt = (nowv * nowt + mid * a[i].r * a[i].c) / (nowv + mid * a[i].r);
					nowv += mid * a[i].r;
				}
			if (nowt > x + eps)
			{
				l = mid;
				continue;
			}
			nowt = nowv = 0;
			for (int i = n; i >= 1; i--)
				if (nowv + mid * a[i].r + eps > v)
				{
					nowt = (nowv * nowt + (v - nowv) * a[i].c) / v;
					nowv = v;
					break;
				}
				else
				{
					nowt = (nowv * nowt + mid * a[i].r * a[i].c) / (nowv + mid * a[i].r);
					nowv += mid * a[i].r;
				}
			if (nowt + eps < x)
			{
				l = mid;
				continue;
			}
			r = mid;
		}
		printf("%.10f\n", l);
	}
	return 0;
}
