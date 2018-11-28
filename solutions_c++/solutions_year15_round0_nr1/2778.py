#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <hash_set>
#include <array>

#define FILE_BUF_SIZE 512
#define MAX_SHYNESS_LEVEL 6

using namespace std;



int main()
{
	// Prepare file
	FILE* inputFile;
	fopen_s(&inputFile, "A-small-attempt2.in", "r");
	if (inputFile == nullptr)
	{
		printf("Input file open error!\n");
	}

	FILE* outputFile;
	fopen_s(&outputFile, "Small_Output.txt", "w");
	if (outputFile == nullptr)
	{
		printf("Output file open error!\n");
	}

	// Read count of test case
	char fileBuf[FILE_BUF_SIZE + 1];
	fgets(fileBuf, FILE_BUF_SIZE + 1, inputFile);
	int countOfTestCase = atoi(fileBuf);

	for (int caseNo = 1; caseNo <= countOfTestCase; caseNo++)
	{
		// Read max shyness level and audience data
		int maxShynessLevel = atoi(fileBuf);
		char audienceData[MAX_SHYNESS_LEVEL + 2];
		fscanf(inputFile, "%d %s", &maxShynessLevel, audienceData);
		
		int standingAudience = 0;
		int needAudience = 0;
		for (int i = 0; i <= maxShynessLevel; i++)
		{
			char tempAudience = audienceData[i];
			int countOfAudience = atoi(&tempAudience);

			if (countOfAudience != 0 && i > standingAudience)
			{
				needAudience += (i - standingAudience);
				standingAudience += needAudience;
			}
			
			standingAudience += countOfAudience;
		}

		fprintf(outputFile, "Case #%d: %d\n", caseNo, needAudience);
	}

	return 1;
}
