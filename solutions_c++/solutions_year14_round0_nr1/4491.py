#include <cstdio>

bool find(int key, int target[])
{
	for (int i = 0; i < 4; i++) if (target[i] == key) return true;
	return false;
}

int match(int r1[], int r2[])
{
	int c = 0;
	for (int i = 0; i < 4; i++) {
		if (find(r1[i], r2)) c++;
	}
	return c;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int r1, r2, map1[4][4], map2[4][4];
		scanf("%d", &r1);
		for (int i =0 ;i < 4; i++) for (int j = 0; j < 4; j++) scanf("%d", &map1[i][j]);
		scanf("%d", &r2);
		for (int i =0 ;i < 4; i++) for (int j = 0; j < 4; j++) scanf("%d", &map2[i][j]);
		int count = match(map1[r1-1],map2[r2-1]);
		printf("Case #%d: ", t+1);
		if (count == 0) {
			printf("Volunteer cheated!\n");
		}
		else if (count == 1) {
			for (int i = 0; i < 4; i++) if (find(map1[r1-1][i], map2[r2-1])) {
				printf("%d\n", map1[r1-1][i]);
				break;
			}
		}
		else {
			printf("Bad magician!\n");
		}
	}
}