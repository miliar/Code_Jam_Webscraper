#include<iostream>
#include<stdlib.h>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996)

int main(void){

	FILE* ifp;
	FILE* ofp;

	ifp = fopen("A-large.in", "r");
	ofp = fopen("output.txt", "w");

	if (ifp == NULL || ofp == NULL){
		printf("open error");
		return 0;
	}

	char cT[100]; memset(cT, NULL, 100);
	int iT = 0;
	fgets(cT, 100, ifp);
	iT = atoi(cT);
//	printf("iT:%s", cT);
	for (int i = 1; i <= iT; i++){

		//당 개수 추출 //26개 당까지
		char cN[100]; memset(cN, NULL, 100);
		int iN = 0;
		fgets(cN, 100, ifp);
		if (strlen(cN) == 0) break;
		iN = atoi(cN);
//		printf("iN: %d ", iN);
		//각 당의 당원들 추출
		char cP[1000]; memset(cP, NULL, 100);
		int iP[30] = { 0 };
		int iIndex = 0;
		fgets(cP, 1000, ifp);

		int total = 0;

		char* tokenPtr = strtok(cP, " ");
		while (tokenPtr != NULL){
			iP[iIndex] = atoi(tokenPtr);
			//printf("%d ", iP[iIndex]);
			total += iP[iIndex];
			iIndex++;
			tokenPtr = strtok(NULL, " ");
		}
		
		//결과
		char result[60000]; memset(result, NULL, 60000);
		sprintf(result, "Case #%d:", i);
		int rIndex;
		if (i < 10) rIndex = 8;
		else rIndex = 9;

		if (iN == 2){
			if (iP[0] > iP[1]){
				while (iP[0] != iP[1]){
					result[rIndex++] = ' ';
					char C;
					iP[0]--; C = 0 + 65; result[rIndex++] = C;
					if (iP[0] == iP[0 + 1]) break;
					iP[0]--; C = 0 + 65; result[rIndex++] = C;

				}
			}
			else if (iP[0] < iP[0 + 1]){
				while (iP[0] != iP[0 + 1]){
					result[rIndex++] = ' ';
					char C;
					iP[0 + 1]--; C = (0+1) + 65; result[rIndex++] = C;
					if (iP[0] == iP[0 + 1]) break;
					iP[0 + 1]--; C = (0+1) + 65; result[rIndex++] = C;
				}
			}
//			printf("[%d]", iP[0]);
			while (iP[0] != 0){
				result[rIndex++] = ' ';
				iP[0]--; iP[0 + 1]--;
				char C;
				C = 0 + 65; result[rIndex++] = C; //printf("%c", C);
				C = (0 + 1) + 65; result[rIndex++] = C; //printf("%c", C);
			}
			result[rIndex] = '\n';
			fputs(result, ofp);
		}
		else{
			/*
			for (int k = 0; k<iIndex; k++){
		//		printf("%d ", iP[k]);
			}
			*/
			int count = 0;
			while (total > 2){
				//최대값 구하기
				char C = ' '; result[rIndex++] = C;

				int max = 0;

				for (int j = 0; j < iIndex; j++){

					if (iP[max] < iP[j]){
						max = j;
						//maxIndex = j;
					}
				}
				iP[max] -= 1; //1명 탈출
				total -= 1; //전체 수 줄음

				C = max + 65; result[rIndex++] = C;
			}
			result[rIndex++] = ' ';
			for (int k = 0; k < iIndex; k++){
				if (iP[k] != 0){
					char C = k + 65; result[rIndex++] = C;
				}

			}

			//printf("%d", count);
			result[rIndex] = '\n';
			fputs(result, ofp);
		}
	}

	return 0;
}