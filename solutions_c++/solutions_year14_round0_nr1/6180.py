#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

string NL = "\n";

string solve(int r1_i, int r2_i, int g1[][4], int g2[][4]) {
	vector<int> matches;
	for(int i = 0; i < 4; ++i) {
		for(int j = 0; j < 4; ++j) {
			// cout << g1[r1_i][i] << ":" << g2[r2_i][j] << NL;
			if(g1[r1_i][i] == g2[r2_i][j]) {
				matches.push_back(g1[r1_i][i]);
			}
		}
	}

	if(matches.size() == 0)
		return "Volunteer cheated!";
	else if(matches.size() == 1)
		return to_string(matches[0]);
	else
		return "Bad magician!";
}

int main() {
	int T;

	int r1;
	int r2;
	int g1[4][4];
	int g2[4][4];

	vector<string> results;

	ifstream fin("A-small-attempt0.in");
	fin >> T;
	for(int i = 0; i < T; ++i) {
		fin >> r1;
		for(int r = 0; r < 4; ++r) {
			for(int c = 0; c < 4; ++c) {
				fin >> g1[r][c];
			}
		}

		fin >> r2;
		for(int r = 0; r < 4; ++r) {
			for(int c = 0; c < 4; ++c) {
				fin >> g2[r][c];
			}
		}

		results.push_back(solve(r1 - 1, r2 - 1, g1, g2));
	}
	fin.close();

	ofstream fout("magic-trick.out");
	for (int i = 0; i < results.size(); ++i)
		fout << "Case #" << i + 1 << ": " << results[i] << NL;

	fout.close();

	return 0;
}