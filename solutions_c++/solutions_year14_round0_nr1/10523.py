#include<stdio.h>
int main() {
	int x, ans1[4][4], ans2[4][4], i, j, n, m, k = 1;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d", &x);
	int a = x;
	while (k <= a) {
		int ok = 0, card = 0;
		scanf("%d", &n);
		for (i = 1;i <=4; i++)
			for (j = 1;j <=4; j++)
				scanf("%d", &ans1[i][j]);
		scanf("%d", &m);
		for (i = 1;i <= 4; i++)
			for (j = 1;j <=4; j++)
				scanf("%d", &ans2[i][j]);
		for (i = 1;i <= 4; i++)
			for (j = 1;j <=4; j++)
				if (ans1[n][i] == ans2[m][j]) {
					card = ans1[n][i];
					ok++;
				}
		if (card == 0)
			printf("Case #%d: Volunteer cheated!\n", k);
		else
			if (ok > 1)
				printf("Case #%d: Bad magician!\n", k);
			else
				if (ok != 0 && card != 0)
			printf("Case #%d: %d\n", k, card);
		k++;
	}
	return 0;
}
