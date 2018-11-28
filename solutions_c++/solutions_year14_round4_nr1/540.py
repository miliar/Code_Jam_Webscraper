#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 10001;

int a[MAXN], n, m;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t ++){
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i ++)
			scanf("%d", &a[i]);
		int ans = n;
		sort(a, a + n);
		int p = n - 1;
		for (int i = 0; i <= p; i ++){
			while (i < p && a[i] + a[p] > m)
				p --;
			if (i < p && a[i] + a[p] <= m)
				ans --, p --;
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}
