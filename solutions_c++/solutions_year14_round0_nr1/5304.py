#include <cstdio>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		int r1, r2;
		int sq1[4][4], sq2[4][4];
		scanf("%d", &r1);
		r1--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &sq1[i][j]);
			}
		}
		scanf("%d", &r2);
		r2--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &sq2[i][j]);
			}
		}
		int ans = -1;
		bool badmagician = false;
		for (int i = 0; i < 4; i++) {
			int num = sq1[r1][i];
			for (int j = 0; j < 4; j++) {
				if (num == sq2[r2][j]) {
					if (ans != (-1)) {
						badmagician = true;
						goto fin;
					}
					ans = num;
				}
			}
		}
		fin:
		printf("Case #%d: ", tc+1);
		if (ans == (-1)) {
			printf("Volunteer cheated!\n");
		}
		else if (badmagician) {
			printf("Bad magician!\n");
		}
		else {
			printf("%d\n", ans);
		}
	}
}