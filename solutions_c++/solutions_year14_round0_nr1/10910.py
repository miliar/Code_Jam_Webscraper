#include <cstdio>

int main() {
	int tests; scanf("%d", &tests);
	for (int t = 1; t <= tests; t++) {
		int ans1; scanf("%d", &ans1); ans1--;
		int m1[4][4];
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++)
			scanf("%d", &m1[i][j]);

		int ans2; scanf("%d", &ans2); ans2--;
		int m2[4][4];
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++)
			scanf("%d", &m2[i][j]);

		int cnt = 0, val = 0;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++)
			if (m1[ans1][i] == m2[ans2][j])
				cnt++, val = m1[ans1][i];

		if (cnt == 0)
			printf("Case #%d: Volunteer cheated!\n", t);
		else if (cnt > 1)
			printf("Case #%d: Bad magician!\n", t);
		else
			printf("Case #%d: %d\n", t, val);
	}

	return 0;
}