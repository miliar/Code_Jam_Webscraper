/*
 * main.cpp
 *
 *  Created on: 9 Apr, 2016
 *      Author: wangyong
 */

#include <iostream>

using namespace std;
const int digitArrayLen = 10;

bool checkFlags(bool *flag){
	bool allFlag = true;
	for(int i = 0; i < digitArrayLen; i++){
		allFlag = allFlag && flag[i];
	}

	return allFlag;
}

bool recordDigits(int input, bool *flag){
//	int counter = 0;//the first time
	bool allFlag = false;

	do {
	    int digit = input % 10;
//	    if(counter == 0 && digit == 0){
//	    	flag[0] = true;
//	    }
	    flag[digit] = true;
	    bool curFlag = checkFlags(flag);
	    if(curFlag){
	    	allFlag = curFlag;
	    	break;
	    }

	    input /= 10;
//	    counter++;
	} while (input > 0);

	return allFlag;
}

int main(){
	//cout<<"hello world"<<endl;
	int N = 0,T = -1, lastNum = -1;
	int counter = 0, maxIter = 10000;

	cin>> N;
	for(int i = 0; i < N; ++i){
		cin>> T;
		bool* flag = new bool[digitArrayLen];
		bool finishOrNot = false;
		for(int j = 0; j < digitArrayLen; j++){
			flag[j] = false;
		}

		counter = 0;
		do{
			counter++;
			int tmp = T * counter;
			finishOrNot = recordDigits(tmp, flag);
			if(finishOrNot){
				cout<<"Case #"<<(i+1)<<": "<< tmp <<endl;
			}
			//cout<< tmp<<endl;

			if(counter > maxIter){
				cout<<"Case #"<<(i+1)<<": "<< "INSOMNIA" <<endl;
				break;
			}
		}while(!finishOrNot);

	}

	return 0;
}



