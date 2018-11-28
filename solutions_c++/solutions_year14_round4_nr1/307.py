#include <cstdio>
#include <set>

using namespace std;

int main() {
	freopen("src/out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		int n, m;
		scanf("%d%d", &n, &m);
		multiset<int> s;
		for (int i = 0; i < n; i++) {
			int a;
			scanf("%d", &a);
			s.insert(a);
		}
		int ans = 0;
		while (s.size()) {
			int a = *s.begin();
			s.erase(s.begin());
			if (s.size()) {
				auto it = s.upper_bound(m - a);
				if (it != s.begin()) {
					s.erase(--it);
				}
			}
			ans++;
		}
		printf("%d\n", ans);
	}
}
