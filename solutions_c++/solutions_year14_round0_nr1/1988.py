//source here
#include <iostream>
#include <cstdio>
#include <math.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	int case_id = 1;

	while (T--) {
		int row1;
		cin >> row1;
		int sqr1[4][4];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> sqr1[i][j];

		int row2;
		cin >> row2;
		int sqr2[4][4];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> sqr2[i][j];

		int count = 0;
		int ans = -1;
		for (int i = 0; i < 4; i++) {
			// is sqr1[row1][i] exists in sqr2[row2][j].
			for (int j = 0; j < 4; j++) {
				if (sqr1[row1 - 1][i] == sqr2[row2 - 1][j]) {
					ans = sqr1[row1 - 1][i];
					count++;
					break;
					
				}
			}
		}

		if (count == 0) {
			printf("Case #%d: Volunteer cheated!\n", case_id++);
		}
		else if (count == 1) {
			printf("Case #%d: %d\n", case_id++, ans);
		}
		else {
			printf("Case #%d: Bad magician!\n", case_id++);
		}
	}
	return 0;
}