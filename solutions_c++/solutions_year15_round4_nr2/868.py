#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#define eps 1e-6
using namespace std;
int n;
double fV, fX;
double V, X;
struct st
{
	double x;
	double v;
	double vmul;
}a[100001];
bool operator < (const st &xx, const st & yy)
{
	return xx.vmul < yy.vmul;
}
double calc(double tmax)
{
	double nowx = 0, nowv = 0;
	for (int i = 1; i <= n; i++)
	{
		if (i == 1)
		{
			nowx = a[i].x;
			nowv = a[i].v * tmax;
		} else
		{
			nowx = (nowx * nowv + a[i].v * a[i].x * tmax) / (nowv + a[i].v * tmax);
			nowv += a[i].v * tmax;
		}
	}
	if (nowx > X)
	{
		for (int i = n; i >= 1; i--)
		{
			if (nowx <= X + eps) return nowv;
			if (i == 1 || a[i].x <= X - eps) return 0;
			if ((nowx * nowv - a[i].v * a[i].x * tmax) / (nowv - a[i].v * tmax) > X - eps)
			{
				nowx = (nowx * nowv - a[i].v * a[i].x * tmax) / (nowv - a[i].v * tmax);
				nowv -= a[i].v * tmax;
			} else
			{
				double tmp = (nowx * nowv - X * nowv) / (tmax * (a[i].x - X));
				nowx = X;
				nowv -= tmp * tmax;
			}
		}
		return nowv;
	} else
	if (nowx < X - 1e-7)
	{
		for (int i = 1; i <= n; i++)
		{
			if (nowx + eps >= X) return nowv;
			if (i == n || a[i].x >= X) return 0;
			if ((nowx * nowv - a[i].v * a[i].x * tmax) / (nowv - a[i].v * tmax) < X)
			{
				nowx = (nowx * nowv - a[i].v * a[i].x * tmax) / (nowv - a[i].v * tmax);
				nowv -= a[i].v * tmax;
			} else
			{
				double tmp = (nowx * nowv - X * nowv) / (tmax * (a[i].x - X));
				nowx = X;
				nowv -= tmp * tmax;
			}
		}
		return nowv;
	}
	return nowv;
}
int main()
{
	int tot, tt, pop;
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		if (tt == 8)
			pop = 1;
		scanf("%d%lf%lf", &n, &fV, &fX);
		V = fV;
		X = fX;
		double dv = 0;
		double left = 0, right = 0, vmax;
		memset(a, 0, sizeof(a));
		for (int i = 1; i <= n; i++)
		{
			double vv, xx;
			scanf("%lf%lf", &vv, &xx);
			double sv = vv, sx = xx;
			right = right > (V / sv ) ? right : (V/sv);
			st tmp;
			tmp.x = sx;
			tmp.v = sv;
			tmp.vmul = sx;
			if (fabs(sx - X) < eps)
			{
				dv += sv;
				i--;
				n--;
			} else
			{
				a[i] = tmp;
			}
		}
		sort(a + 1, a + n + 1);
		vmax = right;
		right += 1;
		if (calc(right) + dv * right <= V)
			printf("Case #%d: IMPOSSIBLE\n", tt);
		else
		{
			while (left < right - 1e-6)
			{
				double mid = (left + right) / 2;
				if (calc(mid) + dv * mid < V)
					left = mid;
				else
					right = mid;
			}
			printf("Case #%d: %.7lf\n", tt, left); 
		}
	}
	return 0;
}
