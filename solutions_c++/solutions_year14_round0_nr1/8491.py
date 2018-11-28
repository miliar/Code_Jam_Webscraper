#include <iostream>
using namespace std;

void main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, row1, row2, i, j, sum, number;
	int a1[5][5], a2[5][5];
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
	{
		sum = 0;
		scanf("%d", &row1);
		for (i = 1; i <= 4; i++)
			for (j = 1; j <= 4; j++)
				scanf("%d", &a1[i][j]);

		scanf("%d", &row2);
		for (i = 1; i <= 4; i++)
			for (j = 1; j <= 4; j++)
				scanf("%d", &a2[i][j]);

		for (i = 1; i <= 4; i++)
			for (j = 1; j <= 4; j++)
				if (a1[row1][i] == a2[row2][j])
				{
					number = a1[row1][i];
					sum++;
				}
		if (sum == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", t);
		}
		else if ( sum > 1)
		{
			printf("Case #%d: Bad magician!\n", t);
		}
		else
		{
			printf("Case #%d: %d\n", t, number);
		}
	}
	
}