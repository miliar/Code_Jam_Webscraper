#include <stdio.h>

int main(int argc, char *argv[])
{
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		int row;
		scanf("%d", &row);

		int arr[4][4];
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				scanf("%d", &arr[j][k]);
			}
		}

		int newrow;
		scanf("%d", &newrow);

		int newarr[4][4];
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				scanf("%d", &newarr[j][k]);
			}
		}

		int result;
		int count = 0;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (arr[row-1][j] == newarr[newrow-1][k])
				{
					result = arr[row-1][j];
					count++;
				}
			}
		}

		if (count == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", i+1);
		}
		else if (count == 1)
		{
			printf("Case #%d: %d\n", i+1, result);
		}
		else
		{
			printf("Case #%d: Bad magician!\n", i+1);
		}
	}
}
