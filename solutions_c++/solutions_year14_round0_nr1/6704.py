#include <cstdio>

int main(void) {
	int tests;
	scanf("%d", &tests);
	for (int i = 1; i <= tests; i++) {
		int t1[4][4], t2[4][4];
		int r1, r2;
		scanf("%d", &r1);
		r1--;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				scanf("%d", &t1[j][k]);
		scanf("%d", &r2);
		r2--;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				scanf("%d", &t2[j][k]);
		int ok = 0, n;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				if (t1[r1][j] == t2[r2][k]) {
					ok++;
					n = t1[r1][j];
				}
		printf("Case #%d: ", i);	
		if (ok == 0)
			printf("Volunteer cheated!\n");
		else if (ok == 1)
			printf("%d\n", n);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
