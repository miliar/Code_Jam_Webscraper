#include <iostream.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string>

#define INFILE	"C-small-attempt3.in"
#define OUTFILE	"C-small-attempt3.out"

using namespace std;

int main(int argc, char *argv[])
{
	FILE *infile, *outfile;
	int NumOfCase = 0;
	int Result = 0;
	unsigned long Min = 0;
	unsigned long Max = 0;
	unsigned long Begin = 0;
	unsigned long End = 0;
	char CurChar;
	string strTmp, strInv;
	char NumBuffer[100];
	bool blCharCompare = false;

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
		NumOfCase = NumOfCase * 10 + (CurChar - '0');
 	}
 	printf("NumOfCase : %d\n", NumOfCase);

 	/* Read Case by Case */
 	for (int i=0; i<NumOfCase; i++) {
 		Min = 0;
 		Max = 0;
		/* Get number of row (N) */
 		while ((EOF != (CurChar = fgetc(infile))) && 
			   (' ' != CurChar)) {
			Min = Min * 10 + (CurChar - '0');
 		}
 	
 		/* Get number of row (M) */
 		Result = 0;
 		while ((EOF != (CurChar = fgetc(infile))) && 
			   ('\n' != CurChar)) {
			Max = Max * 10 + (CurChar - '0');
 		}

		Begin = (unsigned long)sqrt(Min);
		End = (unsigned long)sqrt(Max);
//		printf("%d, %d\n", Begin, End);
		for (int j=Begin; j<=End; j++) {
			blCharCompare = true;
			itoa(j, NumBuffer, 10);
			for (int k=0; k<(strlen(NumBuffer)); k++) {
				if (NumBuffer[k] != NumBuffer[strlen(NumBuffer) - k - 1]) {
					blCharCompare = false;
					break;
				}
			}
			if (true == blCharCompare) {
				itoa(j*j, NumBuffer, 10);
				for (int k=0; k<(strlen(NumBuffer)); k++) {
					if (NumBuffer[k] != NumBuffer[strlen(NumBuffer) - k - 1]) {
						blCharCompare = false;
						break;
					}
				}
			}
			if ((true == blCharCompare) &&
				(Min <= (j*j))) {
				printf("%d, %d\n", j, j*j);
				Result++;
			}
		}
		
		fprintf(outfile, "Case #%d: %d\n", i+1, Result);
	}

    fclose(infile);
    fclose(outfile);
    
	return 0;
}
