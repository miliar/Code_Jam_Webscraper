// OJ.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"

#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <climits>
#include <cmath>
#include <sstream>
using namespace std;

ifstream in("A-large.in");
ofstream out("A-large.out");
streambuf *cinbuf = cin.rdbuf();
streambuf *coutbuf = cout.rdbuf();

void redirectIO() {
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());
}

void recoverIO() {
	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);
}

//long long int getBase(long long int n) {
//	long long int base = 1;
//	while (n / 10) {
//		base *= 10;
//		n /= 10;
//	}
//	return base;
//}
//
//string LLtoString(long long int n) {
//	stringstream s;
//	s << n;
//	string ret;
//	s >> ret;
//	return ret;
//}
//
//long long int StringtoLL(string str) {
//	stringstream s;
//	s << str;
//	long long int ret;
//	s >> ret;
//	return ret;
//}

// B-large
//int main() {
//	redirectIO();
//	int T;
//	long long int N, base;
//	string str;
//	cin >> T;
//	for (int i = 1; i <= T; ++i) {
//		cin >> N;
//		base = getBase(N);
//		str = LLtoString(N);
//		char last = '1', ch;
//		int invalid = -1;
//		for (int j = 0; j < str.length(); ++j) {
//			if (str[j] < last) {
//				invalid = j - 1;
//				ch = str[j - 1];
//				for (; j < str.length(); ++j) {
//					str[j] = '0';
//				}
//			}
//			last = str[j];
//		}
//		if (invalid != -1) {
//			while (invalid-1 >= 0 && str[invalid-1] == ch) {
//				str[invalid] = '0';
//				--invalid;
//			}
//			cout << "Case #" << i << ": " << StringtoLL(str) - 1 << endl;
//		}
//		else {
//			cout << "Case #" << i << ": " << StringtoLL(str) << endl;
//		}
//		
//	}
//	recoverIO();
//	//system("pause");
//	return 0;
//}

// A-small and A-large
int main() {
	redirectIO();
	int T, K;
	string S;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> S >> K;
		int cnt = 0;
		int slen = S.length();
		for (int j = 0; j <= slen - K; ++j) {
			if (S[j] == '-') {
				++cnt;
				for (int k = 0; k < K; ++k) {
					S[k + j] = (S[k + j] == '+' ? '-' : '+');
				}
			}
		}
		if (S == string(slen, '+')) {
			cout << "Case #" << i << ": " << cnt << endl;
		}
		else {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
	}
	recoverIO();
	//system("pause");
	return 0;
}

// B-small
//bool check(int n) {
//	int base = 1, tmp = n;
//	while (tmp/10) {
//		tmp /= 10;
//		base *= 10;
//	}
//	tmp = n;
//	int last = -1, cur;
//	while (base) {
//		cur = tmp / base;
//		if (cur < last) {
//			return false;
//		}
//		last = cur;
//		tmp %= base;
//		base /= 10;
//	}
//	return true;
//}
//
//int main() {
//	redirectIO();
//	int T, N;
//	cin >> T;
//	for (int i = 1; i <= T; ++i) {
//		cin >> N;
//		while (!check(N)) --N;
//		cout << "Case #" << i << ": " << N << endl;
//	}
//	recoverIO();
//	return 0;
//}