
#include "stdafx.h"
#include <cstdio>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\ravill\\Documents\\Algo\\B-large.in");
	fout.open("C:\\Users\\ravill\\Documents\\Algo\\B-large.out");
	int T;
	fin >> T;
	for (int ccnt = 1; ccnt <= T; ccnt++) {
		int A[2502];
		memset(A, 0, sizeof(A));
		int N;
		fin >> N;
		for (int i = 0; i < (2 * N - 1)*N; i++) {
			int x;
			fin >> x;
			A[x]++;
		}
		vector<int> ret;
		for (int i = 0; i < 2501; i++) {
			if (A[i] > 0 && A[i] % 2 == 1) {
				ret.push_back(i);
			}
		}
		sort(ret.begin(), ret.end());
		
		cout << "Case #" << ccnt << ": ";
		fout << "Case #" << ccnt << ": ";

		for (int i = 0; i < ret.size(); i++) {
			cout << ret[i] << " ";
			fout << ret[i] << " ";
		}
		cout << endl;
		fout << endl;
	}
	return 0;
}

