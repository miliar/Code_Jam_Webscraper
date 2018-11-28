#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int nTest;
int first_row, second_row, ret;
int grid[4][4], gone[16];

int main() {

	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);

	scanf("%d", &nTest);
	for(int test = 1; test <= nTest; test++) {
		int match = 0;
		memset(gone, 0, sizeof gone);

		scanf("%d", &first_row);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++) {
				scanf("%d", &grid[i][j]);
				if (i+1 == first_row)
					gone[grid[i][j]-1] = 1;
			}
		scanf("%d", &second_row);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++) {
				scanf("%d", &grid[i][j]);
				if (i+1 == second_row) 
					if (gone[grid[i][j]-1]) {
						ret = grid[i][j];
						match++;
					}
			}

		if (match == 1) printf("Case #%d: %d\n", test, ret);
		else printf("Case #%d: %s\n", test, !match ? "Volunteer cheated!" : "Bad magician!");
	}

	return 0;
}