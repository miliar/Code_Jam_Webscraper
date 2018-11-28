#include<cstdio>
#include<cstring>

int a[5][5];
int cnt[17];

int
main ()
{
	freopen("As.in","r",stdin);
	freopen("As.out","w",stdout);
	int t;
	scanf ("%d", &t);
	for (int tc = 1; tc <= t; tc ++){
		int row1, row2;
		scanf ("%d", &row1);
		for (int i = 1; i <= 4; i ++)
			for (int j = 1; j <= 4; j ++)
				scanf ("%d", &a[i][j]);

		memset (cnt, 0, sizeof (cnt));
		for (int i = 1; i <= 4; i ++)
			cnt[a[row1][i]] ++;
		
		scanf ("%d", &row2);
		for (int i = 1; i <= 4; i ++)
			for (int j = 1; j <= 4; j ++)
				scanf ("%d", &a[i][j]);

		for (int i = 1; i <= 4; i ++)
			cnt[a[row2][i]] ++;

		int ans = 0, ans_i = -1;
		for (int i = 1; i <= 16; i ++)
			if (cnt[i] == 2){
				ans ++;
				ans_i = i;
			}

		printf ("Case #%d: ",tc);
		switch (ans){
		case 0:
			printf ("Volunteer cheated!\n",tc);
			break;
		case 1:
			printf ("%d\n", ans_i);
			break;
		default:
			printf ("Bad magician!\n");
			break;
		}
	}
	return 0;
}