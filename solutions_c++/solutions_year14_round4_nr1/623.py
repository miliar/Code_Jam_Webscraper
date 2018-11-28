#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 10000 + 10;

int a[MAXN];

int main()
{
	int T; 
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		int n, x;
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		sort(a, a + n);
		int ans = 0, i = n - 1, j = 0;
		for (; i > j; --i)
		{
			++ans;
			if (a[i] + a[j] <= x)
				++j;
		}
		if (i == j)
			++ans;
		printf("Case #%d: %d\n", tt, ans);
	}

	return 0;
}
