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
	ifstream file("A-small-attempt0.in", std::ifstream::in);

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
	
	int *row2;
	int *row;
	int finalPos;
	int initPos;
	int numCard;
	int j;
	for(int i=0;i<numCases;i++){
		getline(file,line);
		string caseString;
		caseString = "";
		std::istringstream(line) >> initPos;
		printf("\n initPos %d", initPos);
		row = (int *) malloc(4*sizeof(int));
		row2 = (int *) malloc(4*sizeof(int));
		
		std::stringstream lineStream(line);
		std::string cell;

		for(j=0;j<initPos;j++){

			getline(file,line);
			
			
			//cout << "\n here is the " << j << "th number " << *(bookShelf+j) << "\n";


		}
		
		
			istringstream(line) >> *(row+0) >> *(row+1) >> *(row+2) >> *(row+3);
			printf("\n");
		for(int k = 0; k < 4; k++){	
			printf("%d ", *(row+k));
		}
	
		for(j=initPos;j<4;j++){
			getline(file,line);
			
			//cout << "\n here is the " << j << "th number " << *(bookShelf+j) << "\n";


		}
		getline(file,line);
		istringstream(line) >> finalPos;

		printf("\n final Pos %d", finalPos);
		

		for(j=0;j<finalPos;j++){

			getline(file,line);
			
			
			//cout << "\n here is the " << j << "th number " << *(bookShelf+j) << "\n";


		}
		
		
		istringstream(line) >> *(row2+0) >> *(row2+1) >> *(row2+2) >> *(row2+3);
		printf("\n");
		for(int k = 0; k < 4; k++){
			printf("%d ", *(row2+k));
		}

		for(j=finalPos;j<4;j++){
			getline(file,line);
			
			//cout << "\n here is the " << j << "th number " << *(bookShelf+j) << "\n";


		}
		numCard = 0;
		int rowResult[4];
		for(int k = 0; k < 4;k++){
			for(int m = 0;m<4;m++){
				*(rowResult + k) = *(row + k ) - *(row2 + m );
				if(*(rowResult + k) == 0 && numCard == 0){
					numCard = *(row2 + m );
				
				}else if(*(rowResult + k) == 0 && numCard > 0){
					numCard = -1;
					break;
				}
			}
		}
		if(numCard == 0){
			caseString.append("Volunteer cheated!");
		}else if(numCard == -1){
			caseString.append("Bad magician!");
		}else{
			stringstream ss;
			ss << numCard;
			caseString.append(ss.str());
		}
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






