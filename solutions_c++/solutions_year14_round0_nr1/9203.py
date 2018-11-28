#include <cstdio>

int main ()
{
	int T;
	int r1, r2;
	int arr1[5][5];
	int arr2[5][5];
	scanf("%d", &T);

	for (int tcase = 1; tcase <= T; tcase++)
	{
		//Read data

		scanf("%d", &r1);

		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1;j <= 4; j++)
			{
				scanf("%d", &arr1[i][j]);
			}
		}

		scanf("%d", &r2);

		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1;j <= 4; j++)
			{
				scanf("%d", &arr2[i][j]);
			}
		}

		//Find matches

		int match;
		int cntMatches = 0;
		bool isMatch;

		for (int i = 1; i <= 4; i++)
		{
			isMatch = false;

			for (int j = 1; j <= 4; j++)
			{
				isMatch |= (arr1[r1][i] == arr2[r2][j]);
			}

			if (isMatch)
			{
				match = arr1[r1][i];
				cntMatches++;
			}
		}

		if (cntMatches == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", tcase);
		}

		else if (cntMatches == 1)
		{
			printf("Case #%d: %d\n", tcase, match);
		}

		else
		{
			printf("Case #%d: Bad magician!\n", tcase);
		}
	}
}