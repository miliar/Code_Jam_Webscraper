#include <stdlib.h>
#include <stdio.h>
#include <string>

#define FILE_NAME		"D-large"
#define MAX_DATA_LEN	1000

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
		int NumOfMass = 0;
		float Naomi[MAX_DATA_LEN];
		float Ken[MAX_DATA_LEN];
		string strTmp;
		int NaomiWinsDW = 0, KenWinsW = 0;
		
		// get number of mass
		CurPos = 0;
		TmpCh = fgetc(pFileIn);
		while ('\n' != TmpCh) {
			pText[CurPos] = TmpCh;
			pText[CurPos + 1] = ' ';
			CurPos++;
			TmpCh = fgetc(pFileIn);
		}
		printf("NumOfMass : %d\n", atoi(pText));
		NumOfMass = atoi(pText);
		
		// get Nomi line
		for (int j = 0; j < NumOfMass; j++) {
			TmpCh = fgetc(pFileIn);
			while(' ' != TmpCh && '\n' != TmpCh) {
				strTmp += TmpCh;
				TmpCh = fgetc(pFileIn);
			}
			sscanf(strTmp.c_str(), "%f", &Naomi[j]);
			strTmp.clear();	
		}
		
		// get Ken line
		for (int j = 0; j < NumOfMass; j++) {
			TmpCh = fgetc(pFileIn);
			while(' ' != TmpCh && '\n' != TmpCh) {
				strTmp += TmpCh;
				TmpCh = fgetc(pFileIn);
			}
			sscanf(strTmp.c_str(), "%f", &Ken[j]);
			strTmp.clear();	
		}

		// sort, big -> small
		MASS_DATA MassData[NumOfMass*2];
		for (int j = 0; j < NumOfMass; j++) {
			MassData[j].strOwner = "Naomi";
			MassData[j].weight = Naomi[j];
			MassData[j].blCompeted = false;
			MassData[j+NumOfMass].strOwner = "Ken";
			MassData[j+NumOfMass].weight = Ken[j];
			MassData[j+NumOfMass].blCompeted = false;
		}
		while(1) {
			bool blSorted = false;
			for (int j = 0; j < (2*NumOfMass - 1); j++) {
				if (MassData[j].weight < MassData[j+1].weight) {
					string strTmpOwner = MassData[j].strOwner;
					float TmpWeight = MassData[j].weight;
					MassData[j].strOwner = MassData[j+1].strOwner;
					MassData[j].weight = MassData[j+1].weight;
					MassData[j+1].strOwner = strTmpOwner;
					MassData[j+1].weight = TmpWeight;
					blSorted = true;
				}
			}
			if (false == blSorted) {
				break;
			}
		}
		for (int j = 0; j < NumOfMass*2; j++) {
			printf("@@@ [%s][%f]\n", MassData[j].strOwner.c_str(), MassData[j].weight);
		}

		// play Deceitful war
		for (int j = 0; j < NumOfMass*2; j++) {
			// get maximum naomi
			if ("Naomi" != MassData[j].strOwner) {
				continue;
			}
			
			for (int k = j; k < NumOfMass*2; k++) {
				// skip if not ken or competed
				if (("Ken" != MassData[k].strOwner) ||
					(true == MassData[k].blCompeted)) {
					continue;
				}
				
				MassData[k].blCompeted = true;
				NaomiWinsDW++;
				break;
			}
		}
		
		// play war
		for (int j = 0; j < NumOfMass*2; j++) {
			// get maximum naomi
			if ("Ken" != MassData[j].strOwner) {
				continue;
			}
			
			for (int k = j; k < NumOfMass*2; k++) {
				// skip if not ken or competed
				if (("Naomi" != MassData[k].strOwner) ||
					(true == MassData[k].blCompeted)) {
					continue;
				}
				
				MassData[k].blCompeted = true;
				KenWinsW++;
				break;
			}
		}
		
//		printf("@@@[%d][%d]\n", NaomiWinsDW, NumOfMass - KenWinsW);
//		system("pause");
		fprintf(pFileOut, "Case #%d: %d %d\n", i+1, NaomiWinsDW, NumOfMass - KenWinsW);

	}
	
	fclose(pFileIn);
	fclose(pFileOut);
	
	return 0;
}
