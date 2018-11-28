#include <cstdio>
#include <set>
#include <algorithm>
using namespace std;

int solve() {
	int N, X;
	multiset<int> s;
	scanf("%d%d", &N, &X);
	for (int i = 0; i < N; i += 1) {
		int a;
		scanf("%d", &a);
		s.insert(a);
	}
	int ans = 0;
	while (!s.empty()) {
		multiset<int>::iterator it = --s.end(), jt;
		jt = s.upper_bound(X - *it);
		if (jt != s.begin()) {
			--jt;
			if (jt != it) {
				s.erase(jt);
				s.erase(it);
			} else if (jt == s.begin()) {
				s.erase(it);
			} else {
				--jt;
				s.erase(jt);
				s.erase(it);
			}
		} else {
			s.erase(it);
		}
		ans += 1;
	}
	return ans;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i += 1)
		printf("Case #%d: %d\n", i, solve());
}

