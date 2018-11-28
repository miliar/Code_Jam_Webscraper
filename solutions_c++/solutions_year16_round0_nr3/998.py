#include <cstdio>

typedef long long LL;

LL isprime(LL x) {
	for (LL i = 2; i * i <= x; ++i) {
		if (x % i == 0) {
			return i;
		}
	}
	return 0;
}

int n, m, ans;
int a[55];

void dfs(int x) {
	if (x == n - 1) {
		bool flag = true;
		for (int i = 2; i <= 10; ++i) {
			LL cur = 1, res = 0;
			for (int j = 0; j < n; ++j) {
				if (a[j] == 1) {
					res += cur;
				}
				cur *= i;
			}
			int tmp = isprime(res);
			if (tmp == 0) {
				flag = false;
				break;
			}
		}
		if (flag) {
			++ans;
			for (int i = n - 1; i >= 0; --i) {
				printf("%d", a[i]);
			}
			for (int i = n - 1; i >= 0; --i) {
				printf("%d", a[i]);
			}
			for (int i = 2; i <= 10; ++i) {
				LL cur = 1, res = 0;
				for (int j = 0; j < n; ++j) {
					if (a[j] == 1) {
						res += cur;
					}
					cur *= i;
				}
				int tmp = isprime(res);
				printf(" %d", tmp);
			}
			puts("");
		}
		return;
	}
	a[x] = 0;
	dfs(x + 1);
	if (ans == m) return;
	a[x] = 1;
	dfs(x + 1);
	if (ans == m) return;
}

int main() {
	freopen("1.out", "w", stdout);
	printf("Case #1:\n");
	scanf("%d%d", &n, &m);
	a[0] = 1;
	a[n - 1] = 1;
	dfs(1);
	return 0;
}

