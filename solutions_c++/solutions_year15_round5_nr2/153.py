#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int INF = (int)1e6;
const int N = 1010;
int n, k;
int s[N];
int a[N], b[N];
int L[N], R[N];

bool check(int p, int d)
{
	int l = 0, r = 0;
	for (int i = 0; i < k; i++)
		if (R[i] - L[i] > d)
			return false;
	for (int i = 0; i < k; i++)
	{
		if (i == p) continue;
		int dl = L[p] - L[i];
		int dr = L[p] + d - R[i];
		if (dr < dl)
			return false;
		l += dl;
		r += dr;
	}
	int x = ((l - s[0]) / k) * k;
	l -= x * k;
	r -= x * k;
	while(l > s[0])
	{
		l -= k;
		r -= k;
	}
	while(l + k <= s[0])
	{
		l += k;
		r += k;
	}
	return s[0] <= r;
}

void solve()
{
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n - k + 1; i++)
		scanf("%d", &s[i]);
	for (int i = 0; i < n; i++)
		a[i] = 0;
	for (int i = k; i < n; i++)
		a[i] = a[i - k] + s[i - k + 1] - s[i - k];
	for (int i = 0; i < k; i++)
	{
		L[i] = INF;
		R[i] = -INF;
		for (int j = i; j < n; j += k)
		{
			L[i] = min(L[i], a[j]);
			R[i] = max(R[i], a[j]);
		}
	}
	int ans = INF;
	for (int i = 0; i < k; i++)
	{
		int l = -1;
		int r = INF;
		while(r - l > 1)
		{
			int m = (l + r) / 2;
			if (check(i, m))
				r = m;
			else
				l = m;
		}
		ans = min(ans, r);
	}
	printf("%d\n", ans);
	return;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}