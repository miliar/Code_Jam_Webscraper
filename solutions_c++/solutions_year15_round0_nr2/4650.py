#include <cstdio>
using namespace std;

const int N = 1000 + 100, INF = 1000000000;
int a[N], n;

int dfs(int p, int m, int s)
{
	if(p > n) return m + s;

	int ans = INF;
	for(int i = 1; i <= a[p]; ++i) {
		int x = (a[p] + i - 1) / i;
		int y = dfs(p + 1, x > m ? x : m, s + i - 1);
		if(ans > y) ans = y;
	}
	return ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ++ca) {
		scanf("%d", &n);
		for(int i = 1; i <= n; ++i)
			scanf("%d", &a[i]);
		printf("Case #%d: %d\n", ca, dfs(1, 0, 0));
	}
}