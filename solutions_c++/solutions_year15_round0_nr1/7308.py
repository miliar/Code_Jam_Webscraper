#include <stdlib.h>
#include <stdio.h>
#include <string>

#define STRING_LENGTH   1024
#define SMAX            1024

using std::string;

int main()
{
    FILE *pFileIn;
	FILE *pFileOut;
	int NumOfGames = 0;
	char pText[256];
	char TmpCh;
	int CurPos = 0;
	int Idx;
	int i, j, k;

	// input file
	pFileIn = fopen("A-large.in", "r");
	if (NULL == pFileIn) {
    	printf("Cannot open input file.\n");
    	return -1;
	}
    
	// output file
	pFileOut = fopen("A-large.out", "w");
	if (NULL == pFileOut) {
    	printf("Cannot open output file.\n");
    	return -1;
	}
    
	// get number of games
	TmpCh = fgetc(pFileIn);
	while ('\n' != TmpCh) {
    	pText[CurPos] = TmpCh;
    	CurPos++;
    	TmpCh = fgetc(pFileIn);
	}
//	printf("NumOfGames : %d\n", atoi(pText));
	
	NumOfGames = atoi(pText);
	
	// play game
	for (i=0; i<NumOfGames; i++) {
	    // get Smax
	    int Smax = 0;
	    CurPos = 0;
	    TmpCh = fgetc(pFileIn);
	    while (('\n' != TmpCh) && (' ' != TmpCh)) {
    	    pText[CurPos] = TmpCh;
    	    pText[CurPos+1] = ' ';
    	    CurPos++;
    	    TmpCh = fgetc(pFileIn);
	    }
	    Smax = atoi(pText);
//	    printf("Smax[%d] = %d\n", i, Smax);
	    
	    int S[SMAX];
	    int ClapNum = 0;
	    int AddAud = 0;
	    for (j=0; j<=Smax; j++) {
	        TmpCh = fgetc(pFileIn);

            // error warning
	        if ('\n' == TmpCh) {
	            printf("BBB %c\n", TmpCh);
	            break;
	        }

	        S[j] = TmpCh - '0';
//	        if (i==0 || i==1) {
//	            printf("S[%d][%d] = %d\n", i, j, S[j]);
//	        }
            if (j == 0) {
                ClapNum = S[j];
            } else {
                if (j > ClapNum) {
                    AddAud += j - ClapNum;
                    ClapNum = j;
                }
                ClapNum += S[j];
            }
	    }
	    // write to file
	    fprintf(pFileOut, "Case #%d: %d\n", i+1, AddAud);
	    printf("Case #%d: %d\n", i+1, AddAud);
	    
	    // clean the '\n'
	    TmpCh = fgetc(pFileIn);
	}
	
	// close file
	fclose(pFileIn);
	fclose(pFileOut);

    return 0;
}