#include <stdio.h>



int countMatch(int* match, int row1[], int row2[])
{
	int count = 0;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (row1[i]==row2[j])
			{
				*match = row1[i];
				count++;
			}
		}
	}
	return count;
}

int main(int argc, char const *argv[])
{
	freopen (argv[1], "r", stdin);
	freopen (argv[2], "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int row1;
		int grid1[4][4];
		scanf("%d", &row1);
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf ("%d", grid1[i]+j);
			}
		}
		int row2;
		int grid2[4][4];
		scanf("%d", &row2);
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf ("%d", grid2[i]+j);
			}
		}
		int match;
		int count = countMatch (&match, grid1[row1-1], grid2[row2-1]);
		char ans[32];
		if (count==0)
		{
			sprintf (ans, "%s", "Volunteer cheated!");
		}
		else if (count>1)
		{
			sprintf (ans, "%s", "Bad magician!");
		}
		else
		{
			sprintf (ans, "%d", match);
		}
		sprintf (ans, "%s", ans);
		printf("Case #%d: %s\n", t, ans);
	}
	return 0;
}