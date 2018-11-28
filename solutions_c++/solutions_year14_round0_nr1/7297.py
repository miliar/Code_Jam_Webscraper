#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>

int T, a1, a2, m[16], x[4], s[4], l;

int main(void) {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		memset(m, 0, sizeof(m));
		scanf("%d", &a1);
		for (int i = 1; i <= 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &x[j]);
				if (i == a1) {
					m[x[j] - 1]++;
				}
			}
		}
		scanf("%d", &a2);
		for (int i = 1; i <= 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &x[j]);
				if (i == a2) {
					m[x[j] - 1]++;
				}
			}
		}
		l = 0;
		for (int k = 0; k < 16; k++) {
			if (m[k] == 2)
				s[l++] = k;
		}
		printf("Case #%d: ", t);
		if (l == 0) printf("Volunteer cheated!\n");
		else if (l == 1) printf("%d\n", s[0] + 1);
		else printf("Bad magician!\n");
	}

	return 0;
}