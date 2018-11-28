// gcj-1b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *pFile, *pFileOut;
	pFile = fopen("A-large.in", "rb");
	pFileOut = fopen("out.txt", "wb");
	char N[256] = {0}, nCases = 0, tmp = 0;
	fgets(N, 5, pFile);
	nCases = atoi(N);
	for (int i = 0; i < nCases; i++)
	{
		fprintf(pFileOut, "Case #%d: ", i+1);
		int numbers[10] = { 0 }, letters[10] = {0};
		bool newLine=true;
		while (true)
		{
			tmp = fgetc(pFile);
			if ((tmp < 65) || (tmp > 90))
				if (newLine)
					newLine = false;
				else
					break;
			newLine = false;
			switch (tmp)
			{
			case 90:
				numbers[0]++;
				break;
			case 87:
				numbers[2]++;
				break;
			case 85:
				numbers[4]++;
				break;
			case 88:
				numbers[6]++;
				break;
			case 71:
				numbers[8]++;
				break;
			case 69:
				letters[0]++;
				break;
			case 79:
				letters[1]++;
				break;
			case 78:
				letters[2]++;
				break;
			case 84:
				letters[3]++;
				break;
			case 72:
				letters[4]++;
				break;
			case 73:
				letters[5]++;
				break;
			case 86:
				letters[6]++;
				break;
			case 70:
				letters[7]++;
				break;
			case 82:
				letters[8]++;
				break;
			case 83:
				letters[9]++;
				break;
			default:
				break;
			}
		}		
		letters[4] = letters[4] - numbers[8];
		numbers[3] = letters[4];		
		letters[7] = letters[7] - numbers[4];
		numbers[5] = letters[7];
		letters[0] = letters[0] - (numbers[0] + numbers[8] + (2*numbers[3]) + numbers[5]);
		letters[1] = letters[1] - (numbers[0] + numbers[2] + numbers[4]);
		letters[3] = letters[3] - (numbers[2] + numbers[8]);		
		letters[5] = letters[5] - (numbers[6] + numbers[8] + numbers[5]);
		numbers[9] = letters[5];
		letters[6] = letters[6] - numbers[5];
		numbers[7] = letters[6];
		letters[0] = letters[0] - ((2 * numbers[7]) + numbers[9]);
		numbers[1] = letters[0];
		for (int j = 0; j < 10; j++)
			for (int k = 0; k < numbers[j]; k++)
				fprintf(pFileOut, "%d", j);
		if (i < (nCases - 1))
			fprintf(pFileOut, "\n");
	}	
	fcloseall();
	return 0;
}

