/*
 * main.cpp
 *
 *  Created on: 9 Apr, 2016
 *      Author: wangyong
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int findLastMinusIndex(string inputStr){
	unsigned int strLen = inputStr.length();
	for(int i = strLen - 1; i >= 0; i--){
		if(inputStr[i] == '-'){
			return i;
		}
	}

	return -1;//indicate that job is done
}

int findFirstSeqMinusIndex(string inputStr, int idxOfLastMinus){
	int firstSeqMinusIdx = idxOfLastMinus;

	for(int i = idxOfLastMinus -1; i >= 0; i--){
		if(inputStr[i] == '-'){
			firstSeqMinusIdx = i;
		}
		else{
			break;
		}
	}

	return firstSeqMinusIdx;
}

string flipAllChars(string input, int idxLastMinus){
	string tmp = "";
	for(int i = 0; i <= idxLastMinus; ++i){
		char pushValue = input[i] == '+' ? '-' : '+';
		tmp.push_back(pushValue);
	}

	for(int i = 0; i <= idxLastMinus; ++i){
		input[idxLastMinus-i] = tmp[i];
	}

	return input;
}

int flip(string input){
	int counter = 0;
	unsigned int strLen = input.length();

	int idxOfLastMinus = findLastMinusIndex(input);
	while(idxOfLastMinus != -1){
		bool firstCharIsMinus = input[0] == '-';
		if(firstCharIsMinus){
			input = flipAllChars(input, idxOfLastMinus);
		}
		else{
			int firstSeqMinusIndex = findFirstSeqMinusIndex(input,idxOfLastMinus);
			input = flipAllChars(input, firstSeqMinusIndex-1);
		}

		counter++;
		idxOfLastMinus = findLastMinusIndex(input);
	}

	return counter;
}


int main(){
	int N = -1;

	string tmpN = "";
	getline(cin, tmpN);
	N = stoi(tmpN,nullptr,10);//convert string to integer

	for(int i = 0; i < N; ++i){
		string lineOfCharacters;
		getline(cin, lineOfCharacters);
		int counter = flip(lineOfCharacters);
		cout<<"Case #"<<(i+1)<<": "<< counter <<endl;
	}

	return 0;
}

