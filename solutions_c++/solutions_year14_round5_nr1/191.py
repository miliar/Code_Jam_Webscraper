#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1000010;

long long arr[N], sum[N];

int mid (int s, int n)
{
	int l = s, r = n - 1;
	if (arr[s] > sum[n] - sum[s]) return s;
	else
	{
		while (r - l > 1)
		{
			int m = (l + r) >> 1;
			if (sum[m] - sum[s - 1] > sum[n] - sum[m]) // [s, m] : [m + 1, n]
				r = m;
			else l = m;
		}
		return r; 
	}
}

int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int kase = 1; kase <= T; ++kase)
	{
		int n, p, q, r, s; scanf("%d %d %d %d %d", &n, &p, &q, &r, &s);
		for (int i = 1; i <= n; i++) arr[i] = ((long long)(i - 1) * p + q) % r + s;
		sum[0] = 0;
		for (int i = 1; i <= n; i++) sum[i] = sum[i - 1] + arr[i];
		
		long long ans = sum[n];
		for (int s = 1; s <= n; s++)
		{
			int tt = mid(s, n);
			ans = min(ans, max(sum[s - 1], max(sum[tt] - sum[s - 1], sum[n] - sum[tt]))); // [1, s - 1], [s, tt], [tt + 1, n]
			if (tt - 1 >= s)
				ans = min(ans, max(sum[s - 1], max(sum[tt - 1] - sum[s - 1], sum[n] - sum[tt - 1]))); // [1, s - 1], [s, tt - 1], [tt, n]
		}
		
		printf("Case #%d: %.10f\n", kase, (double)(sum[n] - ans) / sum[n]);
	}
	fclose(stdin), fclose(stdout);
	return 0;
}
