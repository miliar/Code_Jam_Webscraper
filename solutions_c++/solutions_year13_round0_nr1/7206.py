#include <stdio.h>
#include <stdlib.h>
#include <share.h>

const unsigned int MAX_U16 = 65535;

void main()
{
	char* fileName = "..\\input\\A-large.in";
	char* fileOutName = "..\\output\\A-large.out";
	FILE* filePtr = _fsopen(fileName, "r", _SH_DENYNO);
	FILE* fileOutPtr = _fsopen(fileOutName, "w", _SH_DENYNO);
	if (!filePtr || !fileOutPtr)
	{
		printf("File not found\n");
		return;
	}

	char currLine[MAX_U16];
	fgets(currLine, MAX_U16, filePtr);
	int numCases = atoi(currLine);
	for (int i = 0; i < numCases; i++)
	{
		char currState[4][4];
		for (int j = 0; j < 4; j++)
		{
			fgets(currLine, MAX_U16, filePtr);
			for (int k = 0; k < 4; k++)
				currState[j][k] = currLine[k];
		}

		bool bFoundDot = false;
		bool bWinX = false;
		bool bWinO = false;

		// Check for not done
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (currState[j][k] == '.')
				{
					bFoundDot = true;
					break;
				}
			}
		}

		// Check horizontal
		for (int j = 0; j < 4; j++)
		{
			int xCount = 0;
			int oCount = 0;
			for (int k = 0; k < 4; k++)
			{
				if (currState[j][k] == 'X')
					xCount++;
				else if (currState[j][k] == 'O')
					oCount++;
				else if (currState[j][k] == 'T')
				{
					xCount++;
					oCount++;
				}
			}
			if (xCount == 4)
				bWinX = true;
			else if (oCount == 4)
				bWinO = true;
		}

		// Check vertical
		for (int j = 0; j < 4; j++)
		{
			int xCount = 0;
			int oCount = 0;
			for (int k = 0; k < 4; k++)
			{
				if (currState[k][j] == 'X')
					xCount++;
				else if (currState[k][j] == 'O')
					oCount++;
				else if (currState[k][j] == 'T')
				{
					xCount++;
					oCount++;
				}
			}
			if (xCount == 4)
				bWinX = true;
			else if (oCount == 4)
				bWinO = true;
		}

		// Check diagonal TL to BR
		int xCount = 0;
		int oCount = 0;
		for (int j = 0; j < 4; j++)
		{	
			if (currState[j][j] == 'X')
				xCount++;
			else if (currState[j][j] == 'O')
				oCount++;
			else if (currState[j][j] == 'T')
			{
				xCount++;
				oCount++;
			}
		}
		if (xCount == 4)
			bWinX = true;
		else if (oCount == 4)
			bWinO = true;

		// Check diagonal TR to BL
		xCount = 0;
		oCount = 0;
		for (int j = 0; j < 4; j++)
		{	
			if (currState[j][3 - j] == 'X')
				xCount++;
			else if (currState[j][3 - j] == 'O')
				oCount++;
			else if (currState[j][3 - j] == 'T')
			{
				xCount++;
				oCount++;
			}
		}
		if (xCount == 4)
			bWinX = true;
		else if (oCount == 4)
			bWinO = true;

		if (i != numCases - 1)
			fgets(currLine, MAX_U16, filePtr);

		if (bWinX)
			fprintf(fileOutPtr, "Case #%d: X won\n", i + 1);
		else if (bWinO)
			fprintf(fileOutPtr, "Case #%d: O won\n", i + 1);
		else if (bFoundDot)
			fprintf(fileOutPtr, "Case #%d: Game has not completed\n", i + 1);
		else
			fprintf(fileOutPtr, "Case #%d: Draw\n", i + 1);
	}
	fflush(fileOutPtr);
	fclose(fileOutPtr);
	fclose(filePtr);
}