// MagicTrick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int N = 0;
	int Row1=0;
	int Row2=0;
	int arrOption1[16];
	int arrOption2[16];
	int iNumberCount = 0;
	int iMagicNumber = 0;

	FILE* fpin = fopen("C:\\GCJ\\A-small-attempt2.in", "r");
	FILE* fpout = fopen("C:\\GCJ\\A-small-attempt2.out", "w");

	if(NULL == fpin || NULL == fpout )
		return 0;

	fscanf(fpin, "%d", &N);

	for (int tc = 0; tc<N; tc++)
	{
		fscanf(fpin, "%d", &Row1);
		for(int i = 0; i < 16; i+=4)
		{  
			fscanf(fpin, "%d %d %d %d", &arrOption1[i], &arrOption1[i+1], &arrOption1[i+2], &arrOption1[i+3]);
		}

		fscanf(fpin, "%d", &Row2);
		for(int i = 0; i < 16; i+=4)
		{  
			fscanf(fpin, "%d %d %d %d", &arrOption2[i], &arrOption2[i+1], &arrOption2[i+2], &arrOption2[i+3]);
		}

		for(int i = ((Row1-1)*4); i < (Row1*4); i++) 
		{
			for(int j = ((Row2-1)*4); j < (Row2*4); j++) 
			{
				if (arrOption1[i] == arrOption2[j])
				{
					iNumberCount++;
					iMagicNumber = arrOption1[i];
				}
			}
		}

		if (iNumberCount == 1)
		{
			fprintf(fpout, "Case #%d: %d\n", tc+1, iMagicNumber);
		}
		else if( iNumberCount > 1)
		{
			fprintf(fpout, "Case #%d: Bad magician!\n", tc+1);
		}
		else
		{
			fprintf(fpout, "Case #%d: Volunteer cheated!\n", tc+1);
		}
		iNumberCount = 0;
	}

	fclose(fpin);
	fclose(fpout);
	return 0;

	
}

