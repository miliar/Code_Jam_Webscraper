#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <complex>
#include <vector>
using namespace std;
bool check(vector<bool> a);


int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	for (int q = 0; q < T; q++) {
		int x;
		fin >> x;
		vector<bool> digits(10);
		for (int i = 0; i < 10; i++) {
			digits[i] = false;
		}
		if (x == 0) {
			fout << "Case #" << q + 1 << ":" << " INSOMNIA" << endl;
			continue;
		}
		int p = 1;
		while (check(digits) == false) {
			int y = p*x;
			int z = log10(y);
			for (int p = 0; p <= z; p++) {
				digits[y % 10] = true;
				y = (y - (y % 10)) / 10;

			}
			p++;
		}
		fout << "Case #" << q + 1 << ": " << x*(p-1) << endl;

	}
    return 0;
}

bool check(vector<bool> a) {
	for (int i = 0; i < a.size(); i++) {
		if (a[i] == false) {
			return false;
		}
	}
	return true;
}
