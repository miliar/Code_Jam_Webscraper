#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

char s[1005];

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt)
	{
		int ans = 0, cur = 0, n;
		scanf("%d%s", &n, s);
		for (int i = 0; i <= n; ++i)
		{
			s[i] -= '0';
			if (s[i] && i > cur)
				ans += i - cur, cur = i;
			cur += s[i];
		}

		printf("Case #%d: %d\n", tt, ans);
	}

	return 0;
}