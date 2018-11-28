#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int N = 10100;
int n;
int s[N];
int a[N];
int ans[N];
int m;

void solve()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &s[i]);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	m = 0;
	while(a[0] > 1)
	{
		ans[m++] = 0;
		for (int i = 0; i < n; i++)
			a[i] /= 2;
	}
	while(true)
	{
		int k = 1;
		while(k < n && a[k] == 0) k++;
		if (k == n) break;
		int x = s[k];
		ans[m++] = x;
		for (int i = 0; i < n; i++)
		{
			if (a[i] == 0) continue;
			while(k < n && s[k] - s[i] < x) k++;
			if (k == n || s[k] - s[i] != x) throw;
			if (a[k] < a[i]) throw;
			a[k] -= a[i];
		}
	}
	for (int i = 0; i < m; i++)
		printf("%d ", ans[i]);
	printf("\n");
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