/*
 * Main.cpp
 *
 *  Created on: 09 Nisan 2016
 *      Author: Hatice
 */

#include <iostream>
#include <string>
#include <stdio.h>
#include <fstream>
using namespace std;

ofstream outFile;
string temp;
bool isHappy;
int minCount=0;
void exportData(int caseNumber){
  outFile << "Case #"<<caseNumber<<": "<<minCount << endl;
}

void findMinimum(string S,int caseNumber){
	bool isDone=true;int index=0;
	if(S[0]=='+')
		{isHappy=true;}
	else
		{isHappy=false;}
	index++;

	for(int i=1;i<S.size();i++){
		if(S[i]=='+' && isHappy==true)
			index++;
		else if (S[i]=='-' && isHappy==true){
			isHappy=false;
			index++;
		}
		else if(S[i]=='-' && isHappy==false){
			index++;
		}
		else if(S[i]=='+' && isHappy==false){
			break;
		}
	}
	if(isHappy==false){
		for(int j=0;j<index;j++){
			if(S[j]=='+')
				S[j]='-';
			else
				S[j]='+';
		}
		minCount++;
	}

	for(int i=0;i<S.size();i++){
		if(S[i]=='-'){
			isDone=false;
			break;
		}
	}

	if(isDone==true){
		exportData(caseNumber);
		minCount=0;
	}
	else{
		findMinimum(S,caseNumber);
	}
		

}
void importData(char* infileName){
	fstream inFile(infileName,ios_base::in);
	int T;
	string S;
	inFile >> T;
	for (int i=0;i<T;i++){
		inFile >> S;
		findMinimum(S,i+1);
	}
	
}

int main(int argc, char *argv[]){
	outFile.open(argv[2]);
	importData(argv[1]);
	
	

	return 0;

}
