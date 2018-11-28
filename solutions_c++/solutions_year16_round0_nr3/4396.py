/*
 * quantifyCMain.cpp
 *
 *  Created on: 9 Apr, 2016
 *      Author: wangyong
 */

#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


int* copyDigitsArray(int *inputDigits, int inputN)
{
	int *tmp = new int[inputN];
	for(int i = 0; i < inputN; i++)
	{
		tmp[i] = inputDigits[i];
	}

	return tmp;
}

int* getNextDigitsArray(int *inputDigits, int inputN)
{
	int *curDigitsArray = copyDigitsArray(inputDigits, inputN);
	for(int i = 1; i < inputN - 1; i++){ //from lowest to highest digits
		if(curDigitsArray[i] == 0){
			curDigitsArray[i] = 1;
			//cout<<"ehhehhe";
			break;
		}
		else if(curDigitsArray[i] == 1 && i < (inputN - 2)){
			curDigitsArray[i] = 0;
		}
		else if(curDigitsArray[i] == 1 && i == (inputN - 2)){
			return NULL;
		}
	}

//	cout<<"next: "<<endl;
//	for(int i = 0; i < inputN; ++i){
//		cout<<curDigitsArray[inputN - 1 - i];
//	}
//	cout<<endl;

	return curDigitsArray;
}

long unsigned int string2IntValue(int *inputDigits, int inputN, int base){
	long unsigned int value = 0;
	for(int i = 0; i < inputN; ++i){
		value += inputDigits[i] * pow(base, i);
	}

	return value;
}



long unsigned int checkIsPrime(long unsigned int inputValue){
	long unsigned int maxIter = (long unsigned int) sqrt(inputValue);
	//cout<<"maxIter: "<<maxIter<<endl;

	for(long unsigned int i = 2; i <= maxIter; i++){
		long unsigned int remainder = inputValue % i;
		if(remainder == 0){
			return i; //return the divider
		}
		else{
			continue;
		}
	}


	return 0;//return 0, indicating that it is a prime.
}



bool checkIsJamcoin(int *inputDigits, int inputN, string& interpretationStr)
{
	//value to string
	interpretationStr = "";
	for(int i = inputN - 1; i >= 0; i--){
//		char *intStr = itoa(inputDigits[i]);
//		string str = string(intStr);
//		interpretationStr += str;
		string str = to_string(inputDigits[i]);
		interpretationStr += str;
	}
	interpretationStr += " ";

	//change string to value and check whether it is prime
	for(int i = 2; i <= 10; ++i){
		long unsigned int value = string2IntValue(inputDigits, inputN, i);
		long unsigned int flag = checkIsPrime(value);
		if(flag == 0){ //this is a prime
			return false; //it is not Jamcoin
		}
		else{
			string str = to_string(flag);
			interpretationStr += str;
			if(i < 10){
				interpretationStr += " ";
			}
		}
	}

	return true;//it is a Jamcoin
}

vector<string> getJamcoin(int inputN, int inputJ, int *inputDigits)
{
	int counter = 0;
	vector<string> vecAllCases;
	int totalNum = pow(2, inputN - 2);

	for(int i = 0; i < totalNum; ++i){
		string interpretationStr = "";
		bool isJamcoin = checkIsJamcoin(inputDigits, inputN, interpretationStr);
		if(isJamcoin){
			vecAllCases.push_back(interpretationStr);
			counter++;
		}

		if(counter >= inputJ){
			break;
		}
		inputDigits = getNextDigitsArray(inputDigits, inputN);
		if(inputDigits == NULL){
			cout<<"##########error#######"<<endl;
		}
	}

	return vecAllCases;
}

int main(){
	int T = -1, N = -1, J = -1;
	cin >> T;


	for(int i = 0; i < T; i++){
		cin >> N;
		cin >> J;
		int* digits = new int[N];
		digits[0] = 1; //lowest
		digits[N-1] = 1;//highest
		for(int i = 1; i <= N-2; i++) //initialize
		{
			digits[i] = 0;
		}

		vector<string> tmpStr = getJamcoin(N, J, digits);
		cout<<"Case #"<<(i+1)<<": " <<endl;
		for (std::vector<string>::iterator it = tmpStr.begin() ; it != tmpStr.end(); ++it)
		{
			cout << *it<< endl;
		}

		delete []digits;
	}

	return 0;
}



