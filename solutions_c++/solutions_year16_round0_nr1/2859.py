#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
bool vis[11];

void factor(ll x) {
	while (x > 0) {
		vis[x % 10] = true;
		x /= 10;
	}
}

bool check() {
	for (int i = 0; i < 10; i ++) {
		if (!vis[i]) return false;
	}return true;
}

void solve(int tst) {
	int n;
	scanf("%d", &n);
	if (n == 0) {
		printf("Case #%d: INSOMNIA\n", tst);
		return;
	}
	memset(vis, 0, sizeof vis);
	for (int i = 1; ; i ++) {
		ll v = 1ll * i * n;
		factor(v);
		if (check()) {
			printf("Case #%d: %lld\n", tst, v);
			return;
		}
	}
	printf("Case #%d: INSOMNIA\n", tst);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++) {
		solve(i);
	}
	return 0;
}