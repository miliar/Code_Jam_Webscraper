#include <stdio.h>

int* match(int *str1, int *str2) {
	int r[2] = {0, 0};
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if(str1[i] == str2[j]) {
				r[0] = str1[i];
				r[1]++;
			}
		}
	}
	return r;
}

int main() {
	freopen ("A-small-attempt1.in","r",stdin);
	freopen("A-small.out", "w", stdout);
	int c;
	scanf("%d", &c);
	for (int i = 0; i < c; i++) {
		int row1;
		int str1[4][4];
		scanf("%d", &row1);
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				scanf("%d", &str1[j][k]);
			}
		}
		int row2;
		int str2[4][4];
		scanf("%d", &row2);
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				scanf("%d", &str2[j][k]);
			}
		}
		if (match(str1[row1 - 1], str2[row2 - 1])[1] == 1) {
			printf("Case #%d: %d\n",i + 1, match(str1[row1 - 1], str2[row2 - 1])[0]);
		} else if (match(str1[row1 - 1], str2[row2 - 1])[1] == 0) {
			printf("Case #%d: Volunteer cheated!\n",i + 1);
		} else {
			printf("Case #%d: Bad magician!\n",i + 1);
		}
	}
	fclose(stdout);
	return 0;
}