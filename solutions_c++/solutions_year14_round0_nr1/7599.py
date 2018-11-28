#include <cstdio>

int main()
{
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; i++) {
		int row;
		int num[4][4];
		int appeared[16] = {0};
		for (int j = 0; j < 2; j++) {
			scanf ("%d", &row);
			for (int r = 0; r < 4; r++)
				for (int c = 0; c < 4; c++)
					scanf ("%d", &num[r][c]);
			for (int c = 0; c < 4; c++)
				appeared[num[row-1][c] - 1]++;
		}
		char flag = 0;
		int pos = 0;
		for (int j = 0; j < 16; j++) {
			if (appeared[j] == 2) {
				if (flag == 1) {
					printf ("Case #%d: Bad magician!\n", i+1);
					flag = -1;
					break;
				}
				else flag = 1, pos = j+1;
			}
		}
		if (flag == -1) continue;
		else if (flag == 0) printf ("Case #%d: Volunteer cheated!\n", i+1);
		else if (flag == 1) printf ("Case #%d: %d\n", i+1, pos);
	}
}
