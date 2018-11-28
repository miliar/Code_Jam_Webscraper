#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1E3 + 10;

int n;
int a[MAXN];
int dfn[MAXN], len[MAXN];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		scanf("%d", &n);
		for (int i = 1; i <= n; ++i)
			scanf("%d", &a[i]), len[i] = 0;
		int ans = 0;
		for (int i = 1; i <= n; ++i){
			for (int j = 1; j <= n; ++j)
				dfn[j] = 0;

			int u = i, tot = 0;
			for (; dfn[u] == 0; u = a[u]){
				dfn[u] = ++tot;
			}
			len[u] = max(len[u], dfn[u]);
			ans = max(ans, tot + 1 - dfn[u]);
		}
		int cnt = 0;
		for (int i = 1; i <= n; ++i)
			for (int j = i + 1; j <= n; ++j)
				if (a[i] == j && a[j] == i)
					cnt += len[i] + len[j];
		ans = max(ans, cnt);
		printf("%d\n", ans);
	}
	return 0;
}
