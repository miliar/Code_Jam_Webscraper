#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int tc, i, j, ans1, ans2;
	int k, count = 0;
	int arr1[4][4];
	int arr2[4][4];
	int m = 1;
	scanf ("%d", &tc);
	
	while (tc--) {
		count = 0;
		scanf("%d", &ans1);
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				scanf("%d", &arr1[i][j]);
			}
		}

		scanf ("%d", &ans2);
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				scanf("%d", &arr2[i][j]);
			}
		}

		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				if (arr1[ans1 - 1][i] == arr2[ans2 - 1][j]) {
					k = arr1[ans1 - 1][i];
					count++;
				}
			}
		}

		if (count == 1) {
			printf ("Case #%d: %d\n",m, k);
			m++;
		}

		if (count > 1) {
			printf ("Case #%d: Bad magician!\n", m);
			m++;
		}

		if (count == 0) {
			printf ("Case #%d: Volunteer cheated!\n",m);
			m++;
		}
	}

	return 0;
}
