// Revenge of the Pancakes.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

int main()
{
	ifstream in("B-large.in");
	streambuf *cinbuf = cin.rdbuf();
	cin.rdbuf(in.rdbuf());

	ofstream out("B-large.out");
	streambuf *coutbuf = cout.rdbuf();
	cout.rdbuf(out.rdbuf());

	int t;
	cin >> t;
	string str;
	for (int i = 1; i <= t; i++) {
		cin >> str;
		int slen = str.length();
		int curPlus = 0;
		int curCnt = 0;
		for (int j = 0; j < slen;) {
			if (str[j] == '+') {
				curPlus++;
				j++;
			}
			else {
				int off = 1;
				while ((j + off) < slen&&str[j + off] == '-') {
					off++;
				}
				if (curPlus > 0) {
					curCnt += 2;
				}
				else {
					curCnt++;
				}
				j += off;
			}

		}
		cout << "Case #" << i << ": " << curCnt << endl;
	}
	system("pause");
    return 0;
}

