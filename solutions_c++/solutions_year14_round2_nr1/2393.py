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

// Problem A. 

#pragma region files
//string infile = "sample.txt";
string infile = "A-small-attempt0.in";
//string infile = "A-large.in";
string outfile = "output.txt";

ifstream in(infile);
ofstream out(outfile);
#pragma endregion

int main() {
	
	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		out << "Case #" << test << ": ";
		int N;
		in >> N;
		vector<string> s;
		for (int i = 0; i < N; ++i) {
			s.push_back("");
			in >> s.back();
		}
		vector<string> base(N, "");
		vector<vector<int>> count(N, vector<int>(1, 1));
		bool done = false;
		for (int i = 0; i < N; ++i) {
			base[i] += s[i][0];
			for (int j = 1; j < s[i].length(); ++j) {
				if (s[i][j] != base[i].back()) {
					base[i] += s[i][j];
					count[i].push_back(1);
				} else {
					++count[i].back();
				}
			}
			if (base[i] != base[0]) {
				out << "Fegla Won";
				done = true;
				break;
			}
		}
		if (! done) {
			int changes = 0;
			vector<int> avg(count[0].size(), 0);
			for (int i = 0; i < count[0].size(); ++i) {
				for (int j = 0; j < count.size(); ++j) {
					avg[i] += count[j][i];
				}
			}
			for (int i = 0; i < count[0].size(); ++i) {
				avg[i] = floor(double(avg[i]) / double(count.size())) + 0.5;
				for (int j = 0; j < count.size(); ++j) {
					changes += abs(count[j][i] - avg[i]);
				}
			}
			out << changes;
		}
		out << endl;
	}

	return 0;
}