#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;


const int maxn = 1e3 + 100;
int a[maxn];


void solve()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i] );
	int ans = 0;
	for (int i = 0; i < n; i++)
	{
		int mn = a[0];
		int mid = 0;
		for (int j = 1; j < n - i; j++)
			if (a[j] < mn)
			{
				mid = j;
				mn = a[j];
			}
		ans += min(mid, n - i - mid - 1);
		for (int j = mid; j < n - i - 1; j++)
			a[j] = a[j + 1];
	}
	printf("%d", ans);
}


int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		fprintf(stderr, "Case #%d: ", i);
		solve();
		printf("\n");
		fprintf(stderr, "OK\n");
	}


	return 0;
}
