#include <cstdio>
#include <set>

using namespace std;

const int MAXN = 100010;

multiset<int> S;

int n, m;

int main(void) {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
		scanf("%d%d", &n, &m); S.clear();
		for (int i = 1, x; i <= n; i++) scanf("%d", &x), S.insert(-x);
		int Ans = 0;
		for (multiset<int>::iterator it = S.begin(); it != S.end();) {
			int tmp = -*it - m;
			S.erase(it++);
			multiset<int>::iterator ot = S.lower_bound(tmp);
			if (ot != S.end()) {
				if (ot == it) it++;
				S.erase(ot);
			}
			Ans++;
		}
		printf("Case #%d: %d\n", _, Ans);
	}
	return 0;
}

