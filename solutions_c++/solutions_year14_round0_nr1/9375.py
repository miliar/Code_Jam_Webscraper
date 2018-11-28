#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <stdio.h>
#include <iostream>

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		int row1, row2;
		int mat1[4][4], mat2[4][4];
		row1 = row2 = 0;
		memset(mat1, 0, sizeof mat1);
		memset(mat2, 0, sizeof mat2);
		scanf("%d", &row1);
		row1 = row1 - 1;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				scanf("%d", &mat1[j][k]);
			}
		}
		scanf("%d", &row2);
		row2 = row2 - 1;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				scanf("%d", &mat2[j][k]);
			}
		}
		int count = 0; 
		int answer = 0;
		for (int s = 0; s < 4; s++) {
			for (int t = 0; t < 4; t++) {
				if (mat1[row1][s] == mat2[row2][t]) {
					count++;
					answer = mat1[row1][s];
				}
			}
		}
		if (count == 1) {
			printf("Case #%d: %d\n", i, answer);
		} 
		else if (count == 0) {
			printf("Case #%d: %s\n", i, "Volunteer cheated!");
		}
		else if (count > 1) {
			printf("Case #%d: %s\n", i, "Bad magician!");
		}
	}
	return 0;
}
