#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int n, a[100010], w, ans, l, r, T, m;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		ans = 0;
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
		sort(a + 1, a + n + 1);
		l = 1, r = n;
		while (l <= r)
		{
			if (a[l] + a[r] <= m) l++, r--;
			else r--;
			ans++;
		}
		printf("Case #%d: %d\n", ++w, ans);
	}
	return 0;
}
