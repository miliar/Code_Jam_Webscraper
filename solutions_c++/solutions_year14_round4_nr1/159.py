#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;



const int maxn = 1e4 + 100;
int a[maxn];
bool used[maxn];

void solve()
{
	int n, sz;
	scanf("%d%d", &n, &sz);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i] );
	sort(a, a + n);
	int ans = 0;
	int l = 0, r = n - 1;
	while (r >= l)
	{
		if (a[l] + a[r] > sz)
		{
			r--;
			ans++;
			continue;
		}
		ans++;
		l++;
		r--;
	}
	printf("%d", ans);
}


int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

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