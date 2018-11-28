#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

void main(){
	int roundNum, currRound =0;
	int blockNum;
	int i,j, warWin=0, dewarWin=0;
	double *naomiNum1, *kenNum1;
	double *naomiNum2, *kenNum2;

	FILE *r = fopen("D-large.in","r");
	FILE *s = fopen("D-large.out","w");
	fscanf(r,"%d\n", &roundNum);

	while (currRound < roundNum){
		fscanf(r, "%d\n", &blockNum);
		naomiNum1 = (double*)malloc(sizeof(double)* blockNum);
		kenNum1 = (double*)malloc(sizeof(double)* blockNum);
		naomiNum2 = (double*)malloc(sizeof(double)* blockNum);
		kenNum2 = (double*)malloc(sizeof(double)* blockNum);
		for (i = 0; i < blockNum; i++)
			fscanf(r, "%lf", &naomiNum1[i]);
		for (i = 0; i < blockNum; i++)
			fscanf(r, "%lf", &kenNum1[i]);
		sort(naomiNum1, naomiNum1 + blockNum);
		sort(kenNum1, kenNum1 + blockNum);
		for (i = 0; i < blockNum; i++){
			naomiNum2[i] = naomiNum1[i];
			kenNum2[i] = kenNum1[i];
		}
		//for (i = 0; i < blockNum; i++)
		//	printf("%lf %lf\n", naomiNum[i], kenNum[i]);

		

		for (i = 0; i < blockNum; i++){ // war
			for (j = 0; j < blockNum; j++){
				if (naomiNum1[i] < kenNum1[j] && naomiNum1[i] != -1 && kenNum1[j] != -1){
					naomiNum1[i] = -1;
					kenNum1[j] = -1;
					warWin--;
					break;
				}
			}
		}

		for (i = 0; i < blockNum; i++){ // dewar
			for (j = 0; j < blockNum; j++){
				if (naomiNum2[i] > kenNum2[j] && naomiNum2[i] != -1 && kenNum2[j] != -1){
					naomiNum2[i] = -1;
					kenNum2[j] = -1;
					dewarWin++;
					break;
				}
			}
		}

		warWin += blockNum;
		fprintf(s, "Case #%d: %d %d\n", currRound + 1, dewarWin, warWin);
		warWin= 0;
		dewarWin = 0;
		currRound++;
	}
}