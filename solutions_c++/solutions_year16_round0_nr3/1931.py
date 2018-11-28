#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 10010
#define ll long long
using namespace std;

int T, n, j, tot, a[33], pri[N], ss[N], p[11];

void init() {
	for (int i = 2; i <= N - 10; i++) {
		if (!ss[i]) pri[++tot] = i;
		for (int j = i; i * j < N - 10; j++) ss[i] = 1;
	}
}

int work(int x) {
	p[x] = 0;
	for (int i = 1; i <= tot; i++) {
		int t = 0;
		for (int j = 1; j <= n; j++) t = (t * x + a[j]) % pri[i];
		if (!t) {
			p[x] = pri[i];
			return 1;
		}
	}
	return 0;
}

void check() {
	for (int i = 2; i <= 10; i++) if (!work(i)) return;
	j--;
	for (int i = 1; i <= n; i++) printf("%d", a[i]);
	for (int i = 2; i <= 10; i++) printf(" %d", p[i]);
	printf("\n");
}

void dfs(int x) {
	if (!j) return;
	if (x == 1) a[x] = 1, dfs(x + 1);
	else if (x == n) a[x] = 1, check();
	else {
		a[x] = 0;
		dfs(x + 1);
		a[x] = 1;
		dfs(x + 1);
	}
}

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	init();
	scanf("%d", &T);
	for (int k = 1; k <= T; k++) {
		printf("Case #%d:\n", k);
		scanf("%d %d", &n, &j);
		dfs(1);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}