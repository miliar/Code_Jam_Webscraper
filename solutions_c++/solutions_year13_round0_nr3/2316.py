#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>

using namespace std;
#define MAX 105

/* Global variables */
long long a;
long long b;

vector<long long> pList; 	// list of palindrome numbers
/* prototypes */



/*
void nextPalindrome( const char input[], const char output[]){
	
}
*/

bool isPalindrome(long long x){
	char xs[MAX];	// x in string
	sprintf(xs, "%lld", x);
	// determine the length of xs
	int len = 0;
	for(int i=0; ; i++){
		if(xs[i] == '\0'){
			len = i;
			break;
		}
	}
	// see if it is a palindrome
	int rep;
	if(len % 2 == 0){
		rep = len/2;
	} else {
		rep = len/2 + 1;
	}

	
	for(int i=0; i< rep; i++){
		if(xs[i] != xs[len-1 - i]){
			return false;
		} 
	}
	return true;
}

int main(){
	int numCases;
	cin >> numCases;

	// do it for 1 to 10^14 and store the results in a vector

	long long begin = 1;		// 1 to (10^7)^2
	long long end = 10000000;	

	for(long long int x = begin; x <= end; x++){
		if(isPalindrome(x)){
			if(isPalindrome(x*x)){
				pList.push_back(x*x);
				
			}
		}
	}	
	
	pList.push_back(-1);
	// we will print all the vectors
	/*int index=1;
	for(vector<long long>::iterator it = pList.begin(); it != pList.end(); it++){
		cout << "At " << index << "The number is " << (*it) << endl;
			index++;
	}
*/
//	cout << "The 39th element is" << pList[39] << endl;	0
//	cout << "The 40th element is" << pList[40] << endl;	0

	for(int caseN=1; caseN <= numCases; caseN++){
		cin >> a;
		cin >> b;

		// for each case, iterate through the vector and find the number of Fair and Square
		long long numFS = 0;
		for(long long i=0; ; i++){
			if(pList[i] >= a and pList[i] <= b){
				numFS++;	
				//cout << numFS << "The number is" << pList[i] << endl;
			} else if(pList[i] > b or pList[i] < 0){
				break;
			}
		}	


		cout << "Case #" << caseN << ": " <<   numFS <<    endl;
	}
}
