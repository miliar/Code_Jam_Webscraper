#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int a[1005];

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt)
	{
		int n = 0;
		cin >> n;
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		int ans = 100500100;
		for (int q = 1; q < 1005; ++q)
		{
			int x = 0;
			for (int i = 0; i < n; ++i)
				x += (a[i] - 1) / q;
			ans = min(ans, q + x);
		}

		printf("Case #%d: %d\n", tt, ans);
	}

	return 0;
}