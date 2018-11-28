#include <stdio.h>

int main() {
	int T;
	int L[4], R[4], D[2];
	scanf("%d", &T);
	char c;
	scanf("%c", &c);
	for (int i = 0; i < T; i++) {
		for (int j = 0; j < 4; j++) {
			L[j] = 0;
			R[j] = 0;
		}
		D[0] = 0; D[1] = 0;	
		int flag = 0;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				scanf("%c", &c);
				int t = 0;
				if (c == '.')
					flag = 1;
				if (c == 'O')
					t = 1;
				if (c == 'X')
					t = -1;
				if (c == 'T')
					t = 100;
				L[j] += t;
				R[k] += t;
				if (j == k)
					D[0] += t;
				if (j == 3 - k)
					D[1] += t;
			}
			scanf("%c", &c);
		}
		int flag2 = 0;
		for (int j = 0; j < 4; j++) {
			if (L[j] == 4 || R[j] == 4 || D[j % 2] == 4 || L[j] == 103 || R[j] == 103 || D[j % 2] == 103) {
				if (!flag2)
					printf("\nCase #%d: O won", i + 1);
				flag2 = 1;
			}
			else if (L[j] == -4 || R[j] == -4 || D[j % 2] == -4 || L[j] == 97 || R[j] == 97 || D[j % 2] == 97) {
				if (!flag2)
					printf("\nCase #%d: X won", i + 1);
				flag2 = 1;
			}
		}
		if (!flag2) {
			if (flag)
				printf("\nCase #%d: Game has not completed", i + 1);
			else
				printf("\nCase #%d: Draw", i + 1);
		}
		scanf("%c", &c);
	}
	return 0;
}
