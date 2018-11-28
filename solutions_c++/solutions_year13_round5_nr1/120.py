#include <cstdio>
#include <algorithm>
using namespace std;
long long a[38], b[38];
int main()
{
	freopen("Al.in", "r", stdin);
	freopen("Al.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++ cas)
	{
		long long B;
		int n;
		scanf("%lld%d", &B, &n);
		for (int i = 0; i < n; ++ i)
			scanf("%lld", &a[i]);
		for (int i = n; i < 37; ++ i)
			a[i] = 0;
		sort(a, a + 37);
		double res = 0;
		a[37] = b[37] = 10000000000000LL;
		for (int num = 1; num <= 37; ++ num)
		{
			long long tot = 0;
			for (int i = 0; i < num; ++ i)
			{
				tot += a[num - 1] - a[i];
				b[i] = a[num - 1];
			}
			for (int j = num; j < 37; ++ j)
				if (a[j] == a[num - 1])
				{
					++ tot;
					b[j] = a[num - 1] + 1;
				}
				else
					b[j] = a[j];
			if (tot > B)
			   break;
			for (int j = num + 1; j <= 37; ++ j)
			{
				int k = j;
				while (b[j - 1] == b[k - 1]) ++ j;
				-- j;
				long long mores = 0;
				for (int i = 0; i < k - 1; ++ i)
					mores += b[j - 1] - b[i] - 1;
				if (tot + mores > B)
				{
					for (int i = 0; i < k - 1; ++ i)
						b[i] += (B - tot) / (k - 1);
					tot += (B - tot) / (k - 1) * (k - 1);
					break;
				}
				tot += mores;
				for (int i = 0; i < j; ++ i)
					b[i] = b[j - 1] - 1;
			}
			double ans = 0;
			for (int i = 0; i < num; ++ i)
				ans += (double) (b[i] - a[i]) * 36 / num;
			ans -= tot;
			res = max(res, ans);
		}
		printf("Case #%d: %.10f\n", cas, res);
	}
	return 0;
}
