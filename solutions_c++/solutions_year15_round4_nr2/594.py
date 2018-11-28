#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>

#define pb push_back
#define mp make_pair
#define LL long long
#define LD long double
#define maxlongint 2147483647

using namespace std;

const int inf = 999999999;
const int mod = 1000000007;
const double eps = 1e-12;

inline int Getint()
{
	char ch = getchar();
	while (ch < '0' || ch > '9') ch = getchar();
	int ret = 0;
	while (ch >= '0' && ch <= '9') ret = ret * 10 + ch - '0', ch = getchar();
	return ret;
}

struct dwell
{
	double v, t;
};

dwell a[110];

inline bool cmp(const dwell &a, const dwell &b)
{
	return a.v * a.t > b.v * b.t;
}

int T, n;
double VOL, TEMP;

int main()
{
	freopen("123.in", "r", stdin);
	freopen("123.out", "w", stdout);
	T = Getint();
	for (int _ = 1; _ <= T; _++)
	{
		n = Getint(), scanf("%lf%lf", &VOL, &TEMP); VOL *= 100000.0;
		//printf("v, t = %.10lf %.10lf\n", VOL, TEMP);
		for (int i = 1; i <= n; i++)
		{
			scanf("%lf%lf", &a[i].v, &a[i].t);
			a[i].v *= 100000.0;
			a[i].t -= TEMP;
		}
		sort(a + 1, a + n + 1, cmp);
		LD l = 0.0, r = 0.0, ans = 1e14;
		for (int i = 1; i <= n; i++)
		{
			l += a[i].v;
			r += VOL / a[i].v;
		}
		l = VOL / l, r += eps * 2;
		bool flag = false;
		//l = 0.6633333332, r = 0.6633333334;
		//printf("l, r = %.10f %.10f\n", (double)l, (double)r);
		while (l + eps < r)
		{
			bool ff = true;
			LD mid = (l + r) / 2.0;
			//printf("l, r, mid = %.10f %.10f %.10f\n", (double)l, (double)r, (double)mid);
			LD up = 0.0, down = 0.0;
			LD v0 = VOL;
			for (int i = 1; i <= n; i++)
			{
				if (mid * a[i].v > v0)
				{
					up += a[i].t * v0;
					v0 = 0.0;
					break;
				}
				else
				{
					up += a[i].t * mid * a[i].v;
					v0 -= mid * a[i].v;
				}
			}
			if (v0 > eps) ff = false;
			LD v1 = VOL;
			for (int i = n; i > 0; i--)
			{
				if (mid * a[i].v > v1)
				{
					down += a[i].t * v1;
					v1 = 0.0;
					break;
				}
				else
				{
					down += a[i].t * mid * a[i].v;
					v1 -= mid * a[i].v;
				}
			}
			//printf("up, down = %.10f %.10f\n", (double)up, (double)down);
			if (v0 > eps) ff = false;
			if (down < eps && 0 < up + eps && ff)
			{
				flag = true;
				ans = mid;
				r = mid;
			}
			else
			{
				l = mid;
			}
		}
		if (!flag) printf("Case #%d: IMPOSSIBLE\n", _); else printf("Case #%d: %.10f\n", _, (double)ans);
	}
	return 0;
}
