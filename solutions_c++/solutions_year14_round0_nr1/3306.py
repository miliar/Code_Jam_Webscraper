#include <cstdio>

//[x][y]
int grid[5][5];

int main() {
	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++) {
		int r1, r2;
		scanf("%d", &r1);

		for (int j = 1; j <= 4; j++)
			for (int k = 1; k <= 4; k++)
				scanf("%d", &grid[k][j]);

		bool nums[17] = {false};
		for (int j = 1; j <= 4; j++)
			nums[grid[j][r1]] = true;

		scanf("%d", &r2);
		for (int j = 1; j <= 4; j++)
			for (int k = 1; k <= 4; k++)
				scanf("%d", &grid[k][j]);

		int right = 0;
		int num = -1;
		for (int j = 1; j <= 4; j++)
			if (nums[grid[j][r2]]) {
				right++;
				num = grid[j][r2];
			}

		printf("Case #%d: ", i);
		if (right == 0) printf("Volunteer cheated!");
		else if (right == 1) printf("%d", num);
		else printf("Bad magician!");
		printf("\n");
	}
}