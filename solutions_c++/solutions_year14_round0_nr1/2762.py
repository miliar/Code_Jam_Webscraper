#include <iostream>

int main()
{
	FILE * fIn;
	fopen_s(&fIn, "A-small-attempt0.in", "rt");
	FILE* fOut;
	fopen_s(&fOut, "A-small-attempt0.out", "wt");
	
	int T=0;
	int caseNum = 1;
	fscanf(fIn, "%d", &T);

	while(T--)
	{
		int r;
		int candidateNum1[4];
		int candidateNum2[4];
		fscanf(fIn, "%d", &r);
		for (int i = 1; i <= 4; i++)
		{
			if (i==r)
			{
				fscanf(fIn, "%d %d %d %d", &candidateNum1[0], &candidateNum1[1], &candidateNum1[2], &candidateNum1[3]);
			}
			else
			{
				int tempNum[4];
				fscanf(fIn, "%d %d %d %d", &tempNum[0], &tempNum[1], &tempNum[2], &tempNum[3]);
			}
		}
		
		fscanf(fIn, "%d", &r);
		for (int i = 1; i <= 4; i++)
		{
			if (i==r)
			{
				fscanf(fIn, "%d %d %d %d", &candidateNum2[0], &candidateNum2[1], &candidateNum2[2], &candidateNum2[3]);
			}
			else
			{
				int tempNum[4];
				fscanf(fIn, "%d %d %d %d", &tempNum[0], &tempNum[1], &tempNum[2], &tempNum[3]);
			}
		}
		int y = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (candidateNum1[i] == candidateNum2[j])
				{
					if (y == 0)
					{
						y = candidateNum1[i];
					}
					else
					{
						y = -1;
					}
				}
			}
		}
		if (y==0)
		{
			fprintf(fOut, "Case #%d: Volunteer cheated!\n", caseNum++);
		}
		else if(y==-1)
		{
			fprintf(fOut, "Case #%d: Bad magician!\n", caseNum++);
		}
		else
		{
			fprintf(fOut, "Case #%d: %d\n", caseNum++, y);
		}
	}
}