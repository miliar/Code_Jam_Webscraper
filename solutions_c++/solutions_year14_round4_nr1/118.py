#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f;
const double eps = 1e-8, pi = acos(-1.0);

const int maxn = 10001;
int tests, X, n, a[maxn];

int cal() {
	multiset<int> s;
	for (int i = 1; i <= n; ++i) {
		s.insert(a[i]);
	}
	int ret = 0;
	while (!s.empty()) {
		int t = *(--s.end());
		s.erase(--s.end());
		set<int>::iterator it = s.upper_bound(X - t);
		if (it != s.begin()) {
			--it;
			s.erase(it);
		}
		++ret;
	}
	return ret;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &tests);
	for (int tt = 1; tt <= tests; ++tt) {
		scanf("%d%d", &n, &X);
		for (int i = 1; i <= n; ++i) {
			scanf("%d", a + i);
		}
		sort(a + 1, a + 1 + n);
		printf("Case #%d: %d\n", tt, cal());
	}
	return 0;
}

