#include <stdio.h>
int main() {
	int t, tc;
	for(scanf("%d", &t), tc = 1; tc <= t; tc++) {
		int r, c[4][4], r2, c2[4][4], ans[4]={0};
		scanf("%d", &r);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++) scanf("%d", &c[i][j]);
		scanf("%d", &r2);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++) scanf("%d", &c2[i][j]);
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(c[r-1][i] == c2[r2-1][j]) {
					ans[i] = 1;
					break;
				}
			}
		}
		if(ans[0]+ans[1]+ans[2]+ans[3] < 1)
			printf("Case #%d: Volunteer cheated!\n", tc);
		else if(ans[0]+ans[1]+ans[2]+ans[3] > 1)
			printf("Case #%d: Bad magician!\n", tc);
		else {
			for(int i = 0; i < 4; i++) {
				if(ans[i]) {
					printf("Case #%d: %d\n", tc, c[r-1][i]);
					break;
				}
			}
		}
	}
	return 0;
}
