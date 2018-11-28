#include <cstdio>
#include <algorithm>

using namespace std;

int T, n, a[29], b[29];
int tmp, ans;
int use[29];

bool gao(int k) {
	if (k == n) return true;
	bool flag = false;
	for (int i = 0; i < n; ++i) if (!use[i] && (a[b[k]] & 1 << i)) {
		flag = true;
		use[i] = true;
		if (!gao(k + 1)) return false;
		use[i] = false;
	}
	return flag;
}

bool check() {
	for (int i = 0; i < n; ++i) b[i] = i;
	do {
		for (int i = 0; i < n; ++i) use[i] = false;
		if (!gao(0)) return false;
	} while (next_permutation(b, b + n));
	return true;
}

void dfs(int x, int y) {
	if (y == n) ++x, y = 0;
	if (x == n) {
		if (ans > tmp) if (check()) ans = tmp;
		return;
	}
	dfs(x, y + 1);
	if (!(a[x] & 1 << y)) {
		++tmp;
		a[x] |= 1 << y;
		dfs(x, y + 1);
		a[x] ^= 1 << y;
		--tmp;
	}
}

int main() {
	scanf("%d", &T);
	for (int tT = 1; tT <= T; ++tT) {
		printf("Case #%d: ", tT);
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			a[i] = 0;
			for (int j = 0; j < n; ++j) {
				int x;
				scanf("%1d", &x);
				a[i] |= x << j;
			}
		}
		ans = 100000;
		tmp = 0;
		dfs(0, 0);
		printf("%d\n", ans);
	}
	return 0;
}
