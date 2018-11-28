#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <hash_set>
#include <array>

#define FILE_BUF_SIZE 512
#define MAX_PLATE 1000
#define MAX_PANCAKE 1000

using namespace std;



int main()
{
	// Prepare file
	FILE* inputFile;
	fopen_s(&inputFile, "B-large.in", "r");
	if (inputFile == nullptr)
	{
		printf("Input file open error!\n");
	}

	FILE* outputFile;
	fopen_s(&outputFile, "Large_Output.txt", "w");
	if (outputFile == nullptr)
	{
		printf("Output file open error!\n");
	}

	// Read count of test case
	char fileBuf[FILE_BUF_SIZE + 1];
	fgets(fileBuf, FILE_BUF_SIZE + 1, inputFile);
	int countOfTestCase = atoi(fileBuf);

	int originalCountOfPancake[MAX_PLATE];
	int countOfPancake[MAX_PLATE];
	for (int caseNo = 1; caseNo <= countOfTestCase; caseNo++)
	{
		// Read original count of plate		
		fgets(fileBuf, FILE_BUF_SIZE + 1, inputFile);
		int originalCountOfPlate = atoi(fileBuf);				

		// Read pancake data
		int totalCountOfPancake = 0;	
		int maxCountOfPancake = 0;
		memset(originalCountOfPancake, 0, sizeof(originalCountOfPancake));
		for (int i = 0; i < originalCountOfPlate; i++)
		{
			fscanf(inputFile, "%d", &originalCountOfPancake[i]);
			totalCountOfPancake += originalCountOfPancake[i];
			maxCountOfPancake = max(maxCountOfPancake, originalCountOfPancake[i]);
		}
		fgets(fileBuf, FILE_BUF_SIZE + 1, inputFile);
				
		// Greed method
		int minMinute = INT_MAX;
		for (int i = 1; i <= maxCountOfPancake; i++)
		{
			// Prepare
			int recommandCountOfPancake = i;
			int countOfPlate = originalCountOfPlate;
			memcpy(countOfPancake, originalCountOfPancake, sizeof(originalCountOfPancake));

			// Calculate count of plate			
			for (int i = 0; i < originalCountOfPlate; i++)
			{
				if (countOfPancake[i] > recommandCountOfPancake)
				{
					countOfPlate += ((countOfPancake[i] / recommandCountOfPancake) - 1);
					if (countOfPancake[i] % recommandCountOfPancake != 0)
					{
						countOfPlate++;
					}

					countOfPancake[i] = recommandCountOfPancake;
				}
			}

			// Calculate max count of pancake
			int maxCountOfPancake = 0;
			for (int i = 0; i < originalCountOfPlate; i++)
			{
				maxCountOfPancake = max(maxCountOfPancake, countOfPancake[i]);
			}

			// Calculate minute
			int minute = maxCountOfPancake + (countOfPlate - originalCountOfPlate);
			minMinute = min(minMinute, minute);
		}

		fprintf(outputFile, "Case #%d: %d\n", caseNo, minMinute);
	}

	return 1;
}
