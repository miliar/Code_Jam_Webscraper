#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <math.h>
#include <string>
#include <string.h>
#include <iomanip>

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)

using namespace std;

int main() {

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t, T, i, j, k, N, l;
	string s, out;

	fin >> T;
	for1(t, T) {

		fin >> s;

		l = s.length();
		out = s[0];


		for1(i, l-1) {
			if (s[i] > out[0]) {
				out = s[i] + out;
			}
			else if (s[i] == out[0]) {
				out = s[i] + out;
			}
			else {
				out = out + s[i];
			}

		}

		fout << "Case #" << t << ": " << out << endl;

	}

	return 0;
}