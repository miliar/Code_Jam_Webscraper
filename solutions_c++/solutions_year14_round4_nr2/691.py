#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;
int n, a[100010], w, ans, l, r, T, m, b[1010], c[1010], cnt;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("1.out", "w", stdout);
	a[0] = 2147483647;
	scanf("%d", &T);
	while (T--)
	{
		ans = 0;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) b[i] = c[i] = 0;
		for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
		l = 1, r = n;
		for (int i = 1; i <= n; i++)
		{
			m = 0;
			for (int j = l; j <= r; j++)
				if (a[m] > a[j]) m = j;
			if (m - l < r - m)
			{
				for (int j = m; j > l; j--) swap(a[j], a[j - 1]), ans++;
				l++;
			}
			else
			{
				for (int j = m; j < r; j++) swap(a[j], a[j + 1]), ans++;
				r--;
			}
		}
		printf("Case #%d: %d\n", ++w, ans);
 	}
	return 0;
}
