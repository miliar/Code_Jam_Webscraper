#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>
#include <functional>
using namespace std;
int a[100001] = {0};
int candid(int n, int l)
{
	int now = 0;
	for (int i = 1; i <= n; i++)
		now += (a[i]-1) / l;
	return now;
}
int main()
{
	int T, tt;
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (tt = 1; tt <= T; tt++)
	{
		int n, r = 0;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &a[i]); 
			r = max(r, a[i]);
		}
		int best = 1000000;
		for (int l = 1; l <= r; l++)
		{
			int v = candid(n, l);
			if (l + v <= best) best = l + v;
		} 
		printf("Case #%d: %d\n", tt, best);
	}
	return 0;
}
