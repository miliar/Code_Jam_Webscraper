// CountingSheep.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <bitset>
#include <fstream>
using namespace std;

int getMask() {
	int bits = 0xffffffff;
	bits = bits << 10;
	bits = ~bits;
	return bits;
}

int main()
{
	//输入输出重定向
	ifstream in("A-small-attempt1.in");
	streambuf *cinbuf = cin.rdbuf();			//save old buf
	cin.rdbuf(in.rdbuf());
	ofstream out("A-small-attempt1.out");
	streambuf *coutbuf = cout.rdbuf();			//save old buf
	cout.rdbuf(out.rdbuf());

	int mask = getMask();
	//cout << bitset<sizeof(int) * 8>(mask) << endl;
	int res[201];
	memset(res, -1, sizeof(res));
	for (int i = 1; i <= 200; i++) {
		int mask = getMask();
		int cur = i;
		int off = 1;
		while (mask) {
			cur = i*off;
			char strbuf[256] = { 0 };
			sprintf_s(strbuf, "%d", cur);
			//printf("%s\n", strbuf);
			int slen = strlen(strbuf);
			for (int j = 0; j < slen; j++) {
				int curNum = strbuf[j] - '0';
				int curBit = 1 << curNum;
				if (mask&curBit) {
					mask = mask - curBit;
				}
			}
			off++;
		}
		//cout <<i<<":"<< cur << endl;
		res[i] = cur;
	}
	int t;
	cin >> t;
	int n;
	for (int i = 1; i <= t; i++) {
		cin >> n;
		if (res[n] < 0) {
			cout <<"Case #"<<i<<": INSOMNIA" << endl;
		}
		else {
			cout <<"Case #"<<i<<": "<< res[n] << endl;
		}
	}
	//system("pause");
    return 0;
}

