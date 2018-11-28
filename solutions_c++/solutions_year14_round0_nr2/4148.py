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
void bookSorting(void){
	int i;
	ifstream file("B-large.in", std::ifstream::in);

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
	
	
	double *row;
	int finalPos;
	double initRate;
	double timeTaken;
	int numCard;
	int j;
	for(int i=0;i<numCases;i++){
		getline(file,line);
		string caseString;
		caseString = "";
		
		row = (double *) malloc(3*sizeof(double));
			
		
		istringstream(line) >> *(row+0) >> *(row+1) >> *(row+2);

		initRate = 2.0;
		timeTaken = 0;
		bool change = true;
		while(change){
			if(*(row+2)>*(row+0)){
				
				double nochangeTime = *(row+2)/initRate;
				double changeTime = *(row+0)/initRate + *(row+2)/(initRate+*(row+1));
				if(nochangeTime <= changeTime){
					initRate = initRate;
					timeTaken = timeTaken+*(row+2)/initRate;
					change = false;
				}else{

					timeTaken = timeTaken + *(row+0)/initRate;
					initRate = initRate + *(row+1);
					change = true;
				}
			}else{
				timeTaken = *(row+2)/initRate;
				change = false;
			}

		}
		
		stringstream ss;
		ss << std::fixed << std::setprecision(std::numeric_limits<double>::digits10) << timeTaken;
        
		caseString.append(ss.str());

		fileOut << "Case #" << i+1 << ": " << caseString << "\n"; 
		caseString = "";
		
		free(row);
		
		
		

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






