#include <iostream.h>
#include <stdlib.h>
#include <stdio.h>
#include <string>

#define INFILE	"B-large.in"
#define OUTFILE	"B-large.out"
#define MAX_LAWN_SIZE	10000

bool CheckPossibility(int* pLawn, int NRow, int MCol)
{
	int i=0, j=0;
	bool pblLawn[MAX_LAWN_SIZE];
	int TmpMax = 0;

	for (i=0; i<NRow; i++) {
		/* Find max */
		TmpMax = 0;		
		for (j=0; j<MCol; j++) {
			if (TmpMax < pLawn[i * MCol + j]) {
				TmpMax = pLawn[i * MCol + j];
			}
		}
		/* Check possiblility */
		for (j=0; j<MCol; j++) {
			if (TmpMax > pLawn[i * MCol + j]) {
				pblLawn[i * MCol + j] = false;
			} else {
				pblLawn[i * MCol + j] = true;
			}
		}
	}
	for (j=0; j<MCol; j++) {
		/* Find max */
		TmpMax = 0;		
		for (i=0; i<NRow; i++) {
			if (TmpMax < pLawn[i * MCol + j]) {
				TmpMax = pLawn[i * MCol + j];
			}
		}
		/* Check possiblility */
		for (i=0; i<NRow; i++) {
			if ((TmpMax > pLawn[i * MCol + j]) &&
				(false == pblLawn[i * MCol + j])) {
				return false;
			}
		}
	}
	
	return true;
}

int main(int argc, char *argv[])
{
	FILE *infile, *outfile;
	int i = 0, j = 0, k = 0;
	int NumOfGame = 0;
	int NRow = 0;
	int MCol = 0;
	int TmpVal = 0;
	char CurChar;
	int pLawn[MAX_LAWN_SIZE];
	bool blIsPossible;

	if ( (infile = fopen(INFILE, "r")) == NULL ) {
		printf("can't open input file\n");
		return -1;
	} else if( (outfile = fopen(OUTFILE, "w+")) == NULL ) {
		printf("can't open output file\n");
		return -1;
	}

	/* Get number of test case */
	while ((EOF != (CurChar = fgetc(infile))) && 
		   ('\n' != CurChar)) {
		NumOfGame = NumOfGame * 10 + (CurChar - '0');
 	}
 	printf("NumOfCase : %d\n", NumOfGame);

 	/* Read Case by Case */
 	for (i=0; i<NumOfGame; i++) {
 		NRow = 0;
 		MCol = 0;
		/* Get number of row (N) */
 		while ((EOF != (CurChar = fgetc(infile))) && 
			   (' ' != CurChar)) {
			NRow = NRow * 10 + (CurChar - '0');
 		}
 	
 		/* Get number of row (M) */
 		while ((EOF != (CurChar = fgetc(infile))) && 
			   ('\n' != CurChar)) {
			MCol = MCol * 10 + (CurChar - '0');
 		}

		/* Read a single Case, Case #(i+1) */
		k = 0;
		for (j=0; j<NRow*MCol;) {
			if (EOF == (CurChar = fgetc(infile))) {
				printf("Reading file error!!\n");
			}
			
			if (('\n' != CurChar) && (' ' != CurChar)) {
				TmpVal = TmpVal * 10 + (CurChar - '0');
			} else {
				pLawn[j] = TmpVal;
				TmpVal = 0;
				j++;
			}
		}
		
		/* Check if it's possible */
		blIsPossible = CheckPossibility(pLawn, NRow, MCol);
		
		fprintf(outfile, "Case #%d: %s\n", i+1, (true == blIsPossible) ? "YES" : "NO");
	}

    fclose(infile);
    fclose(outfile);
    
	return 0;
}
