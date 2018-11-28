#include <bits/stdc++.h>
using namespace std;

int n;
long long a[1000100];

int main()
{
	freopen("a-large.in", "r", stdin); 
	freopen("a-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int noTest = 1; noTest <= test; noTest++)
	{
		int p, q, r, s;
		cin >> n >> p >> q >> r >> s;
		for (int i = 1; i <= n; i++)
		{
			a[i] = ((i - 1LL) * p + q) % r + s;
			a[i] += a[i - 1];
		}
		
		long long ans = a[n];
		for (int i = 1; i < n; i++) ans = min(ans, max(a[i], a[n] - a[i]));
		
		for (int i = 1, j = 0; i < n; i++)
		{
			while (j < i && a[j + 1] <= a[i] - a[j + 1]) j++;
			ans = min(ans, max(a[n] - a[i], max(a[i] - a[j], a[j])));
			if (j < i) ans = min(ans, max(a[n] - a[i], max(a[i] - a[j + 1], a[j + 1])));
		}
		
		printf("Case #%d: %.12lf\n", noTest, 1.0 * (a[n] - ans) / a[n]);
	}
}
