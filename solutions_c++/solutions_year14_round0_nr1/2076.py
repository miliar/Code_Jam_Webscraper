// codejamQualRoundA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* in = fopen("smallA.in","r");
	FILE* out = fopen("smallA.out","w");
	int caseCount = 0;
	fscanf(in,"%d",&caseCount);

	int firstRow, secondRow;
	int firstGrid[4][4], secondGrid[4][4];

	for(int i=0;i<caseCount;i++)
	{
		fscanf(in,"%d",&firstRow);
		for(int r=0; r<4; r++)
			for(int c=0; c<4; c++)
				fscanf(in,"%d",&firstGrid[r][c]);
		fscanf(in,"%d",&secondRow);
		for(int r=0; r<4; r++)
			for(int c=0; c<4; c++)
				fscanf(in,"%d",&secondGrid[r][c]);

		int matches = 0, match = -1;
		for(int c=0; c<4; c++)
			for(int sc=0;sc<4;sc++)
				if(firstGrid[firstRow-1][c] == secondGrid[secondRow-1][sc]) 
				{
						matches++;
						match = firstGrid[firstRow-1][c];
				}
			

		if(matches==0) fprintf(out,"Case #%d: Volunteer cheated!\n",i+1);
		else if(matches==1) fprintf(out,"Case #%d: %d\n",i+1,match);
		else fprintf(out,"Case #%d: Bad magician!\n",i+1);
	}
	fclose(in); fclose(out);
	return 0;
}

