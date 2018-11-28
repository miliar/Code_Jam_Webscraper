#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void printCase(char firstrow[20], char secondrow[20], FILE *file);
int main(){
	FILE *file;
	FILE *output;
	char buffer[20];
	char firstrow[20];
	char secondrow[20];
	int input;
	int rownum[2];
	int casenum= 0;
	file = fopen("A-small-attempt0.in", "r");
	output = fopen("Output.txt", "w");
	if (file == NULL){
		printf("wrong file");

		getchar();
		return 0;
	}
	fgets(buffer, 20, file);
	input = atoi(buffer);
	while (input != casenum){
		for (int i = 0; i < 2; i++){
			fgets(buffer, 20, file);
			rownum[i] = atoi(buffer);
			for (int j = 0; j < 4; j++){
				fgets(buffer, 20, file);
				if (j == rownum[i]-1 && i == 0){
					strcpy(firstrow, buffer);
				}
				else if (j == rownum[i] - 1 && i == 1){
					strcpy(secondrow, buffer);
				}
				else continue;
			}
		}

		fprintf(output, "Case #%d: ", casenum+1);
		printCase(firstrow, secondrow, output);
		casenum++;
	}
	fclose(file);
	fclose(output);
	return 0;
}
void printCase(char firstrow[20],char secondrow[20], FILE *file){
	char *parsechar = nullptr;
	int answer=0;
	int samenum = 0;
	int firstdec[4];
	int seconddec[4];
	parsechar = strtok(firstrow, " \n");
	for (int k = 0; k < 4; k++){
		firstdec[k] = atoi(parsechar);
		parsechar = strtok(NULL, " \n");
	}
	parsechar = strtok(secondrow, " \n");
	for (int n = 0; n < 4; n++){
		seconddec[n] = atoi(parsechar);
		parsechar = strtok(NULL, " \n");
	}
	for (int i = 0; i <4; i++){
		for (int j = 0; j < 4; j++){
			if (firstdec[i] == seconddec[j]){
				answer = firstdec[i];
				samenum++;
				break;
			}
		}
		if (samenum>1) break;
	}
	if (samenum > 1) fprintf(file, "Bad magician!\n");
	else if (answer == 0)
		fprintf(file, "Volunteer cheated!\n");
	else
		fprintf(file, "%d\n", answer);
}