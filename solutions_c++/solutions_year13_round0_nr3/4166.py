//============================================================================
// Name        : Test.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>

using namespace std;

int winCase[10][4] = {
		{0, 1, 2, 3},
		{4, 5, 6, 7},
		{8, 9, 10, 11},
		{12, 13, 14, 15},
		{0, 4, 8, 12},
		{1, 5, 9, 13},
		{2, 6, 10, 14},
		{3, 7, 11, 15},
		{0, 5, 10, 15},
		{3, 6, 9, 12}
};

void func_for_Problem1(int nCases) {
	string srcStr;
	string retStr;

	for(int i = 0; i < nCases; i++) {
		char x[17];
		char o[17];

		getline(cin, srcStr); retStr.append(srcStr);
		getline(cin, srcStr); retStr.append(srcStr);
		getline(cin, srcStr); retStr.append(srcStr);
		getline(cin, srcStr); retStr.append(srcStr);
		getline(cin, srcStr);

		for(int j = 0; j < 16;j++) {
			if(retStr[j] == 'T') {
				x[j] = 'X';
				o[j] = 'O';
			} else {
				x[j] = o[j] = retStr[j];
			}
		}
		x[16] = 0;
		o[16] = 0;

		// 1: X won
		// 2: O won
		// 3: Draw
		// 4: Game has not completed
		int result = 0;
		int ax = 0;
		int ao = 0;
		int isFull = 1;
		for(int k = 0; k < 10; k++) {
			ax = ao = 0;
			for(int l = 0; l < 16; l++) {
				if(x[l] == '.') {
					isFull = 0;
					break;
				}
			}

			for(int l = 0; l < 4; l++) {
				if(x[winCase[k][l]] == 'X') {
					ax++;
				}

				if(o[winCase[k][l]] == 'O') {
					ao++;
				}
			}

			if(ax == 4) {
				result = 1;
				break;
			} else if(ao == 4) {
				result = 2;
				break;
			}
		}

		if(result == 0) {
			if(isFull == 1) {
				result = 3;
			} else {
				result = 4;
			}
		}
		// check x win

		cout << "Case #" << (i+1);
		switch(result) {
		case 1:
			cout << ": X won" << endl;
			break;
		case 2:
			cout << ": O won" << endl;
			break;
		case 3:
			cout << ": Draw" << endl;
			break;
		case 4:
			cout << ": Game has not completed" << endl;
			break;
		case 0:
		default:
			break;
		}
		//cout << "Case #" << (i+1) << ": " << x << endl;
		//cout << "Case #" << (i+1) << ": " << o << endl;
		retStr.clear();
	}
}

char faircase[][256] = {
		"1",// 1
		"4",// 2
		"9",// 3
		"121",// 11
		"484",// 22
		"10201",// 101
		"12321",// 111
		"14641",// 121
		"40804",// 202
		"44944",// 212
		"1002001",// 1001
		"1234321",// 1111
		"4008004",// 2002
		"100020001",// 10001
		"102030201",// 10101
		"104060401",// 10201
		"121242121",// 11011
		"123454321",// 11111
		"125686521",// 11211
		"400080004",// 20002
		"404090404",// 20102
		"10000200001",// 100001
		"10221412201",// 101101
		"12102420121",// 110011
		"12345654321",// 111111
		"40000800004",// 200002
		"1000002000001",// 1000001
		"1002003002001",// 1001001
		"1004006004001",// 1002001
		"1020304030201",// 1010101
		"1022325232201",// 1011101
		"1024348434201",// 1012101
		"1210024200121",// 1100011
		"1212225222121",// 1101011
		"1214428244121",// 1102011
		"1232346432321",// 1110111
		"1234567654321",// 1111111
		"4000008000004",// 2000002
		"4004009004004",// 2001002
		"100000020000001",// 10000001
		"100220141022001",// 10011001
		"102012040210201",// 10100101
		"102234363432201",// 10111101
		"121000242000121",// 11000011
		"121242363242121",// 11011011
		"123212464212321",// 11100111
		"123456787654321",// 11111111
		"400000080000004",// 20000002
};

void func_for_Problem3(int nCases) {
	string srcStr;
	string dstStr;

	for(int i = 0; i < nCases; i++) {
		string fromStr, toStr;
		double from = 0, to = 0;
		int result = 0;
		cin >> fromStr;
		cin >> toStr;

		from = atof(fromStr.c_str());
		to = atof(toStr.c_str());
#if 1
		for(unsigned int k = 0; k < sizeof(faircase)/sizeof(faircase[0]); k++) {
			if(from <= atof(faircase[k]) && to >= atof(faircase[k]))
					result++;
		}
#else
		if(fromStr.length() <= 4 && toStr.length() <= 4) {
			// process it with integer
			// 4, 9, 121, 484

			if(from <= 1 && to >= 1)
				result++;
			if(from <= 4 && to >= 4)
				result++;
			if(from <= 9 && to >= 9)
				result++;
			if(from <= 121 && to >= 121)
				result++;
			if(from <= 484 && to >= 484)
				result++;
		}
#endif
		cout << "Case #" << (i+1) << ": " << result << endl;
	}
}

inline bool isPelindrome(char* a) {
	int lens = strlen(a);
	bool isPelindrome = true;
	for(int k = 0; k < lens/2; k++) {
		if(a[k] != a[lens-k-1]) {
			isPelindrome = 0;
			break;
		}
	}

	return isPelindrome;
}

int main(int argc, char* argv[]) {
	int nCases = 0;
	string srcStr;
/*
	char szSquare[256];
	char szNum[256];
	for(double i = 1; i < 100000000; i = i + 1) {
		sprintf(szNum, "%1.0f", i);
		if(isPelindrome(szNum)) {
			sprintf(szSquare, "%1.0f", i*i);
			if(isPelindrome(szSquare)) {
				printf("\"%1.0f\",// %1.0f\n", i*i, i);
			}
		}
	}
*/
	freopen("D:/GCJ2013/20130413/Problem3/C-large-1.in", "rt", stdin);
	freopen("D:/GCJ2013/20130413/Problem3/C-large-1.out", "wt", stdout);

	getline(cin, srcStr);
	nCases = atoi(srcStr.c_str());

	//func_for_Problem1(nCases);
	func_for_Problem3(nCases);

	return 0;
}
