#include <stdio.h>

int main(){
	FILE *r, *s;
	int testNum;
	int rowNumA, rowNumB;
	int currRound =0,currRow;
	int count =0, output;
	int inputA[4];
	int inputB[4];
	char temp[100];

	r = fopen("A-small-attempt2.in", "r");
	s = fopen("A-small-attempt2.out", "w");
	fscanf(r, "%d\n", &testNum);

	while (currRound < testNum){
		currRow = 0;
		fscanf(r, "%d\n", &rowNumA);
		while (currRow < (rowNumA - 1)){
			fgets(temp, sizeof(temp), r);
			currRow++;
		}

		fscanf(r, "%d %d %d %d\n", &inputA[0], &inputA[1], &inputA[2], &inputA[3]);
		while (currRow < 3){
			fgets(temp, sizeof(temp), r);
			currRow++;
		}

		currRow = 0;
		fscanf(r, "%d\n", &rowNumB);
		while (currRow < (rowNumB - 1)){
			fgets(temp, sizeof(temp), r);
			currRow++;
		}

		fscanf(r, "%d %d %d %d\n", &inputB[0], &inputB[1], &inputB[2], &inputB[3]);
		while (currRow < 3){
			fgets(temp, sizeof(temp), r);
			currRow++;
		}
		
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (inputA[i] == inputB[j]){
					count++;
					output = inputA[i];
				}
			}
		}
		if (count == 0)
			fprintf(s, "Case #%d: Volunteer cheated!\n", currRound + 1);
		else if (count == 1)
			fprintf(s, "Case #%d: %d\n", currRound + 1, output);
		else
			fprintf(s, "Case #%d: Bad magician!\n", currRound + 1);
		
		count = 0;
		currRound++;
	}
}
