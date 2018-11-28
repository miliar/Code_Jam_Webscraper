// lawn.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <assert.h>
#include <string.h>
#include <stdlib.h>

void  readIntegersToArray(char *str,int numItems,unsigned int *arr){
	//string inString=std::string(str,strlen(str));
	char * pch;
	int index=0;
	pch = strtok (str," \n");
	  while (pch != NULL)
	  {
		
		int num = atoi(pch);
		arr[index]=num;
		index++;
		pch = strtok (NULL," \n");
	  }
}

bool isDone(unsigned int** grass,unsigned int ** currentGrass,int n,int m){
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++){
			if(grass[i][j]!=currentGrass[i][j]) return false;
		}

	return true;
}

bool isValid(unsigned int** grass,unsigned int ** currentGrass,int n,int m){
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++){
			if(grass[i][j]>currentGrass[i][j]) return false;
		}

	return true;
}

void getUncuttedMaximumIndex(unsigned int ** grass,unsigned int ** currentGrass,int n,int m,int * rowIndex,int* colIndex){
	int max=0;
	int rowi=-1,coli=-1;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(grass[i][j]!=currentGrass[i][j] && grass[i][j]>max){
				max=grass[i][j];
				rowi=i;coli=j;
			}
		}
	}
	*rowIndex=rowi;*colIndex=coli;
}

bool recursiveCalculation(unsigned int ** grass,unsigned int** currentGrass,int n,int m){

	unsigned int ** tempGrass;


	if(!isValid(grass,currentGrass,n,m)) return false;
	if(isDone(grass,currentGrass,n,m)) return true;

	tempGrass=(unsigned int**)malloc(n*sizeof(unsigned int*));
	for(int row=0;row<n;row++) tempGrass[row]=(unsigned int*)malloc(sizeof(unsigned int)*m);  
	 for(int row=0;row<n;row++)
		 for(int col=0;col<m;col++) tempGrass[row][col]=currentGrass[row][col];
	int rowIndex,colIndex;




	getUncuttedMaximumIndex(grass,currentGrass,n,m,&rowIndex,&colIndex);

	//debug
	/*for(int i=0;i<n;i++){
		for(int j=0;j<m;j++)
			printf("%d ",currentGrass[i][j]);
		printf("\n__________________\n");
	}


	getc(stdin);*/
	//try row cutting 
	for(int j=0;j<m;j++) tempGrass[rowIndex][j]=grass[rowIndex][colIndex];
	if(recursiveCalculation(grass,tempGrass,n,m)){
		for(int row=0;row<n;row++) free(tempGrass[row]);
		free(tempGrass);
		return true;
	}

	//try col cuttinh
	for(int row=0;row<n;row++)
		 for(int col=0;col<m;col++) tempGrass[row][col]=currentGrass[row][col];
	for(int i=0;i<n;i++) tempGrass[i][colIndex]=grass[rowIndex][colIndex];
	if(recursiveCalculation(grass,tempGrass,n,m)){
		for(int row=0;row<n;row++) free(tempGrass[row]);
		free(tempGrass);
		return true;
	}


	for(int row=0;row<n;row++) free(tempGrass[row]);
	free(tempGrass);
	return false;

}


 void calculateSucces(unsigned int ** grass,int n,int m,FILE* out,int index){
	 /*for(int i=0;i<n;i++){
		 for(int j=0;j<m;j++){
			 printf("%d ",grass[i][j]);
		 }
		 printf("\n");
	 }*/
	 unsigned int** currentGrass;
	 currentGrass=(unsigned int**)malloc(n*sizeof(unsigned int*));
	 for(int row=0;row<n;row++) currentGrass[row]=(unsigned int*)malloc(sizeof(unsigned int)*m);     
	 for(int row=0;row<n;row++)
		 for(int col=0;col<m;col++) currentGrass[row][col]=100;
	 bool suc=recursiveCalculation(grass,currentGrass,n,m);
	 if(suc) fprintf(out,"Case #%d: YES\n",index);
	 else  fprintf(out,"Case #%d: NO\n",index);
 }

void startCalculation(FILE* in,FILE* out){
	char str[10000];
	int caseIndex=1;

	int credit,numItems;
	unsigned int prices[2000];//man number of items is 2000
	int n=0,m=0;
	unsigned int** grass; 


	fgets(str,sizeof(str),in);//first line not important
	while(fgets(str,sizeof(str),in) != NULL)
   {
      // strip trailing '\n' if it exists
      int len = strlen(str)-1;
      if(str[len] == '\n') 
         str[len] = 0;
	  sscanf(str,"%d %d",&n,&m);
	  //allocation
	  grass=(unsigned int**)malloc(n*sizeof(unsigned int*));
	  for(int row=0;row<n;row++) grass[row]=(unsigned int*)malloc(sizeof(unsigned int)*m);     
	  //Parsing stage
	  for(int row=0;row<n;row++){
		  fgets(str,sizeof(str),in);
		  readIntegersToArray(str,m,&grass[row][0]);
	  }
	  //calculation stage
	  calculateSucces(grass,n,m,out,caseIndex);

	// startCalculation(prices,numItems,credit,out,caseIndex);
	 for(int row=0;row<n;row++) free(grass[row]);
	 free(grass);
	 caseIndex++;
   }
	//getc(stdin);
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
	return 0;
}

