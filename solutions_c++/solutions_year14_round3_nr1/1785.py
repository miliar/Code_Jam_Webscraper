#include <stdlib.h>
#include <stdio.h>
#include <string>

#define FILE_NAME		"A-small-attempt1"

using std::string;

typedef struct MASS_DATA {
	string strOwner;
	float weight;
	bool blCompeted;
};

int main()
{
	FILE *pFileIn;
	FILE *pFileOut;
	int NumOfGames = 0;
	char pText[256];
	char TmpCh;
	int CurPos = 0;
	double CostC, ExtraF, TargetX;
	int i,j;
	
	pFileIn = fopen(FILE_NAME".in", "r");
	if (NULL == pFileIn) {
		printf("Cannot open input file.\n");
		return -1;
	}
	
	// output file
	pFileOut = fopen(FILE_NAME".out", "w");
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
	printf("NumOfGames : %d\n", atoi(pText));
	NumOfGames = atoi(pText);
	
	// play games
	for (i=0; i<NumOfGames; i++) {
		int P, Q; // P/Q
		TmpCh = fgetc(pFileIn);
		CurPos = 0;
		while (('\n' != TmpCh) && ('/' != TmpCh)) {
			pText[CurPos] = TmpCh;
			CurPos++;
			pText[CurPos] = ' ';
			TmpCh = fgetc(pFileIn);
		}
		printf("P : %d\n", atoi(pText));
		P = atoi(pText);
		
		TmpCh = fgetc(pFileIn);
		CurPos = 0;
		while (('\n' != TmpCh) && ('/' != TmpCh)) {
			pText[CurPos] = TmpCh;
			CurPos++;
			pText[CurPos] = ' ';
			TmpCh = fgetc(pFileIn);
		}
		printf("Q : %d\n", atoi(pText));
		Q = atoi(pText);
		
		// check if Q legal
		int Tmp = Q;
		int Generations = 0;
		while ((Tmp!=-1) && (Tmp!=1)) {
			if (0 != Tmp%2) {
				Tmp = -1;
				break;
			}
			Tmp = Tmp/2;
			Generations++;
//			printf("%d\n", Tmp);
		}
		if (Tmp!=1) {
			printf("Case illegal! %d\n", Tmp);
			fprintf(pFileOut, "Case #%d: impossible\n", i+1);
			continue;
		}
		
		// ANS = Y
		int Y = Generations;
		Tmp = P;
		while (Tmp!=1) {
			Tmp = Tmp/2;
			Y--;
			printf("%d\n", Tmp);
		}
		printf(">> %d %d\n", Generations, Y);
		fprintf(pFileOut, "Case #%d: %d\n", i+1, Y);
//		system("pause");
	}

	// close files	
	fclose(pFileIn);
	fclose(pFileOut);
	
	return 0;

}