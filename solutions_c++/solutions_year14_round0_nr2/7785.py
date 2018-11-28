#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma warning(disable:4996)

#define CASE_SIZE_ERROR -1
#define FILE_NOT_EXIST -2

#define CASE_LIMIT 100
#define BASIC_RATE 2
#define INPUT_NAME "B-large.in"
#define OUTPUT_NAME "output.txt"
#define OUTPUT_PREFIX "Case #"

typedef struct Game{
	double farmCost;
	double winGame;
	double additionalRate;
}Game;

void gameCondition(FILE* input, Game* game);
double timeBuy(Game* game, int farmCount);
double timeNotBuy(Game* game, int farmCount);

int main(void){
	FILE* input=NULL;
	FILE* output=NULL;
	int caseNum=0;
	double elapsedTime=0;
	int farmCount=0;
	int i=0;
	Game* game;
	char inputString[50];

	input=fopen(INPUT_NAME,"r");
	if(input==NULL)
		return FILE_NOT_EXIST;
	output=fopen(OUTPUT_NAME,"w");
	fclose(output);

	fgets(inputString,50,input);
	caseNum=atoi(inputString);
	if(caseNum<1||caseNum>CASE_LIMIT)
		return CASE_SIZE_ERROR;

	game=(Game*)malloc(sizeof(Game));

	for(;i<caseNum;i++){
		elapsedTime=0;
		farmCount=0;
		output=fopen(OUTPUT_NAME,"a");
		gameCondition(input,game);

		elapsedTime+=game->farmCost/BASIC_RATE;
		while(timeBuy(game,farmCount)<timeNotBuy(game,farmCount)){
			farmCount++;
			elapsedTime+=game->farmCost/(BASIC_RATE+farmCount*game->additionalRate);
		}
		elapsedTime+=timeNotBuy(game,farmCount);
		
		fprintf(output,"%s%d: %.7lf\n",OUTPUT_PREFIX,i+1,elapsedTime);
		fclose(output);
	}
	fclose(input);
	return 0;
}

void gameCondition(FILE* input, Game* game){
	char bufString[50]={NULL,};
	fgets(bufString,50,input);

	game->farmCost=atof(strtok(bufString," "));
	game->additionalRate=atof(strtok(NULL," "));
	game->winGame=atof(strtok(NULL," "));
}

double timeBuy(Game* game, int farmCount){
	return game->winGame/(BASIC_RATE+(farmCount+1)*game->additionalRate);
}

double timeNotBuy(Game* game, int farmCount){
	return (game->winGame-game->farmCost)/(BASIC_RATE+farmCount*game->additionalRate);
}