#include <bits/stdc++.h>

using namespace std;

const int maxn = 1000 + 10;

int a[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int cas = 0;
	while (T--)
	{
		int d;
		scanf("%d", &d);
		for (int i = 0; i < d; ++i)
		{
			scanf("%d", &a[i]);
		}
		sort(a, a + d);
		int k = a[d - 1];
		int mi = k;
		for (int i = 1; i < k; ++i)
		{
			int sum = i;
			for (int j = d - 1; j >= 0; --j)
			{
				if (a[j] > i)
				{
					sum += (int)ceil(1.0 * a[j] / i) - 1;
				}
				else
				{
					break;
				}
			}
			mi = min(mi, sum);
		}
		printf("Case #%d: %d\n", ++cas, mi);
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}