
#include "stdafx.h"
#include <cstdio>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string CR, JR;
int N;
long long dd;

void d(string cc, string jj, int l, int cmp) {
	if (l == N) {
		long long cl, jl;
		sscanf(cc.c_str(), "%lld", &cl);
		sscanf(jj.c_str(), "%lld", &jl);
		if (abs(cl - jl) < dd || (abs(cl - jl) == dd && (cc<CR || (cc==CR && jj<JR)))) {
			dd = abs(cl - jl);
			CR = cc;
			JR = jj;
		}
		return;
	}
	if (cc[l] != '?' && jj[l] != '?') {
		if (cc[l] < jj[l] && cmp == 0) {
			cmp = -1;
		}
		else if (cc[l] > jj[l] && cmp == 0) {
			cmp = 1;
		}
		d(cc, jj, l + 1, cmp);
	}
	else if (cc[l] == '?' && jj[l] != '?') {
		if (cmp == 0) {
			cc[l] = jj[l];
			d(cc, jj, l + 1, 0);
			if (jj[l] != '0') {
				cc[l] = jj[l] - 1;
				d(cc, jj, l + 1, -1);
			}
			if (jj[l] != '9') {
				cc[l] = jj[l] + 1;
				d(cc, jj, l + 1, 1);
			}
		}
		else if (cmp == -1) {
			cc[l] = '9';
			d(cc, jj, l + 1, cmp);
		}
		else if (cmp == 1) {
			cc[l] = '0';
			d(cc, jj, l + 1, cmp);
		}
	}
	else if (cc[l] != '?' && jj[l] == '?') {
		if (cmp == 0) {
			jj[l] = cc[l];
			d(cc, jj, l + 1, 0);
			if (cc[l] != '0') {
				jj[l] = cc[l] - 1;
				d(cc, jj, l + 1, 1);
			}
			if (cc[l] != '9') {
				jj[l] = cc[l] + 1;
				d(cc, jj, l + 1, -1);
			}
		}
		else if (cmp == -1) {
			jj[l] = '0';
			d(cc, jj, l + 1, cmp);
		}
		else if (cmp == 1) {
			jj[l] = '9';
			d(cc, jj, l + 1, cmp);
		}
	}
	else {
		if (cmp == 0) {
			jj[l] = cc[l] = '0';
			d(cc, jj, l + 1, 0);

			jj[l] = '1';
			cc[l] = '0';
			d(cc, jj, l + 1, -1);

			jj[l] = '0';
			cc[l] = '1';
			d(cc, jj, l + 1, 1);
		}
		else if (cmp == -1) {
			cc[l] = '9';
			jj[l] = '0';
			d(cc, jj, l + 1, cmp);
		}
		else {
			cc[l] = '0';
			jj[l] = '9';
			d(cc, jj, l + 1, cmp);
		}
	}
}

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\ravill\\Documents\\Algo\\B-large.in");
	fout.open("C:\\Users\\ravill\\Documents\\Algo\\B-large.out");
	int T;
	fin >> T;

	for (int ccnt = 1; ccnt <= T; ccnt++) {
		char c[20], j[20];
		fin >> c >> j;
		N = strlen(c);
		dd = 1111111111111111111LL;
		CR = JR = "";
		d(c, j, 0, 0);
		d(c, j, 0, -1);
		d(c, j, 0, 1);
		assert(CR.length() <= 18);
		cout << "Case #" << ccnt << ": " << CR <<" " << JR<< endl;
		fout << "Case #" << ccnt << ": " << CR << " " << JR << endl;
	}
	return 0;
}

