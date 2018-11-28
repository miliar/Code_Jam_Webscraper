
#include "stdafx.h"
#include <cstdio>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;


int main() {
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\ravill\\Documents\\Algo\\A-large.in");
	fout.open("C:\\Users\\ravill\\Documents\\Algo\\A-large.out");
	int T;
	fin >> T;
	for (int ccnt = 1; ccnt <= T; ccnt++) {
		char S[1002];
		fin >> S;

		
		int n = strlen(S);
		string r = "" + string(1, S[0]);
		for (int i = 1; i < n; i++) {
			if (S[i] >= r[0]) {
				r = string(1, S[i]) + r;
			}
			else {
				r = r + string(1, S[i]);
			}
		}
		cout << "Case #" << ccnt << ": " << r << endl;
		fout << "Case #" << ccnt << ": " << r << endl;
	}
	return 0;
}

