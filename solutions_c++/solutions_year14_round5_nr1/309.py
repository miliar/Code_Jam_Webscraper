#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 2010

int n, p, q, r, s;
int arr[MAXN];
long long acc[MAXN];

int main()
{
	int t, cas;
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++) {
		scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
		for (int i = 0; i < n; i++) {
			arr[i] = (1ll * i * p + q) % r + s;
			// printf("%d ", arr[Ki]);
		}
		// printf("\n");
		memset(acc, 0, sizeof acc);
		for (int i = 1; i <= n; i++)
			acc[i] = acc[i - 1] + arr[i - 1];
		int a, b;
		long long total = acc[n];
		double ret = 0.0;
		for (a = 0; a < n; a++) {
			for (b = a; b < n; b++) {
				long long tmp1 = acc[a] - acc[0];
				long long tmp2 = acc[b + 1] - acc[a];
				long long tmp3 = acc[n] - acc[b + 1];
				long long val = max(tmp1, max(tmp2, tmp3));
				// printf("a = %d b = %d tmp1 = %I64d tmp2 = %I64d tmp3 = %I64d val = %I64d\n", a, b, tmp1, tmp2, tmp3, val);
				double tmp = 1.0 * (total - val) / total;
				ret = max(tmp, ret);
			}
		}
		printf("Case #%d: %.10f\n", cas, ret);
	}
	return 0;
}
