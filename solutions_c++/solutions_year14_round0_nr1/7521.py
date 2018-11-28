/*
 * main.cpp
 *
 *  Created on: 2014. 4. 12.
 *      Author: Administrator
 */
#include <stdio.h>

#define MATRIX_SIZE 4
int main()
{
	int testNumber, firstRow, secondRow;
	int firstMatrix[MATRIX_SIZE][MATRIX_SIZE];
	int secondMatrix[MATRIX_SIZE][MATRIX_SIZE];
	int matchCount, matchNumber;

	scanf("%d", &testNumber);

	for (int n = 1; n <= testNumber; n++)
	{
		matchCount = 0;

		scanf("%d", &firstRow);
//		printf("%d\n", firstRow);
		for(int i = 0; i < MATRIX_SIZE; i++)
		{
			for(int j = 0; j < MATRIX_SIZE; j++)
			{
				scanf("%d", &firstMatrix[i][j]);
//				printf("%d ", firstMatrix[i][j]);
			}
//			printf("\n");
		}

//		printf("\n");

		scanf("%d", &secondRow);
//		printf("%d\n", secondRow);
		for(int i = 0; i < MATRIX_SIZE; i++)
		{
			for(int j = 0; j < MATRIX_SIZE; j++)
			{
				scanf("%d", &secondMatrix[i][j]);
//				printf("%d ", secondMatrix[i][j]);
			}
//			printf("\n");

		}
//		printf("\n");

		firstRow--;
		secondRow--;
		for (int i = 0; i < MATRIX_SIZE; i++)
		{
			for (int j = 0; j <MATRIX_SIZE; j++)
			{
				if (firstMatrix[firstRow][i] == secondMatrix[secondRow][j])
				{
					matchCount++;
					matchNumber = firstMatrix[firstRow][i];
				}
			}

		}

		switch (matchCount) {
			case 0:
				printf("Case #%d: Volunteer cheated!\n", n);
			break;
			case 1:
				printf("Case #%d: %d\n", n, matchNumber);
				break;
			case 2:
			case 3:
			case 4:
				printf("Case #%d: Bad magician!\n", n);
				break;
			default:
				break;
		}
	}

	return 0;
}
