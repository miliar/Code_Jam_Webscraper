#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int t, n;
long long a;
long long ar[110];
int res[110];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		scanf("%lld%d", &a, &n);
		for (int i = 1; i <= n; i++)
		{
			scanf("%lld", &ar[i]);
		}
		if (a == 1)
		{
			printf("Case #%d: %d\n", q + 1, n);
			continue;
		}
		sort(ar + 1, ar + n + 1);
		res[0] = 0;
		int ans = n;
		for (int i = 1; i <= n; i++)
		{
			res[i] = res[i - 1];
			while (a <= ar[i])
			{
				a = a * 2 - 1;
				res[i]++;
			}
			a += ar[i];
			ans = min(ans, res[i] + n - i);
		}
		printf("Case #%d: %d\n", q + 1, ans);
	}
	return 0;
}