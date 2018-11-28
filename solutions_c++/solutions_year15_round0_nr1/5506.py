#pragma region includes
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip> // out << setprecision(n) << fixed; // set to show n decimal places
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
#pragma endregion

// A. Standing Ovation

#pragma region files
//string infile = "sample.txt";
//string infile = "A-small-attempt0.in";
string infile = "A-large.in";
string outfile = "output.txt";

ifstream in(infile);
ofstream out(outfile);
#pragma endregion

int main() {
	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		long long total = 0;
		long long n = 0;
		int S_max;
		char c;
		in >> S_max >> c;
		for (int i = 0; i < S_max; ++i) {
			total += c - '0';
			in >> c;
			if (c - '0') {
				long long d = max((long long) 0, i + 1 - total);
				total += d;
				n += d;
			}
		}

		out << "Case #" << test << ": " << n;
		out << endl;

		/*
		cout << 1000 << " ";
		for (int i = 0; i < 1000; ++i) {
			cout << 0;
		}
		cout << 1 << endl;
		cin >> c;
		*/
	}
	return 0;
}