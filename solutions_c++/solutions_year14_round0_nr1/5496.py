#include <cstdio>

int main(void) {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++) {
		int r1, r2;
		scanf("%d", &r1);
	
		int g1[4][4], g2[4][4];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++)
				scanf("%d", &g1[i][j]);
		}
		
		scanf("%d", &r2);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++)
				scanf("%d", &g2[i][j]);
		}
		
		r1--;r2--;
		int badtoed = -1;
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (g1[r1][i] != g2[r2][j]) continue;
				if (badtoed != -1) {
					badtoed = -2;
					break;
				} else badtoed = g1[r1][i];
			}
			
			if (badtoed == -2) break;
		}
		
		if (badtoed == -2) printf("Case #%d: Bad magician!\n", t);
		else if (badtoed == -1) printf("Case #%d: Volunteer cheated!\n", t);
		else printf("Case #%d: %d\n", t, badtoed);
	}
}