
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
	fin.open("C:\\Users\\ravill\\Documents\\Algo\\D-small-attempt0.in");
	fout.open("C:\\Users\\ravill\\Documents\\Algo\\D-small-attempt0.out");
	int T;
	fin >> T;
	for (int ccnt = 1; ccnt <= T; ccnt++) {
		int K,C,S;
		fin >> K >> C >> S;

		cout << "Case #" << ccnt << ": ";
		fout << "Case #" << ccnt << ": ";
		
		long long p = 1;
		for (int i = 0; i < C - 1; i++) {
			p *= K;
		}
		for (int i = 1; i <= S; i++) {
			cout << i*p << " ";
			fout << i*p << " ";
		}
		cout << endl;
		fout << endl;
	}
	return 0;
}

