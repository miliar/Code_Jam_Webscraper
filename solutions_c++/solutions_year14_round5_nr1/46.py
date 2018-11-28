#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;



const int maxn = 1e6 + 100;
const long long INF = 1e18;

int dev[maxn];
long long prefsum[maxn];
long long suffsum[maxn];

void solve()
{
	int n, p, q, r, s;
	scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
	for (int i = 0; i < n; i++)
		dev[i] = ( (i * 1LL * p + q) % (long long) r + s);
	for (int i = 0; i < n; i++)
	{
		prefsum[i] = dev[i];
		if (i > 0)
			prefsum[i] += prefsum[i - 1];
	}
	for (int i = n - 1; i >= 0; i--)
	{
		suffsum[i] = dev[i];
		if (i < n - 1)
			suffsum[i] += suffsum[i + 1];
	}

	if (n < 3)
	{
		if (n == 1)
			printf("0.0000000000");
		else if (n == 2)
		{
			printf("%.11lf", min(dev[0], dev[1] ) / (double) (dev[0] + dev[1] ) );
		}
		return ;
	}

	long long ans = INF;
	int m = 0;
	for (int i = 1; i < n - 1; i++)
	{
		long long cura = prefsum[i - 1];

		m = max(m, i + 1);
		long long mid = prefsum[m - 1] - cura;

		while (m < n - 1 && mid + dev[m] <= suffsum[m] )
		{
			mid += dev[m];
			m++;
		}
		{
			long long a = cura;
			long long b = mid;
			long long c = suffsum[m];
			long long cur = max(a, max(b, c) );
			ans = min(ans,  cur);
		}
		if (m < n - 1)
		{
			mid += dev[m];
			m++;

			long long a = cura;
			long long b = mid;
			long long c = suffsum[m];
			long long cur = max(a, max(b, c) );
			ans = min(ans,  cur);

			m--;
		}
	}
	printf("%.11lf", 1. - ans / (double) prefsum[n - 1] );
}



int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		fprintf(stderr, "Case #%d: ", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
		fprintf(stderr, "OK\n");
	}


	return 0;
}