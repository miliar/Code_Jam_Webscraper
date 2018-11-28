// QuestionA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++){
		string S;
		cin >> S;
		int counter = 0;
		for (int i = 0; i < S.length()-1; i++){
			char first = S[i];
			char second = S[i + 1];
			if (first != second){
				counter++;
			}
		}
		if (S[S.length() - 1] == '-'){
			counter++;
		}
		cout << "Case #" << i << ": " << counter;
		if (i != T){
			cout << endl;
		}
	}
	return 0;
}

