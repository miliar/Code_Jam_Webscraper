/*
 * File: main.cpp
 * --------------
 * This is a blank C++ source file.
 */

#include <iostream>
#include <string>
#include "console.h"
#include "simpio.h"
#include <fstream>
#include "set.h"
#include "strlib.h"
using namespace std;

void tryToReadFile(ifstream & fileReader);
void processingFile(ifstream & fileReader);
void processNumber(ofstream &fileWriter,int num,int caseNum);
Set<int> elementsInNum(int num);

int limit=0;
//Set<int> numbersToSee={0,1,2,3,4,5,6,7,8,9};
Set<int> numbersToSee;

int main() {
	for(int i=0;i<10;i++){
		numbersToSee+=i;
	}
	foreach(int k in numbersToSee){
		cout<<k<<endl;
	}
	ifstream fileReader;
	tryToReadFile(fileReader);
	cout<<"processing file"<<endl;
	processingFile(fileReader);
	fileReader.close();
	cout<<"finished"<<endl;
	return 0;
}

void processingFile(ifstream &fileReader){
	ofstream fileWriter;
	fileWriter.open("result.in");
	fileReader>>limit;
	int caseNum=0;
	while(true){
		string line;
		fileReader>>line;
		//readline(fileReader,line);
		if(fileReader.fail()) break;
		caseNum++;
		int num=stringToInteger(line);
		processNumber(fileWriter,num,caseNum);
	}
	fileWriter.close();
}

void processNumber(ofstream &fileWriter,int num,int caseNum){
	//cout<<num<<endl;
	Set<int> numsLeft=numbersToSee;
	int currentNum;
	bool numFound=false;
	for(int i=1;i<limit;i++){
		int currentNum=i*num;
		numsLeft-=elementsInNum(currentNum);
		if(numsLeft.isEmpty()) {
			fileWriter<<"Case #"<<caseNum<<": "<<currentNum<<endl;
			numFound=true;
			break;
		}
	}
	//cout<<numsLeft<<endl;
	if(!numFound) fileWriter<<"Case #"<<caseNum<<": "<<"INSOMNIA"<<endl;
}


Set<int> elementsInNum(int num){
	Set<int> result;
	if(num==0) result+=0;
	while(num>0){
		result.add(num%10);
		num/=10;
	}
	return result;
}

void tryToReadFile(ifstream &fileReader){
	string fileName=getLine("enter file name:   ");
	fileReader.open(fileName.c_str());
	while(fileReader.fail()){
		fileName=getLine("can't open file, enter file name again:   ");
		fileReader.clear();
		fileReader.open(fileName.c_str());
	}
}

