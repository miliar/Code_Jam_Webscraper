//author: whd

#include <cstdio>

#define mp make_pair
#define pb push_back

typedef long long big;
using namespace std;
int main() {
	int cas, cass;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &cas);
	for (cass = 1; cass <= cas; cass++) {
		printf("Case #%d: ", cass);
		int i, n, s, x, ans = 0;
		scanf("%d", &n);
		scanf("%1d", &s);
		for (i = 1; i <= n; i++) {
			scanf("%1d", &x);
			if (i > s && x) {
				ans += i - s;
				s = i;
			}
			s += x;
		}
		printf("%d\n", ans);
	}
}
