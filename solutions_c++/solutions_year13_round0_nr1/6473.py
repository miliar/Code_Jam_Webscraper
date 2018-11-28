// tic1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>
#include <assert.h>
#include <stdlib.h>

#define EMPTY 0
#define X 1
#define O 2
#define T 3

bool gameWins(unsigned int ** board,int player){
	for(int i=0;i<4;i++){
		int count=0;
		for(int j=0;j<4;j++){
			if(board[i][j]==player || board[i][j]==T) count++;
			
		}
		if(count==4) return true;
	}

	for(int i=0;i<4;i++){
		int count=0;
		for(int j=0;j<4;j++){
			if(board[j][i]==player || board[j][i]==T) count++;
			
		}
		if(count==4) return true;
	}
	int count=0;
	for(int i=0;i<4;i++){
		
		if(board[i][i]==player || board[i][i]==T) count++;
	}
	if(count==4) return true;

	count=0;
	for(int i=0;i<4;i++){
		
		if(board[3-i][i]==player || board[3-i][i]==T) count++;
	}
	if(count==4) return true;


	return false;
}

bool boardFull(unsigned int * board[]){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(board[i][j]==EMPTY) return false;
		}
	}
	return true;
}

void calculateStatus(unsigned int**  board,FILE* out,int caseIndex){
	if(gameWins(board,X)){
		fprintf(out,"Case #%d: X won\n",caseIndex);
	}
	else if(gameWins(board,O)){
		fprintf(out,"Case #%d: O won\n",caseIndex);
	}
	else{
		if (boardFull(board)){
			//tie
			fprintf(out,"Case #%d: Draw\n",caseIndex);
		}
		else{
			//game not over
			fprintf(out,"Case #%d: Game has not completed\n",caseIndex);
		}
	}
}

void fillBoardLine(char* str,unsigned int* boardLine){
	for(int i=0;i<4;i++){
		if(str[i]=='.') boardLine[i]=EMPTY;
		if(str[i]=='O') boardLine[i]=O;
		if(str[i]=='X') boardLine[i]=X;
		if(str[i]=='T') boardLine[i]=T;
	}
}

void startCalculation(FILE* in,FILE* out){
	char str[7];
	int caseIndex=1;
	int totalCases;
	 int credit,numItems;
	 unsigned int** board;
	 board=(unsigned int**)malloc(4*sizeof(unsigned int *));
	 for(int i=0;i<4;i++) 
		 board[i]=(unsigned int*)malloc(4*sizeof(unsigned int));
	 int c=0;
	//fgets(str,sizeof(str),in);//first line not important
	while(fgets(str,sizeof(str),in) != NULL)
   {
      // strip trailing '\n' if it exists
      int len =0;


	  if(c==0){
		  len = strlen(str)-1;
		  if(str[len] == '\n') 
			 str[len] = 0;
		  totalCases=atoi(str);
		  c++;
	  }
     //printf("\n%s", str);
	  //Parsing stage
	 for(int i=0;i<4;i++){
		 fgets(str,sizeof(str),in);
		 len = strlen(str)-1;
		  if(str[len] == '\n') 
			 str[len] = 0;

		  fillBoardLine(str,&board[i][0]);
	 }
	calculateStatus(board,out,caseIndex);

	 caseIndex++;
	 if(caseIndex>totalCases) break;
   }
	
}



int main(int argc, char* argv[])
{
	assert(argc==3);
	char* fileName=argv[1];
	FILE* inputFile=fopen(fileName,"r");
	assert(inputFile);

	char* outFilename=argv[2];
	FILE* outFile=fopen(outFilename,"w");
	assert(outFile);

	startCalculation(inputFile,outFile);

	fclose(inputFile);fclose(outFile);

	
	return 0;
}

