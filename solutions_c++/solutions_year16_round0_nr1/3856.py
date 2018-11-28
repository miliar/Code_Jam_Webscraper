#include<cstdio>
#include <cstring>
typedef long long LL;
int T;
bool vis[10];
void init() {
	memset (vis, 0, sizeof vis);
}
void fill(LL x, bool* vis) {
	while(x) {
		vis[x % 10] = true;
		x /= 10;
	}
}
bool full(bool *vis) {
	for (int i = 0; i < 10; i ++)
		if (vis[i] == false)
			return false;
	return true;
}
void solve(LL n) {
	if (n == 0) {
		printf("INSOMNIA\n");
		return ;
	}
	int i;
	for (i = 1; ; i ++) {
		fill(n * i, vis);
		if (full(vis)) break;
	}
	printf("%I64d\n", n * i);
}
int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1, n; i <= T; i ++) {
		scanf("%d", &n);
		printf("Case #%d: ", i);
		init();
		solve(n);
	}
	return 0;
}
