//============================================================================
// Name        : roundOneBFirst.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

const string digitStr[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool checkFinishing(bool* flag, int strLen){
	bool flagAll = true;
	for(int i = 0; i < strLen; i++){
		flagAll = flagAll && flag[i];
	}
	return flagAll;
}

int firstUpdateEachChar(char input, int idx, const string& lineStrings, bool * flag, int strLen){
	if(flag[idx] == true) //has been marked
		return -1;

	bool* flagTmp = new bool[strLen];//flag for all the character
	for(int i = 0; i < strLen; i++){
		flagTmp[i] = flag[i];
	}

	map<char, int> firstMap;
	firstMap['Z'] = 0;
	firstMap['W'] = 2;
	firstMap['U'] = 4;
	firstMap['X'] = 6;
	firstMap['G'] = 8;

	int returnValue = -1;
	bool tmp = false;//not found
	if(firstMap.count(input) > 0 ) //exist
	{
		string numberStr = digitStr[firstMap[input]];
		for(int i = 0; i < numberStr.length(); ++i){
			tmp = false; //not found
			for(int j = 0; j < strLen; ++j){
				if(numberStr[i] == lineStrings[j] && flagTmp[j] == false){
					flagTmp[j] = true; //marked
					tmp = true;
					break;
				}
			}
			if(!tmp){ //not found
				cout<<"not found!!!"<<endl;
				break;
			}
		}

	}

	if(tmp)//found
	{
		returnValue = firstMap[input];
		for(int i = 0; i < strLen; i++){
			flag[i] = flagTmp[i];
		}
	}

	delete []flagTmp;
	return returnValue;
}

int secondUpdateEachChar(char input, int idx, const string& lineStrings, bool * flag, int strLen){
	if(flag[idx] == true) //has been marked
		return -1;

	bool* flagTmp = new bool[strLen];//flag for all the character
	for(int i = 0; i < strLen; i++){
		flagTmp[i] = flag[i];
	}

	map<char, int> firstMap;
	firstMap['F'] = 5;
	firstMap['O'] = 1;
	firstMap['T'] = 3;
	firstMap['S'] = 7;


	int returnValue = -1;
	bool tmp = false;//not found
	if(firstMap.count(input) > 0 ) //exist
	{
		string numberStr = digitStr[firstMap[input]];
		for(int i = 0; i < numberStr.length(); ++i){
			tmp = false; //not found
			for(int j = 0; j < strLen; ++j){
				if(numberStr[i] == lineStrings[j] && flagTmp[j] == false){
					flagTmp[j] = true; //marked
					tmp = true;
					break;
				}
			}
			if(!tmp){ //not found
				cout<<"not found!!!"<<endl;
				break;
			}
		}

	}

	if(tmp)//found
	{
		returnValue = firstMap[input];
		for(int i = 0; i < strLen; i++){
			flag[i] = flagTmp[i];
		}
	}

	delete []flagTmp;
	return returnValue;
}

int thirdUpdateEachChar(char input, int idx, const string& lineStrings, bool * flag, int strLen){
	if(flag[idx] == true) //has been marked
		return -1;

	bool* flagTmp = new bool[strLen];//flag for all the character
	for(int i = 0; i < strLen; i++){
		flagTmp[i] = flag[i];
	}

	map<char, int> firstMap;
	firstMap['I'] = 9;

	int returnValue = -1;
	bool tmp = false;//not found
	if(firstMap.count(input) > 0 ) //exist
	{
		string numberStr = digitStr[firstMap[input]];
		for(int i = 0; i < numberStr.length(); ++i){
			tmp = false; //not found
			for(int j = 0; j < strLen; ++j){
				if(numberStr[i] == lineStrings[j] && flagTmp[j] == false){
					flagTmp[j] = true; //marked
					tmp = true;
					break;
				}
			}
			if(!tmp){ //not found
				cout<<"not found!!!"<<endl;
				break;
			}
		}

	}

	if(tmp)//found
	{
		returnValue = firstMap[input];
		for(int i = 0; i < strLen; i++){
			flag[i] = flagTmp[i];
		}
	}

	delete []flagTmp;
	return returnValue;
}

vector<int> getAllDigits(const string& lineStrings){
	int strLen = lineStrings.length();
	bool* flag = new bool[strLen];//flag for all the character
	for(int i = 0; i < strLen; i++){
		flag[i] = false;
	}

	vector<int> allDigits;
	bool finishFlag = checkFinishing(flag, strLen);
	if(!finishFlag){
		for(int i = 0; i < strLen; i++){
			char input = lineStrings[i];
			int digit = firstUpdateEachChar(input, i, lineStrings, flag, strLen);
			if(digit != -1){
				allDigits.push_back(digit);
			}
		}

		finishFlag = checkFinishing(flag, strLen);
		if(!finishFlag){
			for(int i = 0; i < strLen; i++){
				char input = lineStrings[i];
				int digit = secondUpdateEachChar(input, i, lineStrings, flag, strLen);
				if(digit != -1){
					allDigits.push_back(digit);
				}
			}

		}

		finishFlag = checkFinishing(flag, strLen);
		if(!finishFlag){
			for(int i = 0; i < strLen; i++){
				char input = lineStrings[i];
				int digit = thirdUpdateEachChar(input, i, lineStrings, flag, strLen);
				if(digit != -1){
					allDigits.push_back(digit);
				}
			}
		}
	}

	sort(allDigits.begin(), allDigits.end());

	delete []flag;
	return allDigits;
}


int main(){
	int N = -1;

	string tmpN = "";
	getline(cin, tmpN);
	N = stoi(tmpN,nullptr,10);//convert string to integer

	for(int i = 0; i < N; ++i){
		string lineOfCharacters;
		getline(cin, lineOfCharacters);
		vector<int> allDigits = getAllDigits(lineOfCharacters);
		cout<<"Case #"<<(i+1)<<": ";
		for(vector<int>::iterator it = allDigits.begin(); it != allDigits.end(); ++it){
			cout<< *it;
		}
		cout<<endl;
	}

	return 0;
}
