#include <cstdio>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

#define mp(a,b) make_pair(a, b)

int sz[10006];

void Solve() {
	int n, x;
	cin >> n >> x;
	for (int i = 0; i < n; ++i) {
		cin >> sz[i];
	}
	sort(sz, sz + n);
	int ret = 0, f = 0, s = n - 1;
	while (s >= f) {
		++ret;
		if (sz[s] + sz[f] <= x) {
			--s;
			++f;
		} else {
			--s;
		}
	}
	printf("%d\n", ret);
}

int main() {
	freopen("a_large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}