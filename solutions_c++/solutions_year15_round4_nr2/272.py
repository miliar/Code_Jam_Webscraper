#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

const long double eps = 1e-16;
const int maxn = 1100;
struct data
{
	long double f, x;
};

int n, num, ca;
long double v, x;
data a[maxn];

bool cmp(const data & a ,const data & b)
{
	return a.x < b.x;
}
void solve()
{
	sort(a + 1, a + n + 1, cmp);
	long double l = 0, r = 1e15;
	while (abs(r - l) > 1e-10)
	{
		long double k = (r + l) / 2.0;
		
		long double Min_v = 0, Min_x = 0, Max_v = 0, Max_x = 0;
			
		for (int i = 1; i <= n; i++)
		{
			if (Min_v + k * a[i].f > v)
			{
				Min_x = (Min_v * Min_x + (v - Min_v) * a[i].x) / v;
				Min_v = v;
				break;
			}
			else
			{
				Min_x = (Min_v * Min_x + k * a[i].f * a[i].x) / (Min_v + k * a[i].f);
				Min_v = Min_v + k * a[i].f;
			}
		}

		for (int i = n; i >= 1; i--)
		{
			if (Max_v + k * a[i].f > v)
			{
				Max_x = (Max_v * Max_x + (v - Max_v) * a[i].x) / v;
				Max_v = v;
				break;
			}
			else
			{
				Max_x = (Max_v * Max_x + k * a[i].f * a[i].x) / (Max_v + k * a[i].f);
				Max_v = Max_v + k * a[i].f;
			}
		}

		if ((abs(Min_v - v) >eps) || (abs(Max_v - v) > eps))
		{
			l = k;
		}
		else if ((Min_x < x || abs(Min_x - x) < eps) && (Max_x > x || abs(Max_x - x) < eps))
		{
			r = k;
		}
		else l = k;

	}
	
	printf("Case #%d: ", ++ca);
	double ans = l;
	if (abs(ans - 1e15) < eps) printf("IMPOSSIBLE\n"); else printf("%.9lf\n", ans);
}
void init()
{
	cin >> num;
	while (num--)
	{
		cin >> n >> v >> x;
		for (int i = 1; i <= n; i++) cin >> a[i].f >> a[i].x;
		solve();
	}
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("jb.out","w",stdout);
	init();
	return 0;
}
