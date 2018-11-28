#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f;
const double eps = 1e-8, pi = acos(-1.0);

const int maxn = 1001;
int tests, n, a[maxn], order[maxn], T[maxn];

bool cmp(int x, int y) {
	return a[x] < a[y];
}

int lowbit(int x) {
	return x & (-x);
}

int ask(int x) {
	int ret = 0;
	while (x > 0) {
		ret += T[x];
		x -= lowbit(x);
	}
	return ret;
}

void update(int x, int v) {
	while (x <= n) {
		T[x] += v;
		x += lowbit(x);
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &tests);
	for (int tt = 1; tt <= tests; ++tt) {
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i) {
			scanf("%d", &a[i]);
			order[i] = i;
		}
		sort(order + 1, order + 1 + n, cmp);
		int result = 0;
		memset(T, 0, sizeof(T));
		for (int i = 1; i <= n; ++i) {
			update(i, 1);
		}
		for (int i = 1; i <= n; ++i) {
			int w = order[i];
			int pred = ask(w - 1), succ;
			succ = n - i - pred;
			result += min(pred, succ);
			update(w, -1);
		}
		printf("Case #%d: %d\n", tt, result);
	}
	return 0;
}
