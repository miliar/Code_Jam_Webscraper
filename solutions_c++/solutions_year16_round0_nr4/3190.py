// Fractiles.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#define ull unsigned long long int

#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
using namespace std;

ull mypow(int k, int c) {
	if (c <= 0) {
		return 0;
	}
	ull ret = 1;
	if (c == 1) {
		return k;
	}
	if (k & 1 == 0) {
		ret = mypow(k, c/2);
		ret = ret*ret;
	}
	else {
		ret = mypow(k, c/2);
		ret = ret*ret*k;
	}
	return ret;
}

int main()
{
	ifstream in("D-small-attempt2.in");
	streambuf *cinbuf = cin.rdbuf();
	cin.rdbuf(in.rdbuf());

	ofstream out("D-small-attempt2.out");
	streambuf *coutbuf = cout.rdbuf();
	cout.rdbuf(out.rdbuf());


	int t;
	cin >> t;
	int k, c, s;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ":";
		cin >> k >> c >> s;
		// 需要计算出k从0到c-1的所有次数用于做累加
		ull* powerTbl = new ull[c];
		powerTbl[0] = 0;
		if (c > 1) {
			powerTbl[1] = k;
		}
		for (int j = 2; j <= c - 1; j++) {
			powerTbl[j] = powerTbl[j - 1] * k;
		}
		/*ull kpowercMinus2 = mypow(k, c-2);
		ull kpowercMinus1 = kpowercMinus1*k;*/
		//ull integral1 = 0,integral2=0;

		ull* integralTbl = new ull[c];
		for (int j = 0; j < c; j++) {
			integralTbl[j] = 0;
		}

		for (int j = 1; j <= s; j++) {
			ull res = 0;
			for (int k = 0; k < c; k++) {
				res += integralTbl[k];
			}
			res += j;
			cout << " " << res;
			for (int k = 0; k < c; k++) {
				integralTbl[k] += powerTbl[k];
			}
		}
		cout << endl;
		delete[] powerTbl;
		delete[] integralTbl;
	}
	system("pause");
    return 0;
}

