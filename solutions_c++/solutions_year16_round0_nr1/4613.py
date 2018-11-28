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
		bool allSeen = false;
		bool seen[10] = { 0 };
		int N;
		cin >> N;
		if (N == 0){
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		int multiplier = 0;
		while (!allSeen){
			multiplier++;
			int temp = multiplier*N;
			while (temp != 0){
				int digit = temp % 10;
				temp = temp / 10;
				seen[digit] = true;
			}
			allSeen = seen[0] & seen[1] & seen[2] & seen[3] & seen[4] & seen[5] & seen[6] & seen[7] & seen[8] & seen[9];
		}
		cout << "Case #" << i << ": " << multiplier*N;
		if (i != T){
			cout << endl;
		}
	}
	cin >> T;
	return 0;
}

