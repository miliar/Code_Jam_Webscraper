#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int N = 222;
int n, k;
double p[N];
double b[N];
double a[N];

double solve2()
{
	for (int i = 0; i <= k; i++)
		b[i] = 0;
	b[0] = 1;
	for (int i = 0; i < k; i++)
	{
		for (int j = i + 1; j > 0; j--)
			b[j] = b[j] * (1 - a[i]) + b[j - 1] * a[i];
		b[0] *= 1 - a[i];
	}
	return b[k / 2];
}

double solve()
{
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
		scanf("%lf", &p[i]);
	sort(p, p + n);
	double ans = 0;
	for (int l = 0; l <= k; l++)
	{
		int sz = 0;
		for (int i = 0; i < l; i++)
			a[sz++] = p[i];
		int r = n;
		while(sz < k)
			a[sz++] = p[--r];
		double res = solve2();
//		printf("%d : %.5lf\n", l, res);
		ans = max(ans, res);
	}
	return ans;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
		printf("Case #%d: %.13lf\n", i, solve());

	return 0;
}