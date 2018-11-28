#include <cstdio>

using namespace std;

int main() {

	int testcases;
	scanf("%d", &testcases);

	for (int tc=1; tc<testcases+1; tc++) {
		printf("Case #%d: ", tc);

		int firstAns, secondAns;
		int cards1[4][4];
		int cards2[4][4];

		scanf("%d", &firstAns);
		for (int i=0; i<4; i++) {
			scanf("%d %d %d %d", &cards1[i][0], &cards1[i][1], &cards1[i][2], &cards1[i][3]);
		}

		scanf("%d", &secondAns);
		for (int i=0; i<4; i++) {
			scanf("%d %d %d %d", &cards2[i][0], &cards2[i][1], &cards2[i][2], &cards2[i][3]);
		}

		firstAns--;
		secondAns--;

		// see which numbers in the specified rows recur

		int recurring = 0;
		int index;

		for (int i=0; i<4; i++) {
			int current = cards1[firstAns][i];
			// printf("current %d\n", current);
			for (int j=0; j<4; j++) {
				// printf("checking %d\n", cards2[secondAns][j]);
				if (cards2[secondAns][j] == current) {
					// printf("same\n");
					recurring++;
					index = j;
					break;
				}
			}
		}

		if (recurring == 0) printf("Volunteer cheated!\n", recurring);
		else if (recurring == 1) printf("%d\n", cards2[secondAns][index]);
		else printf("Bad magician!\n", recurring);
		
		// printf("%d %d\n", firstAns, secondAns);
		// for (int i=0; i<4; i++) {
		// 	for (int j=0; j<4; j++) {
		// 		printf("%d", cards1[i][j]);
		// 	}
		// 	printf("\n");
		// }
		// for (int i=0; i<4; i++) {
		// 	for (int j=0; j<4; j++) {
		// 		printf("%d", cards2[i][j]);
		// 	}
		// 	printf("\n");
		// }
		
	}

	return 0;
}