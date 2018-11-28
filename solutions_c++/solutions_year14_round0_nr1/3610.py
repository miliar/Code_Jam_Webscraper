#include <stdio.h>

using namespace std;

int main() {
	int tests = 0;
	int fnum = 0, snum = 0;
	int farr[4][4], sarr[4][4];
	int count = 0, result = 0;
	int j = 0, k = 0;

	scanf("%d\n", &tests);	

	for (int i = 1; i <= tests; i++) {
		count = 0;
		scanf("%d\n", &fnum);
		for (j = 0; j < 4; j++)
			scanf("%d %d %d %d\n", &farr[j][0], &farr[j][1], &farr[j][2], &farr[j][3]);

		scanf("%d\n", &snum);
                for (j = 0; j < 4; j++)
                        scanf("%d %d %d %d\n", &sarr[j][0], &sarr[j][1], &sarr[j][2], &sarr[j][3]);

		for (j = 0; j < 4; j++)
		    for (k = 0; k < 4; k++)
			if (sarr[snum-1][k] == farr[fnum-1][j]) {
				if (count == 0)
					result = farr[fnum-1][j];
				//printf("same number\n");
				count++;
			}

		if (count == 0) 
			printf("Case #%d: Volunteer cheated!\n", i);
		if (count == 1)
			printf("Case #%d: %d\n", i, result);
		if (count > 1)
			printf("Case #%d: Bad magician!\n", i);
	}
	return 0;
}
