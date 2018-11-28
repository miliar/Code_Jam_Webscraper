#include <cstdio>
#include <cstring>

int cnt[22];

int main() {
	int T, ans, i, j, a, r;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		memset(cnt, 0, sizeof(cnt));
		scanf("%d", &r);
		for (i = 1; i < r; i++) scanf("%*d%*d%*d%*d");
		for (j = 0; j < 4; j++) {
			scanf("%d", &a);
			cnt[a]++;
		}
		for (; i < 4; i++) scanf("%*d%*d%*d%*d");
		ans = -1;
		scanf("%d", &r);
		for (i = 1; i < r; i++) scanf("%*d%*d%*d%*d");
		for (j = 0; j < 4; j++) {
			scanf("%d", &a);
			if (cnt[a]) {
				if (ans == -1) ans = a;
				else ans = -2;
			}
		}
		for (; i < 4; i++) scanf("%*d%*d%*d%*d");
		switch (ans) {
			case -1:
				puts("Volunteer cheated!");
				break;
			case -2:
				puts("Bad magician!");
				break;
			default:
				printf("%d\n", ans);
				break;
		}
	}
	return 0;
}
