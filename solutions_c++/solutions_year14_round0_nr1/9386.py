// prob1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fpi;
	FILE *fpo;

	int nT;

	int n1,n2;
	int card1[4][4];
	int card2[4][4];
	int i,j;
	int k;
	int theCard = 0;


	fpi = fopen("A-small-attempt0.in","r");
	if (!fpi)
	{
		printf("Fail to open the input file!\n");
		exit(0);
	}
	
	fpo = fopen("A-small-attempt0.out","w");
	if (!fpo)
	{
		printf("Fail to open the output file!\n");
		exit(0);
	}

	fscanf(fpi, "%d", &nT);
	for (k=0; k<nT; k++)
	{
		theCard = 0;

		fscanf(fpi, "%d", &n1);
		for (i=0; i<4; i++)
		{
			for (j=0; j<4; j++)
			{
				fscanf(fpi, "%d", &card1[i][j]);
			}
		}

		fscanf(fpi, "%d", &n2);
		for (i=0; i<4; i++)
		{
			for (j=0; j<4; j++)
			{
				fscanf(fpi, "%d", &card2[i][j]);
			}
		}

		for (i=0; i<4; i++)
		{
			for (j=0; j<4; j++)
			{
				if (card1[n1-1][i] == card2[n2-1][j])
				{
					if (theCard != 0)
					{
						theCard = 99;
						goto OVER;
					}
					theCard = card1[n1-1][i];
				}
			}
		}

OVER:
		if (theCard == 0)
		{
			fprintf(fpo, "Case #%d: Volunteer cheated!\n", k+1);
		}
		else
		{
			if (theCard > 16)
			{
				fprintf(fpo, "Case #%d: Bad magician!\n", k+1);
			}
			else
			{
				fprintf(fpo, "Case #%d: %d\n", k+1, theCard);
			}
		}
	}

	fclose(fpi);
	fclose(fpo);

	return 0;
}

