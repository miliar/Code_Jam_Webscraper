#include <cstdio>
#include <iostream>
#include <algorithm>

const int MAXN = 1000 + 10;

int a[MAXN];

int main()
{
	int T; 
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		int ans = 0;
		for (int i = 0; i < n; ++i)
		{
			int p = i;
			for (int j = p + 1; j < n; ++j)
				if (a[j] < a[p])
					p = j;
			if (p - i < n - 1 - p)
				ans += p - i;
			else ans += n - 1 - p;
			int x = a[p];
			for (int j = p; j > i; --j)
				a[j] = a[j - 1];
		}
		printf("Case #%d: %d\n", tt, ans);
	}

	return 0;
}
