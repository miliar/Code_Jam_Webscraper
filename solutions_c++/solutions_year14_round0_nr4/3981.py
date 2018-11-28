// SortingProblem.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <regex>
#include <math.h>
#include <basetsd.h>
#include <iomanip>
#include <limits>
using namespace std;
UINT64 p, q;
UINT64 n;

void merge(int *p, int start, int middle, int end, int order){
	int *r;
	int leftInd, rightInd;
	leftInd = start;
	rightInd = middle+1;
	
	r = (int *)malloc((end-start+1)*sizeof(int));
	if(order == 0){
		for(int i=0;i<end-start+1;i++){
			if(leftInd!=middle+1 && rightInd!=end+1){
				if(*(p+leftInd) > *(p+rightInd)){
					*(r+i) = *(p+rightInd);
					rightInd++;
				}else{
					*(r+i) = *(p+leftInd);
					leftInd++;
				}
			}else if(leftInd==middle+1 && rightInd!=end+1){
				*(r+i) = *(p+rightInd);
				rightInd++;
			}else if(leftInd!=middle+1 && rightInd==end+1){
				*(r+i) = *(p+leftInd);
				leftInd++;
			}else{
				
			}
		}
	}else{
		for(int i=0;i<end-start+1;i++){
			if(leftInd!=middle+1 && rightInd!=end+1){
				if(*(p+leftInd) < *(p+rightInd)){
					*(r+i) = *(p+rightInd);
					rightInd++;
				}else{
					*(r+i) = *(p+leftInd);
					leftInd++;
				}
			}else if(leftInd==middle+1 && rightInd!=end+1){
				*(r+i) = *(p+rightInd);
				rightInd++;
			}else if(leftInd!=middle+1 && rightInd==end+1){
				*(r+i) = *(p+leftInd);
				leftInd++;
			}else{
				
			}
		}
	}
	int k = 0;
	for(int i = start; i <= end; i++){
		*(p+i) = *(r+k);
		k++;
	}
	free(r);
}

void mergeSort(int *p,int start, int end, int order){
	int middle;

		if(start == end){
		
		}else{
			if(order == 0){
				middle = (end + start)/2;
				mergeSort(p,start,middle,order);
				mergeSort(p,middle+1,end,order);
				merge(p,start,middle,end,order);
				
			}else{
				//cout << "\n" << " " << p[0] << " " << p[1] << " " << p[2];
				middle = (end + start)/2;
				mergeSort(p,start,middle,order);
				mergeSort(p,middle+1,end,order);
				merge(p,start,middle,end,order);
			
			}
		}
	
	
}

void SortAsc(double *r,int len){
	double temp;
	temp = 1.0;
	for(int i = 0; i<len-1;i++){
		
		for(int j = i+1;j<len;j++){
			if(*(r+i) >= *(r+j) ){
				temp = *(r+i);
				*(r+i) = *(r+j);
				*(r+j) = temp;
			}

		}
	}
}


void SortDesc(double *r,int len){
	double temp;
	temp = 1.0;
	for(int i = 0; i<len-1;i++){
		
		for(int j = i+1;j<len;j++){
			if(*(r+i) <= *(r+j) ){
				temp = *(r+i);
				*(r+i) = *(r+j);
				*(r+j) = temp;
			}

		}
	}
}

void bookSorting(void){
	int i;
	ifstream file("D-large.in", std::ifstream::in);

	if (!file) {
		cout << "unable to open file";
		cin >> i;
		exit(1);
		
	}
	ofstream fileOut("output.txt", std::ifstream::out);

	if (!fileOut) {
		cout << "unable to create file";
		cin >> i;
		exit(1);
		
	}
	string line;
	getline(file,line);
	//std::getline(myfile,p);
	int numCases;
	//cout << "Here is the number "+line + "\n";
	std::istringstream(line) >> numCases;
	cout << numCases;
	
	
	int caseID;
	
	double *row2;
	double *row;
	int numWeights;
	double initRate;
	double timeTaken;
	int numCard;
	int j;
	for(int i=0;i<numCases;i++){
		getline(file,line);
		string caseString;
		caseString = "";
		istringstream(line) >> numWeights;
		cout << "\n " << numWeights;
		row = (double *) malloc(numWeights*sizeof(double));
		row2 = (double *) malloc(numWeights*sizeof(double));	
		getline(file,line);
		std::stringstream lineStream(line);
		std::string cell;
		for(int k = 0;k<numWeights;k++){
			std::getline(lineStream,cell,' ');
			std::istringstream(cell) >> *(row+k);
			
		}
		getline(file,line);
		std::stringstream lineStream2(line);
		std::string cell2;
		for(int k = 0;k<numWeights;k++){
			std::getline(lineStream2,cell2,' ');
			std::istringstream(cell2) >> *(row2+k);
			
		}
		
		SortAsc(row,numWeights);
		SortAsc(row2,numWeights);
		printf("\n");
		for(int m = 0;m<numWeights;m++){
			cout << *(row+m) << " ";
			
		}
		printf("\n");
		for(int m = 0;m<numWeights;m++){
			cout << *(row2+m) << " ";
			
		}
		int Ascore = 0;
		int Bscore = 0;
		int AscoreWar=0;
		int *winList = (int *)malloc(numWeights*sizeof(int));
		double temp;
		for(int k = 0;k<numWeights;k++){
			for(int m = k; m < numWeights;m++){
				if(*(row+k)<*(row2 + m)){
					*(winList+k) = 1;
					temp = *(row2 + m);
					*(row2 + m) = *(row2 + k);
					*(row2 + k) = temp;
					Bscore++;
					break;
				}else{
					*(winList+k) = 0;
					
				}
			}
		}
		Ascore = numWeights - Bscore;

		double *tempP = (double *)malloc(numWeights*sizeof(double));
		for(int m =0;m<numWeights;m++){
			*(tempP + m) = *(row+m);
		}
		Bscore = 0;
		SortDesc(row,numWeights);
		SortDesc(row2,numWeights);
		//SortDesc(tempP,numWeights);
		for(int m = 0;m<numWeights;m++){
			for(int k = 0; k < numWeights;k++){
				if(*(row+k)>*(row2 + m)){
					*(winList+k) = 1;
					*(row+k) = 0.0;
					Bscore++;
					break;
				}else{
					*(winList+k) = 0;
					
				}
			}
		}

		
		printf("\n");
		for(int m = 0;m<numWeights;m++){
			cout << *(tempP+m) << " ";
			
		}
		printf("\n");
		for(int m = 0;m<numWeights;m++){
			cout << *(row2+m) << " ";
			
		}
		stringstream ss;
		ss << Bscore;
		caseString.append(ss.str());
		stringstream ss2;
		ss2 << Ascore;
		caseString.append(" " + ss2.str());

		fileOut << "Case #" << i+1 << ": " << caseString << "\n"; 
		caseString = "";
		
		free(row);
		free(row2);
		
		

	}
	file.close();
	fileOut.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	int i;
	bookSorting();
	cout << "\n Exitted";
	cin >> i;
	return 0;
}






