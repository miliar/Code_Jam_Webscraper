#include <cstdio>
#include <iostream>
#include <string>

int main ()
{
	freopen("a.in", "r",stdin);
	freopen("a.out", "w", stdout);

	int test_case = 0;
	int case_no = 1;

	scanf("%d", &test_case);
	while(test_case--)
	{
		int grid[4][4] = {0};
		int grid2[4][4] = {0};
		int row_no = 0;
		int row_no2 = 0;
		int result = 0;

		scanf("%d", &row_no);
		row_no--;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				scanf("%d", &grid[i][j]);
			}
		}

		scanf("%d", &row_no2);
		row_no2--;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				scanf("%d", &grid2[i][j]);
			}
		}

		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				if(grid[row_no][i] == grid2[row_no2][j])
				{
					if(result == 0)
					{
						result = grid[row_no][i];
					}
					else
					{
						result = -1;
						break;
					}
				}
			}
			if(result == -1)
				break;
		}

		if(result == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", case_no++);
		}
		else if(result == -1)
		{
			printf("Case #%d: Bad magician!\n", case_no++);
		}
		else
		{
			printf("Case #%d: %d\n", case_no++, result);
		}
	}

	return 0;
}