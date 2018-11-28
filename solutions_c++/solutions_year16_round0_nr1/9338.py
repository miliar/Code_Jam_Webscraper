/*
 * Main.cpp
 *
 *  Created on: 09 Nisan 2016
 *      Author: Hatice
 */

#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;

int countDigits=0;
int firstN, lastN;
int coefficient=1;
ofstream outFile;
int digits[10]={0,0,0,0,0,0,0,0,0,0};

void exportData(int caseNumber,int lastN){
  if(lastN==0)
     outFile<<"Case #"<<(caseNumber)<<": INSOMNIA"<<endl;
  else
     outFile<<"Case #"<<(caseNumber)<<": "<<lastN<<endl;
}

void markEachDigit(int x)
{
    if(x >= 10)
       markEachDigit(x / 10);

    int digit = x % 10;

    if(digits[digit]==0){
	countDigits++;
        digits[digit]=1;
    }
    
}

void findLastNum(int N, int i){
	if(N==0)
		//cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
		exportData(i+1,N);
	else{
		markEachDigit(N);
		if(countDigits==10)
			//cout<<"Case #"<<(i+1)<<": "<<N<<endl;
			exportData(i+1,N);
		else{
			findLastNum((++coefficient)*firstN,i);
		}
	}
}

void importData(char* infileName){
	fstream inFile(infileName,ios_base::in);
	int T, N;
	inFile >> T;
	for (int i=0;i<T;i++){
		inFile >> firstN;
		findLastNum(firstN,i);
		countDigits=0;
		coefficient=1;
		for(int j=0;j<10;j++)
			digits[j]=0;
	}
}

int main(int argc, char *argv[]){
	outFile.open(argv[2]);
	importData(argv[1]);
	
	return 0;

}
