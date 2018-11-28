#include <cstdio>
#include <cstdlib>
#include <algorithm>
struct arr{
	long long x, y;
	bool operator < (const arr &o) const{
		return (x < o.x || (x == o.x && y > o.y));
	}
}a[4000], s[4000];
int now, w, T, tot;
long long n, m, ans, cnt;
long long get(long long x)
{
	return (x * n - ((x * (x - 1)) >> 1)) % 1000002013ll;
}
using namespace std;
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%I64d%I64d", &n, &m);
		for (int i = 1; i <= m; i++)
		{
			scanf("%d%d%d", &a[i].x, &a[i + m].x, &a[i].y);
			a[i + m].y = -a[i].y;
			ans += get(a[i + m].x - a[i].x) * a[i].y % 1000002013ll;
		}
		m *= 2;
		sort(a + 1, a + m + 1);
		tot = 0;
		for (int i = 1; i <= m; i++)
		{
			if (a[i].y > 0)
				s[++tot] = a[i];
			else
			{
				while (a[i].y < 0)
				{
					cnt = min(-a[i].y, s[tot].y);
					a[i].y += cnt, s[tot].y -= cnt;
					ans -= get(a[i].x - s[tot].x) * cnt % 1000002013ll;
					if (ans < 0) ans += 1000002013ll;
					if (s[tot].y == 0) tot--;
				}
			}
		}
		printf("Case #%d: ", ++w);
		printf("%I64d\n", ans);
		ans = 0;
	}
	return 0;
}
