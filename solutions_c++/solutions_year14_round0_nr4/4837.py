#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int ans2, ans1, cnt;
double a[1010], b[1010];
int T, w, v[1010], n;
int main()
{
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("d.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) scanf("%lf", &a[i]);
		for (int i = 1; i <= n; i++) scanf("%lf", &b[i]);
		for (int i = 1; i <= n; i++) v[i] = 0;
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		cnt = 0;
		for (int i = 1; i <= n; i++)
		{
			for (int j = i; j <= n; j++)
			if ((!v[j]) && b[j] > a[i])
			{
				v[j] = 1;
				cnt++;
				break;
			}
		}
		ans1 = n - cnt;
		ans2 = 0;
		for (int i = 1; i <= n; i++)
		{
			cnt = 0;
			for (int j = 1; j < i; j++) if (a[j] > b[n - j + 1]) cnt++;
			for (int j = i; j <= n; j++)
				if (a[j] > b[j - i + 1]) cnt++;
			ans2 = max(ans2, cnt);
		}
		printf("Case #%d: ", ++w);
		printf("%d %d\n", ans2, ans1);
	}
	return 0;
}
