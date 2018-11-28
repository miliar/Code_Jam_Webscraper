#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <hash_set>
#include <array>

#define FILE_BUF_SIZE 10000
#define L 10000
#define X 10000
#define MAX_LENGTH 10000

using namespace std;

void EvaluateChar(char& left, char& right, bool& negative);

enum Step
{
	STEP_FINDING_K,
	STEP_FINDING_J,
	STEP_FINDING_I,
	STEP_PROCESS_REMAIN
};



int main()
{
	// Prepare file
	FILE* inputFile;
	fopen_s(&inputFile, "C-small-attempt1.in", "r");
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
		// Read l and x 
		int l = 0;
		int x = 0;
		fscanf(inputFile, "%d %d", &l, &x);
		fgets(fileBuf, FILE_BUF_SIZE + 1, inputFile);

		// Read letters
		fgets(fileBuf, FILE_BUF_SIZE + 1, inputFile);

		// Make string		
		char myString[MAX_LENGTH];
		memset(myString, 0, sizeof(myString));
		for (int i = 0; i < x; i++)
		{
			memcpy(myString + (i * l), fileBuf, l);
		}

		// Dechar	
		bool negative = false;
		int index = l * x - 1;
		int indexOfI = 0;

		Step step = STEP_FINDING_K;
		while (true)
		{						
			if (index < 0)
			{
				break;
			}

			// Change step
			if (step == STEP_FINDING_K && myString[index] == 'k')
			{
				step = STEP_FINDING_J;
				index--;
				continue;
			}

			if (step == STEP_FINDING_J && myString[index] == 'j')
			{
				step = STEP_FINDING_I;
				index--;
				continue;
			}

			if (step == STEP_FINDING_I && myString[index] == 'i')
			{
				step = STEP_PROCESS_REMAIN;
				indexOfI = index;
				index--;
				continue;
			}

			if (index <= 0)
			{
				break;
			}

			EvaluateChar(myString[index - 1], myString[index], negative);
			index--;			
		}
				
		if (step == STEP_PROCESS_REMAIN && negative == false && ((indexOfI == 0 && myString[0] == 'i') || myString[0] == '1'))
		{
			fprintf(outputFile, "Case #%d: YES\n", caseNo);
		}
		else
		{
			fprintf(outputFile, "Case #%d: NO\n", caseNo);
		}	
	}

	return 1;
}

void EvaluateChar(char& left, char& right, bool& negative)
{
	if (left == '1')
	{ 
		if (right == '1')
		{			
			left = '1';			
		}
		else if (right == 'i')
		{
			left = 'i';			
		}
		else if (right == 'j')
		{
			left = 'j';			
		}
		else if (right == 'k')
		{
			left = 'k';
		}
	}
	else if (left == 'i')
	{ 
		if (right == '1')
		{
			left = 'i';
		}
		else if (right == 'i')
		{
			left = '1';
			negative = !negative;
		}
		else if (right == 'j')
		{
			left = 'k';
		}
		else if (right == 'k')
		{
			left = 'j';
			negative = !negative;
		}
	}
	else if (left == 'j')
	{ 
		if (right == '1')
		{
			left = 'j';
		}
		else if (right == 'i')
		{
			left = 'k';
			negative = !negative;
		}
		else if (right == 'j')
		{
			left = '1';
			negative = !negative;
		}
		else if (right == 'k')
		{
			left = 'i';
		}
	}
	else if (left == 'k')
	{
		if (right == '1')
		{
			left = 'k';
		}
		else if (right == 'i')
		{
			left = 'j';
		}
		else if (right == 'j')
		{
			left = 'i';
			negative = !negative;
		}
		else if (right == 'k')
		{
			left = '1';
			negative = !negative;
		}
	}

	right = '0';
}
