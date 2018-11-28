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

int tbl[26] = {
		0, //a
		1, //b
		1, //c
		1, //d
		0, //e
		1, //f
		1, //g
		1, //h
		0, //i
		1, //j
		1, //k
		1, //l
		1, //m
		1, //n
		0, //o
		1, //p
		1, //q
		1, //r
		1, //s
		1, //t
		0, //u
		1, //v
		1, //w
		1, //x
		1, //y
		1, //z
};

int is_ok(const char* str, int lim, int len) {
	int count = 0;

	/*
	char* tst = (char*)malloc(len+1);
	memcpy(tst, str, len);
	tst[len] = 0;

	cout << tst << endl;
	*/
	for(int k = 0; k < len; k++) {
		if(tbl[str[k]-'a']) {
			count++;
		} else {
			count = 0;
		}

		if(count >= lim) {
			return 1;
		}
	}

	return 0;
}

void func_for_Problem1(int nCases) {
	string srcStr;
	string dstStr;

	for(int i = 0; i < nCases; i++) {
		string strname, strvalue;
		int result = 0;
		int lens = 0;
		int lim = 0;

		cin >> strname;
		cin >> strvalue;

		lens = strlen(strname.c_str());
		lim = atoi(strvalue.c_str());

		for(int offs = 0; offs < lens + 1 - lim; offs++) {
			for(int len = lim; len < lens + 1 - offs; len++) {
				if(is_ok(strname.c_str() + offs, lim, len)) {
					result++;
				}
			}
		}

		cout << "Case #" << (i+1) << ": " << result << endl;
	}
}

int main(int argc, char* argv[]) {
	int nCases = 0;
	string srcStr;

	freopen("D:/GCJ2013/20130512/P1/A-small-attempt0.in", "rt", stdin);
	freopen("D:/GCJ2013/20130512/P1/A-small-attempt0.out", "wt", stdout);

	getline(cin, srcStr);
	nCases = atoi(srcStr.c_str());

	func_for_Problem1(nCases);

	return 0;
}
