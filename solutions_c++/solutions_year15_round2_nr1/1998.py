#pragma region includes
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip> // out << setprecision(n) << fixed; // set to show n decimal places
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
#pragma endregion

// A. Counter Culture

#pragma region files
//string infile = "sample.txt";
string infile = "A-small-attempt0.in";
//string infile = "A-large.in";
string outfile = "output.txt";

ifstream in(infile);
ofstream out(outfile);
#pragma endregion

void generate(vector<long long> &count, long long stop) {
	stringstream ss;
	string s;
	long long n;
	for (long long i = 0; i <= stop; ++i) {
		count.push_back(i);
	}
	for (long long i = 1; i < stop; ++i) {
		count[i + 1] = min(count[i + 1], count[i] + 1);
		ss << i << " ";
		ss >> s;
		reverse(s.begin(), s.end());
		ss << s << " ";
		ss >> n;
		if ((n > i) && (n <= stop)) {
			count[n] = min(count[n], count[i] + 1);
		}
	}
}

int main() {
	int T;
	in >> T;
	long long n = pow(10, 6);
	vector<long long> count;
	generate(count, n);
	for (int test = 1; test <= T; ++test) {
		long long N;
		in >> N;
		out << "Case #" << test << ": " << count[N] << endl;
	}
	return 0;
}