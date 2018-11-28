// magic.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include "stdio.h"


int _tmain(int argc, char* argv[])
{
	FILE* inputFile;
	FILE*outputFile;
	errno_t err1 = fopen_s(&inputFile, "A-small-attempt2.in", "r");
	errno_t err2 = fopen_s(&outputFile, "output-attempt2.ou", "w+");
	
	int numpreOfAttempt;
	int line1, line2;
	int tab1[4][4], tab2[4][4];

	if(!err1 || !err2)
	{
		fscanf_s(inputFile, "%d", &numpreOfAttempt);
		for(int i=0; i<numpreOfAttempt; i++)
		{
			fscanf_s(inputFile, "%d", &line1);
			for(int j=0; j<4; j++)
			{
				for(int k=0; k<4; k++)
				{
					fscanf_s(inputFile, "%d", &tab1[j][k]);
				}
			}
			fscanf_s(inputFile, "%d", &line2);
			for(int j=0; j<4; j++)
			{
				for(int k=0; k<4; k++)
				{
					fscanf_s(inputFile, "%d", &tab2[j][k]);
				}
			}
			int counter = 0;
			int var = 0;
			for(int j=0; j<4; j++)
			{
				for(int k=0; k<4;k++)
				{
					if(tab1[line1-1][j]==tab2[line2-1][k])
					{
						counter++;
						var = tab1[line1-1][j];
					}
				}
			}
			if(counter == 1)
			{
				fprintf_s(outputFile, "Case #%d: %d\n", i+1, var);
			}
			else
			{
				if (counter > 1)
				{
				fprintf_s(outputFile,"Case #%d: Bad magician!\n", i+1);
				}
				else
				{
				fprintf_s(outputFile,"Case #%d: Volunteer cheated!\n", i+1);
				}
			}

		}
		fclose(inputFile);
		fclose(outputFile);
	}
	return 0;
}

