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

// A. Mushroom Monster

#pragma region files
//string infile = "sample.txt";
//string infile = "A-small-attempt0.in";
string infile = "A-large.in";
string outfile = "output.txt";

ifstream in(infile);
ofstream out(outfile);
#pragma endregion

long long get_y(vector<int> &m) {
	long long y = 0;
	for (int i = 0; i + 1 < m.size(); ++i) {
		y += max(m[i] - m[i + 1], 0);
	}
	return y;
}

long long get_z(vector<int> &m) {
	long long z = 0;
	int delta = 0;
	for (int i = 0; i + 1 < m.size(); ++i) {
		delta = max(delta, m[i] - m[i + 1]);
	}
	for (int i = 0; i + 1 < m.size(); ++i) {
		z += min(m[i], delta);
	}
	return z;
}

int main() {
	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		int N;
		in >> N;
		vector<int> m;
		for (int i = 0; i < N; ++i) {
			m.push_back(0);
			in >> m.back();
		}
		out << "Case #" << test << ": " << get_y(m) << " " << get_z(m);
		out << endl;
	}
	return 0;
}