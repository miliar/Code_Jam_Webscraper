
#include "stdafx.h"
#include <cstdio>
#include <cassert>
#include <fstream>
#include <iostream>
using namespace std;

int g(int N) {
	int v = 0, v1 = (1 << 10) - 1;
	for (int i = 1; i <= 100; i ++) {
		int n = N*i;
		while (n) {
			v |= 1 << (n % 10);
			n /= 10;
		}
		if (v == v1)
			return N*i;
	}
	return -1;
}

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\ravill\\Documents\\Algo\\A-large.in");
	fout.open("C:\\Users\\ravill\\Documents\\Algo\\A-large.out");
	int T;
	fin >> T;
	for (int ccnt = 1; ccnt <= T; ccnt++) {
		int N;
		fin >> N;
		int ret = g(N);
		if (ret < 0) {
			assert(N == 0);
			cout << "Case #" << ccnt << ": " << "INSOMNIA" << endl;
			fout << "Case #" << ccnt << ": " << "INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << ccnt << ": " << ret << endl;
			fout << "Case #" << ccnt << ": " << ret << endl;
		}
	}
	return 0;
}

