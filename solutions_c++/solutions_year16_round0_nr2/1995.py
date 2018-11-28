
#include "stdafx.h"
#include <cstdio>
#include <cassert>
#include <fstream>
#include <iostream>
using namespace std;

int g(char *s) {
	int l = strlen(s) - 1;
	int ret = 0;
	while (l >= 0 && s[l] == '+')
		l--;

	char prev = '.';
	for (int i = l; i >= 0; i--) {
		if (s[i] != prev) {
			prev = s[i];
			ret++;
		}
	}
	return ret;
}

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\ravill\\Documents\\Algo\\B-large.in");
	fout.open("C:\\Users\\ravill\\Documents\\Algo\\B-large.out");
	int T;
	fin >> T;
	for (int ccnt = 1; ccnt <= T; ccnt++) {
		char s[102];
		fin >> s;
		int ret = g(s);
		cout << "Case #" << ccnt << ": " << ret << endl;
		fout << "Case #" << ccnt << ": " << ret << endl;
	}
	return 0;
}

