#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
double winTime(double farmValue, double cookieVelocity, double winCookie);
int main(){
	FILE *file;
	FILE *output;
	char buffer[40];
	int input;
	char *parsedDouble;
	int casenum = 0;
	double farmValue;
	double cookieVelocity;
	double winCookie;
	double allTimeduration;
	file = fopen("B-large.in", "r");
	output = fopen("Output2_large.txt", "w");
	if (file == NULL){
		printf("wrong file");
		getchar();
		return 0;
	}
	fgets(buffer, 40, file);
	input = atoi(buffer);
	while (input != casenum){
		fgets(buffer, 40, file);
		parsedDouble = strtok(buffer, " \n");
		farmValue = atof(parsedDouble);
		parsedDouble = strtok(NULL, " \n");
		cookieVelocity = atof(parsedDouble);
		parsedDouble = strtok(NULL, " \n");
		winCookie = atof(parsedDouble);
		allTimeduration = winTime(farmValue, cookieVelocity, winCookie);
		fprintf(output, "Case #%d: %.7f\n", casenum + 1, allTimeduration);
		casenum++;
	}
	fclose(file);
	fclose(output);
	return 0;
}
double winTime(double farmValue, double cookieVelocity, double winCookie){
	double alltime = 0;
	int farmnum = 0;
	double timeToWin;
	double timeTowinAtAddedFarm;
	double timeFornextFarm;
	while (1){
		timeToWin = (winCookie / (2 + (cookieVelocity*farmnum)));
		timeTowinAtAddedFarm = winCookie / (2 + (cookieVelocity*(farmnum + 1)));
		timeFornextFarm = (farmValue / (2 + cookieVelocity*farmnum));
		if ( (timeToWin - timeTowinAtAddedFarm) > timeFornextFarm ){
			alltime += timeFornextFarm;
			farmnum++;
			continue;
		}
		else{
			alltime += (winCookie / (2 + cookieVelocity*farmnum));
			break;
		}
	}
	return alltime;
}