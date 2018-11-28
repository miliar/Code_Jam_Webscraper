#include <cstdio>
#include <cstring>
#define MAXN (1 << 3)
#define MAXSTEPS (1 << 2)
using namespace std;

int a, b, c;

inline void solve() {
	scanf("%d%d%d", &a, &b, &c);

	int ans = 0;
	for (int i=0; i < a; ++i)
		for (int j=0; j < b; ++j) {
			if ((i & j) < c)
				ans ++;
		}

	printf("%d\n", ans);
}

int main() {
	int brt;
	scanf("%d", &brt);

	for (int test=0; test < brt; ++test) {
		printf("Case #%d: ", test+1);
		solve();
	}
	return 0;
}