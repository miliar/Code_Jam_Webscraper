#include <stdio.h>
#include <string.h>

const int N = 5;

int n, t[N][N], c[N*N];

int main () {
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; i++) {
		memset(c, 0, sizeof(c));

		for (int j = 0; j < 2; j++) {
			scanf("%d", &n);
			for (int x = 0; x < 4; x++)
				for (int y = 0; y < 4; y++)
					scanf("%d", &t[x][y]);

			for (int x = 0; x < 4; x++)
				c[t[n-1][x]]++;
		}

		int ans = 0, p;
		for (int i = 0; i < 20; i++) {
			if (c[i] == 2) {
				ans++;
				p = i;
			}
		}

		printf("Case #%d: ", i);
		if (ans == 0)
			printf("Volunteer cheated!\n");
		else if (ans == 1)
			printf("%d\n", p);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
