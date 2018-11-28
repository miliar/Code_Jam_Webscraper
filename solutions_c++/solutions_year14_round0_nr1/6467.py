#include <stdio.h>
#define MAX 4
int mas_1[MAX][MAX];
int mas_2[MAX][MAX];


int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int count;
	for (count = 0; count < T; count++){
		int i, j;
		int first, second;
		int result = 0;
		int max;
		scanf("%d", &first);
		for (i = 0; i < MAX; i++)
		for (j = 0; j < MAX; j++)
			scanf("%d", &mas_1[i][j]);
		scanf("%d", &second);
		for (i = 0; i < MAX; i++)
		for (j = 0; j < MAX; j++)
			scanf("%d", &mas_2[i][j]);
		first -= 1;
		second -= 1;

		for (i = 0; i < MAX; i++)
		for (j = 0; j < MAX; j++) {
			if (mas_1[first][i] == mas_2[second][j]) {
				result++;
				max = mas_1[first][i];
			}
		}
		if (result == 1)
			printf("Case #%d: %d\n", count+1, max);
		else if (result>1)
			printf("Case #%d: %s\n", count+1, "Bad magician!");
		else printf("Case #%d: %s\n", count+1, "Volunteer cheated!");
	}
	return 0;
}