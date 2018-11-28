#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int a[4][4], b[4][4];

void work() {
	int ra, rb;
	scanf("%d", &ra);
	ra--;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf("%d", &a[i][j]);
	scanf("%d", &rb);
	rb--;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf("%d", &b[i][j]);
	int ans = -1;
	for (int i = 0; i < 4; i++) {
		bool flag = false;
		for (int j = 0; j < 4; j++)
			if (a[ra][i] == b[rb][j]) {
				flag = true;
				break;
			}
		if (flag) {
			if (ans == -1)
				ans = a[ra][i];
			else {
				puts("Bad magician!");
				return;
			}
		}
	}
	if (ans == -1)
		puts("Volunteer cheated!");
	else
		printf("%d\n", ans);
}

int main() {
// freopen("a.in", "r", stdin);
// freopen("a.out", "w", stdout);
	int T, C = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++C);
		work();
	}
	return 0;
}
