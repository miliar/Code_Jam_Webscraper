#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t, n, a[10000];

int main()
{
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		int ans = 0;
		for (int k = n; k >= 1; k--)
		{
			int mn = 1;
			for (int i = 2; i <= k; i++)
				if (a[mn] > a[i]) mn = i;
			ans += min(mn - 1, k - mn);
			for (int i = mn; i < k; i++)
				a[i] = a[i + 1];
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
