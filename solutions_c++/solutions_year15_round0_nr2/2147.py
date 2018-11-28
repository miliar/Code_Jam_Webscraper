#include <bits/stdc++.h>

using namespace std;

int a[11111];

int solve()
{
	int n = 0;
	scanf("%d", &n);
	int ma = 0;
	for (int i = 1; i <= n; i++)
	{
		scanf("%d", &a[i]);
		ma = max(ma, a[i]);
	}
	int ans = 100000;
	for (int i = 1; i <= ma; i++)
	{
		int cur = i;
		for (int j = 1; j <= n; j++) if (a[j] > i)
		{
			int l = a[j] / i;
			int y = (a[j] + l - 1) / l;
			if (y > i)
				l++;
			cur += l - 1;
		}
		ans = min(ans, cur);
	}
	return ans;
}

int main()
{
	int test = 0;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		printf("Case #%d: %d\n", tt, solve());
	}
	return 0;
}