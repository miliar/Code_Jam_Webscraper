#include <cstdio>

int main() {
	int cases;
	scanf("%d", &cases);

	for (int z = 0; z < cases; z++) {
		int row1, row2;
		int board1[4][4];
		int board2[4][4];

		scanf("%d", &row1);
		for (int r = 0; r < 4; r++)
			for (int c = 0; c < 4; c++)
				scanf("%d", &board1[r][c]);
		
		scanf("%d", &row2);
		for (int r = 0; r < 4; r++)
			for (int c = 0; c < 4; c++)
				scanf("%d", &board2[r][c]);

		row1--;
		row2--;

		int numCounts[16] = { 0 };
		for (int c = 0; c < 4; c++) {
			numCounts[ board1[row1][c] - 1 ]++;
			numCounts[ board2[row2][c] - 1 ]++;
		}
		
		int num = -1;
		bool bad = false;
		for (int i = 0; i < 16 && !bad; i++) {
			if (numCounts[i] > 1 && num == -1)
				num = i+1;
			else if (numCounts[i] > 1)
				bad = true;
		}

		printf("Case #%d: ", z+1);
		if (bad)
			printf("Bad magician!\n");
		else if (num == -1)
			printf("Volunteer cheated!\n");
		else
			printf("%d\n", num);
	}

	return 0;
}