
#include "stdafx.h"
#include <cstdio>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> g(int N, int J) {
	vector<string> ret;
	int sz = 0;
	for (int i = 0; i < (1 << (N-2)); i++) {
		int c[2] = { 0, 0 };
		string s = "";
		for (int j = 0; j < N -2; j++) {
			if ((1 << j) & i) {
				(c[j % 2]++);
				s = "1" + s;
			}
			else {
				s = "0" + s;
			}
		}
		if (c[0] == c[1]) {
			s = "1" + s + "1";
			ret.push_back(s);
			sz++;
			if (sz == J) {
				break;
			}
		}
	}
	return ret;
}

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\ravill\\Documents\\Algo\\C-large.in");
	fout.open("C:\\Users\\ravill\\Documents\\Algo\\C-large.out");
	int T;
	fin >> T;
	for (int ccnt = 1; ccnt <= T; ccnt++) {
		int N, J;
		fin >> N >> J;
		vector<string> ret = g(N,J);
		cout << "Case #" << ccnt << ":" << endl;
		fout << "Case #" << ccnt << ":" << endl;
		for (int i = 0; i < J; i++) {
			cout << ret[i] << " 3 4 5 6 7 8 9 10 11" << endl;
			fout << ret[i] << " 3 4 5 6 7 8 9 10 11" << endl;
		}

	}
	return 0;
}

