#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int ttt;
	scanf("%d", &ttt);
	for (int ca = 1; ca <= ttt; ca++)
	{
		int n;
		scanf("%d", &n);
		vector<int> a;
		for (int i = 0; i <= n; i++)
		{
			int x;
			scanf("%1d", &x);
			a.push_back(x);
		}
		int sum = 0;
		int ans = 0;
		for (int i = 0; i <= n; sum += a[i++])
			if (sum < i)
			{
				ans += i - sum;
				sum = i;
			}
		printf("Case #%d: %d\n", ca, ans);
	}
	return 0;
}