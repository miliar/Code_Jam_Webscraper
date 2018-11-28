#include <cstdio>
#include <cstdlib>
#include <cstring>

int T, R, k, cnt[20];

void doit() {
	scanf("%d", &R);
	for (int r = 1; r <= 4; ++r) {
		for (int c = 1; c <= 4; ++c) {
			scanf("%d", &k);
			if (r == R) {
				cnt[k]++;
			}
		}
	}
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		memset(cnt, 0, sizeof(cnt));
		doit(); doit();
		int ans = 0;
		for (int i = 1; i <= 16; ++i) {
			if (cnt[i] == 2 && ans == 0) {
				ans = i;
			} else if (cnt[i] == 2 && ans != 0) {
				ans = -1;
			}
		}
		printf("Case #%d: ", tc);
		if (ans == 0) puts("Volunteer cheated!");
		else if (ans == -1) puts("Bad magician!");
		else printf("%d\n", ans);
	}
	return 0;
}