#include <cstdio>

#define LOCAL_DEBUG

using namespace std;

int R1, R2;
int A1[10][10], A2[10][10];

void solve() {
	int ans = -1, cnt = 0;
	for (int i = 0; i < 4; i++) {
		int num = A1[R1-1][i];
		for (int j = 0; j < 4; j++) {
			if (num == A2[R2-1][j]) {
				cnt++;
				ans = num;
			}
		}
	}
	if (cnt == 1) printf("%d\n", ans);
	else if (cnt == 0) puts("Volunteer cheated!");
	else puts("Bad magician!");
}

int main() {
#ifdef LOCAL_DEBUG
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
#endif
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &R1);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &A1[i][j]);
		scanf("%d", &R2);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &A2[i][j]);
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}