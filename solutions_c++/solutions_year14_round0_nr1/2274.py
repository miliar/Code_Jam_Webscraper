#include <stdio.h>

bool isIn(int x, int *b)
{
	int i;

	for (i = 0; i < 4; i++)
		if (x == b[i]) break;
	
	return i < 4;
}

int main()
{
	int T, t, i, j, a, b[4], x, k, cnt;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d", &a);
		for (i = 1; i <= 4; i++) 
			for (j = 0; j < 4; j++) {
				if (i == a) scanf("%d", &b[j]);
				else scanf("%d", &x);
			}
		scanf("%d", &a);
		k = -1; cnt = 0;
		for (i = 1; i <= 4; i++) 
			for (j = 0; j < 4; j++) {
				scanf("%d", &x);
				if (i == a) 
					if (isIn(x, b)) {
						k = x;
						cnt++;
					}
			}
		if (cnt > 1) printf("Case #%d: Bad magician!\n", t);
		else if (cnt == 0) printf("Case #%d: Volunteer cheated!\n", t);
		else printf("Case #%d: %d\n", t, k);
	}
	return 0;
}

