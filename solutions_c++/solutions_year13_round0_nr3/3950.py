/*
 * probC.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: michael
 */
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>

using namespace std;

bool checkIfSquares(int A, int B){
	if ((floor(sqrt(B)) - ceil(sqrt(A))) == 0)
		return false;
	return true;
}

bool isPalindrome(int n){
	char resultStr[20];
	int len = 0;
	sprintf(resultStr,"%i",n);
	len = strlen(resultStr);
	for (int i=0; i<=(len/2); i++){
		if (resultStr[i] != resultStr[len-1-i])
			return false;
	}
	return true;
}

int main(){
	char buffer[20];
	int numCases;

	cin.getline(buffer,20);
	sscanf(buffer,"%i",&numCases);
	for (int i=0; i<numCases; i++){
		memset(buffer, 0, 20);
		cin.getline(buffer,20);
		int A = 0, B = 0, total = 0;
		sscanf(buffer,"%i %i",&A,&B);
		for (int n=ceil(sqrt(A)); n<=floor(sqrt(B)); n++){
			if (isPalindrome(n)){
				int sqr = n*n;
				if (isPalindrome(sqr))
					total++;
			}
		}
		printf("Case #%i: %i\n",i+1,total);
	}

}



