#include<stdio.h>

#define InputFile "C:\\TempP\\CodeJam\\input\\magic.txt"
#define OutputFile "C:\\TempP\\CodeJam\\input\\OUTmagic.txt"

void calcOutPutMagicTrick(FILE*, FILE*, int num);
void comaprerows(FILE* pOut, int casenum, int[], int[]);

int main()
{
	FILE* pFile = fopen(InputFile, "r");

	if (!pFile)
	{
		printf("Cannot open input.\n");
		return 0;
	}

	FILE* pOutFile  = fopen(OutputFile, "w");


	int nTestCases;
	//read test cases.
	fscanf(pFile,"%d\n", &nTestCases);

	for (int i=0; i < nTestCases; i++)
	{
		calcOutPutMagicTrick(pFile, pOutFile, i+1);
	}

	if (pFile)
	{
		fclose(pFile);
	}

	if (pOutFile)
	{
		fclose(pOutFile);
	}

	return 0;
}

void calcOutPutMagicTrick(FILE* pFile, FILE* pOut, int num)
{
	//Read the answer.
	int answer1;
	fscanf(pFile, "%d\n", &answer1);

	int arrangement1[4][4];
	for (int a1 = 0; a1 <4; a1++)
	{
		fscanf(pFile, "%d %d %d %d\n",&(arrangement1[a1][0]), &(arrangement1[a1][1]), &(arrangement1[a1][2]), &(arrangement1[a1][3]));
	}

	int answer2;
	fscanf(pFile, "%d\n", &answer2);

	int arrangement2[4][4];
	for (int a2 = 0; a2 <4; a2++)
	{
		fscanf(pFile, "%d %d %d %d\n",&(arrangement2[a2][0]), &(arrangement2[a2][1]), &(arrangement2[a2][2]), &(arrangement2[a2][3]));
	}

	comaprerows(pOut, num, arrangement1[answer1 -1], arrangement2[answer2 -1 ]);
}

void comaprerows(FILE* pOut, int casen, int row1[], int row2[])
{
	bool found = false;
	bool badMagician = false;
	int answer = 0;
	for (int i=0; i < 4; i++)
		for (int j=0; j<4; j++)
		{
			if (row1[i] == row2[j])
			{
				if (!found) 
				{
					found = true;
					answer = row1[i];
				} 
				else
				{
					badMagician = true;
					break;
				}
			}
		}

		if (badMagician)
		{
			fprintf(pOut, "Case #%d: Bad magician!\n", casen);
		} else if (found)
		{
			fprintf(pOut, "Case #%d: %d\n", casen, answer);
		} else
		{
			fprintf(pOut, "Case #%d: Volunteer cheated!\n", casen);
		}

}