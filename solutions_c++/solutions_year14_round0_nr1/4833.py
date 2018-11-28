#include <stdlib.h>
#include <stdio.h>
#include <string>

using std::string;

int main()
{
	FILE *pFile;
	FILE *pFileOut;
	int NumOfGames = 0;
	char pText[256];
	char TmpCh;
	int CurPos = 0;
	int Idx;
	int j;

	// input file
	pFile = fopen("A-small-attempt5.in", "r");
	if (NULL == pFile) {
		printf("Cannot open input file.\n");
		return -1;
	}
	
	// output file
	pFileOut = fopen("A-small-attempt5.out", "w");
	if (NULL == pFileOut) {
		printf("Cannot open output file.\n");
		return -1;
	}
	
	// get number of games
	TmpCh = fgetc(pFile);
	while ('\n' != TmpCh) {
		pText[CurPos] = TmpCh;
		CurPos++;
		TmpCh = fgetc(pFile);
	}
	printf("NumOfGames : %d\n", atoi(pText));
	NumOfGames = atoi(pText);
	
	// play games
	for (int i = 0; i < NumOfGames; i++) {
		int NumCnt = 0;
		int Num[34];
		int CardSet[16];
		int Start = 0;
		int Ans = 0;
				
		// get 34 number, (1+16)x2
		Num[0] = 0;
		while (34 > NumCnt) {
			TmpCh = fgetc(pFile);
			if ((TmpCh >= '0') && (TmpCh <= '9')) {
				Num[NumCnt] = Num[NumCnt]*10 + (TmpCh - '0');	
			} else {
				NumCnt++;
				Num[NumCnt] = 0;
			}
//			printf("%c\n", TmpCh);
//			printf("[%d]=[%d]", NumCnt, Num[NumCnt]);
		}
		
		// init. card set to zero
		for (j = 0; j < 16; j++) {
			CardSet[j] = 0;
		}
		
		// let's play, first round
		Start = (Num[0]-1) * 4 + 1;
		for (j = 0; j < 4; j++) {
			Idx = Num[Start + j];
			CardSet[Idx - 1]++;
		}
		
		// second round
		Start = (Num[17]-1) * 4 + 18;
		for (j = 0; j < 4; j++) {
			Idx = Num[Start + j];
			CardSet[Idx - 1]++;
		}
		
		// check card set
		printf("=== Game %d ===\n", i+1);
		for (j = 0; j < 16; j++) {
			printf("CardSet[%d] = %d\n", j, CardSet[j]);
			if (2 == CardSet[j]) {
				Ans = (0==Ans) ? j + 1 : -1;
			}
		}
		
		// Ans : 1~16 normal
		// Ans : -1 more than 2 number in these two row, mag error
		// Ans : 0 cheated
		
		//Case #1: 7
		//Case #2: Bad magician!
		//Case #3: Volunteer cheated!
		fprintf(pFileOut, "Case #%d: ", i+1);
		
		if (-1 == Ans) {
			fprintf(pFileOut, "Bad magician!\n");
		} else if (0 == Ans) {
			fprintf(pFileOut, "Volunteer cheated!\n");
		} else {
			fprintf(pFileOut, "%d\n", Ans);
		}
//		system("pause");
	}
	
	// close file
	fclose(pFile);
	fclose(pFileOut);
	
	return 0;
}