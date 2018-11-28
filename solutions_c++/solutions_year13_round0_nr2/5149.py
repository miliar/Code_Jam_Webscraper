#include<stdio.h>

int table[101][101];
int row, col;

bool judge(int r, int c)
{
	int value = table[r][c];
	bool findColError = false;
	bool findRowError = false;
	for(int i = 0; i < row; i++)
	{
		if(table[i][c] > value)
		{
			findColError = true;
			break;
		}
	}
	for(int i = 0; i < col; i++)
	{
		if(table[r][i] > value)
		{
			findRowError = true;
			break;
		}
	}
	if(findColError && findRowError)
		return true;

	return false;;
}

int main()
{
	int num;
	scanf("%d" ,&num);
	for(int k = 1; k <= num; k++)
	{
		scanf("%d %d", &row, &col);
		for(int i = 0; i < row; i++)
		{
			for(int j = 0; j < col; j++)
			{
				scanf("%d", &table[i][j]);
			}
		}

		bool findError = false;
		for(int i = 0; i < row; i++)
		{
			for(int j = 0; j < col; j++)
			{
				bool result = judge(i, j);
				if(result)
				{
					findError = true;
					break;
				}
			}
			if(findError)
				break;
		}
		if(findError)
		{
			printf("Case #%d: NO\n", k);
		}else
		{
			printf("Case #%d: YES\n", k);
		}

	}


	return 0;
}