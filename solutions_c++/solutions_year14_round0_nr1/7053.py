//#pragma warning( disable : 4996 )
#include<stdio.h>

int i, j, k;
int x, y, res, test;
int data[6][6], data2[6][6];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &test);
	for (k = 1; k <= test; k ++ )
	{
		res = 0;
		scanf("%d", &x);
		for (i = 1; i <= 4; i++)
		{
			for (j = 1; j <= 4; j++)
				scanf("%d", &data[i][j]);
		}
		scanf("%d", &y);
		for (i = 1; i <= 4; i++)
		{
			for (j = 1; j <= 4; j++)
				scanf("%d", &data2[i][j]);
		}

		for (i = 1; i <= 4; i++)
		{
			for (j = 1; j <= 4; j++)
			{
				if (data2[y][i] == data[x][j]) break;
			}
			if (res == 0 && j != 5) res = data2[y][i];
			else if (res != 0 && j != 5) res = 17;
		}

		if (res == 0) printf("Case #%d: Volunteer cheated!\n", k);
		else if (res == 17) printf("Case #%d: Bad magician!\n", k);
		else printf("Case #%d: %d\n", k, res);
	}

	
	return 0;
}