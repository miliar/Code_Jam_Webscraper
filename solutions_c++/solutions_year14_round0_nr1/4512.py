#include <cstdio>
#include <cstring>
#define MAXN (1 << 3)
#define MAXSTEPS (1 << 2)
using namespace std;

const int n = 4;
const int totalSteps = 2;
int row[MAXSTEPS];
int a[MAXN][MAXN];

int amount[MAXN*MAXN];

inline void solve() {
	memset(amount, 0, sizeof(amount));
	for (int step=0; step < totalSteps; ++step) {
		scanf("%d", &row[step]);
		row[step] --;
		for (int i=0; i < n; ++i) {
			for (int j=0; j < n; ++j) {
				scanf("%d", &a[i][j]);
			}
		}
		for (int i=0; i < n; ++i)
			amount[a[row[step]][i]] ++;
	}

	int ans = -1;
	for (int i=1; i <= n*n; ++i) {
		if (amount[i] == totalSteps) {
			if (ans != -1) {
				puts("Bad magician!");
				return;
			}
			ans = i;
		}
	}

	if (ans == -1) puts("Volunteer cheated!");
	else printf("%d\n", ans);
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