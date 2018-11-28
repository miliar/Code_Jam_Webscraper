#include <stdlib.h>
#include <stdio.h>
#include <string>

#define FILE_NAME "B-small-attempt7"

using std::string;

int main()
{
	FILE *pFileIn;
	FILE *pFileOut;
	int NumOfGames = 0;
	char pText[256];
	char TmpCh;
	int CurPos = 0;
	double CostC, ExtraF, TargetX;
	
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

	for (int i = 0; i < NumOfGames; i++) {
		string strTmp = "";
		double CurRate = 2.0;
		double CurTime = 0;
		double CurCookies = 0;
		
		// get CostC
		TmpCh = fgetc(pFileIn);
		while(' ' != TmpCh && '\n' != TmpCh) {
			strTmp += TmpCh;
			TmpCh = fgetc(pFileIn);
		}
		sscanf(strTmp.c_str(), "%lf", &CostC);
		strTmp.clear();
		
		// get ExtraF
		TmpCh = fgetc(pFileIn);
		while(' ' != TmpCh && '\n' != TmpCh) {
			strTmp += TmpCh;
			TmpCh = fgetc(pFileIn);
		}
		sscanf(strTmp.c_str(), "%lf", &ExtraF);
		strTmp.clear();
		
		// get TargetX
		TmpCh = fgetc(pFileIn);
		while(' ' != TmpCh && '\n' != TmpCh) {
			strTmp += TmpCh;
			TmpCh = fgetc(pFileIn);
		}
		sscanf(strTmp.c_str(), "%lf", &TargetX);
		strTmp.clear();

		printf("CostC, ExtraF, TargetX = %lf, %lf, %lf\n", CostC, ExtraF, TargetX);
//		system("pause");

		CurTime = CostC / CurRate;
		while(1) {
			if (TargetX < CostC) {
				CurTime = TargetX / CurRate;
				break;
			}
			
			double NextTime_GetNewFarm = 0;
			double NextTime_NoNewFarm = 0;
			
			// get NextTime_GetNewFarm
			double NeedCookies = TargetX;
			NextTime_GetNewFarm = NeedCookies / (CurRate + ExtraF);
			NextTime_NoNewFarm = (NeedCookies - CostC) / CurRate;
			
//			printf("NextTime_GetNewFarm = %lf\n", NextTime_GetNewFarm);
//			printf("NextTime_NoNewFarm = %lf\n", NextTime_NoNewFarm);
//			system("pause");
			
			if (NextTime_GetNewFarm < NextTime_NoNewFarm) {
				// get new farm
				CurRate += ExtraF;
				CurTime += CostC / CurRate;
			} else {
				// no new farm
				CurTime += (NeedCookies - CostC) / CurRate;
				break;
			}
		}
		
//		printf("CurTime = %lf\n", CurTime);
//		system("pause");

		fprintf(pFileOut, "Case #%d: %lf\n", i+1, CurTime);
	}

	fclose(pFileIn);
	fclose(pFileOut);
	
	return 0;
}