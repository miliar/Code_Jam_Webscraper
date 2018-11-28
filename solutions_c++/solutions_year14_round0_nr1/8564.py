#include<stdio.h>
#define SIZE 4
int main()
{
	int numberOfTestCase;
	scanf("%d", &numberOfTestCase);
	int ip1[SIZE][SIZE], ip2[SIZE][SIZE];
	for (int x = 0; x < numberOfTestCase; x++)
	{
		int row1, row2;
		scanf("%d", &row1);
		for (int y = 0; y < SIZE; y++)
		{
			for (int z = 0; z < SIZE; z++)
			{
				scanf("%d", &ip1[y][z]);
			}
		}
		scanf("%d", &row2);
		for (int y = 0; y < SIZE; y++)
		{
			for (int z = 0; z < SIZE; z++)
			{
				scanf("%d", &ip2[y][z]);
			}
		}
		int noMatchedDigit = 0;
		int matchedNumber = 0;
		for (int y = 0; y < SIZE; y++)
		{
			for (int z = 0; z < SIZE; z++)
			{
				if (ip1[row1 - 1][y] == ip2[row2 - 1][z])
				{
					noMatchedDigit = noMatchedDigit + 1;
					matchedNumber = ip1[row1 - 1][y];
				}
			}
		}
		if (noMatchedDigit == 1)
		{
			printf("Case #%d: %d\n", x + 1, matchedNumber);
		}

		else if (noMatchedDigit > 1)
		{
			printf("Case #%d: Bad magician!\n", x + 1);
		} else
		{
			printf("Case #%d: Volunteer cheated!\n", x + 1);

		}
	}
	return 0;
}
