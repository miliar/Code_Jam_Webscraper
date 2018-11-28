#include "stdio.h"
#include "stdlib.h"
#include "string.h"

static FILE *Opfile;

void SolveCase ( int arrangement1[4][4], int arrangement2[4][4], int ans1, int ans2, int caseNumber )
{
	int numSolns = 0, solution = 0;

	for(int i = 0; i< 4; i++)
	{
		for(int j = 0; j <4; j++)
		{
			if(arrangement1[ans1-1][i] == arrangement2[ans2-1][j])
			{
				numSolns++;
				solution = arrangement1[ans1-1][i];
				break;
			}
		}	
		if(numSolns > 1)
				break;
	}

	if(numSolns == 1)
		fprintf(Opfile, "Case #%d: %d\n", caseNumber, solution);
	else if(numSolns > 1)
		fprintf(Opfile, "Case #%d: Bad magician!\n", caseNumber);				
	else
		fprintf(Opfile, "Case #%d: Volunteer cheated!\n", caseNumber);				
}

// ---------------------------------------------------------------------------------
// This function takes the input file kept in the same dirctory with name "input.txt"
// and processes the input line by line and writes the output file in file
// "output.txt" in the same directory.
// ---------------------------------------------------------------------------------

int ProcessInputFile()
{
	static const char inputfile[] = "C:\\tmp\\A-small-attempt0.in";
	static const char outputfile[] = "C:\\tmp\\output_ques1.txt";

	FILE *Ipfile;
	fopen_s ( &Ipfile, inputfile, "r" );
	fopen_s ( &Opfile, outputfile, "w" );

	if ( Ipfile != NULL && Opfile != NULL)
	{
		int caseNumber = 1, numCases = 0;

		fscanf (Ipfile, "%d", &numCases);

		while ( numCases > 0 ) 
		{
			int arr1[4][4], arr2[4][4], ans1, ans2;
			fscanf (Ipfile, "%d", &ans1);
			for(int i = 0; i< 4; i++)
				fscanf (Ipfile, "%d %d %d %d", &arr1[i][0], &arr1[i][1], &arr1[i][2], &arr1[i][3]);

			fscanf (Ipfile, "%d", &ans2);
			for(int i = 0; i< 4; i++)
				fscanf (Ipfile, "%d %d %d %d", &arr2[i][0], &arr2[i][1], &arr2[i][2], &arr2[i][3]);

			SolveCase ( arr1, arr2, ans1, ans2, caseNumber++ );
			numCases--;
		}
		fclose ( Ipfile );
		fclose ( Opfile );
	}
	else
	{
		if(Ipfile == NULL)
			perror ( inputfile ); /* why didn't the file open? */
		if(Opfile == NULL)
			perror ( outputfile ); /* why didn't the file open? */
	}
	return 0;
}

// ---------------------------------------------------------------------------------
// Main Function
// ---------------------------------------------------------------------------------

int main ( void )
{
	return ProcessInputFile();
}