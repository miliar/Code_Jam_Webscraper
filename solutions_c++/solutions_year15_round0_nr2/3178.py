#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[1002], c[1002];
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, t = 0, n;
	cin >> T;
	while (T--)
	{
		cin >> n;
		memset(c, 0, sizeof(c));
		for (int i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		int ans = 1000;
		for (int i = 1; i <= 1000; i++)
		{
			int now = i;
			for(int j=1;j<=n;j++)
				if (a[j] > i) now += (a[j] - 1) / i;
			ans = min(ans, now);
		}
		cout << "Case #" << ++t << ": ";
		cout << ans << endl;
	}
}