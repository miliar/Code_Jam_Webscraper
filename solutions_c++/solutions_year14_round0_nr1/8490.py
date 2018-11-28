#include <cstdio>
int main() {
	int testnum, l, v[4], V[4];
	scanf("%d", &testnum);
	for (int test = 1;test <= testnum;test++) {
		scanf("%d", &l);
		for (int i = 1;i <= 4;i++) {
			if (i == l) {
				scanf("%d%d%d%d", &v[0], &v[1], &v[2], &v[3]);
			} else {
				scanf("%*d%*d%*d%*d");
			}
		}
		scanf("%d", &l);
		for (int i = 1;i <= 4;i++) {
			if (i == l) {
				scanf("%d%d%d%d", &V[0], &V[1], &V[2], &V[3]);
			} else {
				scanf("%*d%*d%*d%*d");
			}
		}
		int cnt = 0, ans = -1;
		for (int i = 0;i < 4;i++) {
			for (int j = 0;j < 4;j++) {
				if (v[i] == V[j]) {
					ans = v[i];
					cnt++;
				}
			}
		}
		printf("Case #%d: ", test);
		if (cnt == 1)
			printf("%d\n", ans);
		else if (cnt > 1)
			puts("Bad magician!");
		else
			puts("Volunteer cheated!");
	}
	return 0;
}
