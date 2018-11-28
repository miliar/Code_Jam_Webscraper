#include<stdio.h>
int main()
{
	freopen("output.txt", "w", stdout);
	int aa[17];
	int t, row1, row2;
	int card1[5][5], card2[5][5];
	int i, j, k, cnt = 0, ans = 0;

	scanf("%d", &t);
	for (i = 1; i <= t; i++){
		for (j = 1; j <= 16; j++) aa[j] = 0;
		cnt = 0;
		scanf("%d", &row1);
		for (j = 1; j <= 4; j++){
			for (k = 1; k <= 4; k++)
				scanf("%d", &card1[j][k]);
		}
		scanf("%d", &row2);
		for (j = 1; j <= 4; j++){
			for (k = 1; k <= 4; k++)
				scanf("%d", &card2[j][k]);
		}
		for (j = 1; j <= 4; j++) aa[card1[row1][j]]++;
		for (j = 1; j <= 4; j++) aa[card2[row2][j]]++;
		for (j = 1; j <= 16; j++){
			if (aa[j] >= 2){
				cnt++;
				ans = j;
			}
		}
		if (cnt >= 2) printf("Case #%d: Bad magician!\n", i);
		else if (cnt == 1) printf("Case #%d: %d\n", i, ans);
		else printf("Case #%d: Volunteer cheated!\n", i);
	}
}