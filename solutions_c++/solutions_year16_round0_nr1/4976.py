#include <iostream>
#include <cassert>
#include <fstream>
#include <sstream>
#include <math.h>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <time.h>
#include <stdio.h>
#include <direct.h>
#include <windows.h>
#include <mutex>
#include <process.h>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define POW(n) (n*n)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned char CharactorID;
typedef unsigned char Space;
typedef unsigned char sPos;
typedef short Pos;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<unsigned long long> vull;

int T;

bool chk(bool list[10]) {
	REP(i, 10) {
		if (!list[i]) {
			return false;
		}
	}
	return true;
}

void set(bool list[10], const ll& N) {
	string str = to_string(N);

	int length = str.length();
	REP(i, length) {
		int n = str[i] - '0';
		list[n] = true;
	}
}

ll loop(const ll& N) {
	//unordered_map<ll, bool> map;

	bool list[10] = {};

	for (int i = 1; i < 100000; ++i) {
		ll _N = N*i;
		set(list, _N);
		if (chk(list))return _N;
	}

	return -1;
}

int main() {
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		ll N;
		cin >> N;

		if (N == 0) {
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}
		else {
			ll n = loop(N);
			if (n == -1) {
				cout << "Case #" << t << ": INSOMNIA" << endl;
			}
			else {
				cout << "Case #" << t << ": " << n << endl;
			}
		}
	}

	return 0;
}