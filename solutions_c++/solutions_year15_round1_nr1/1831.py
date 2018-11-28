#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int solve1(const vector<int> &in) {
	int res = 0;
	int old = in[0];
	for (int v : in) {
		if (v < old)
			res += old - v;
		old = v;
	}
	return res;
}
int solve2(const vector<int> &in) {
	vector<int> diffs;
	int old = in[0];
	for (int v : in) {
		diffs.push_back(old - v);
		old = v;
	}
	sort(diffs.begin(), diffs.end());
	int pace = diffs.back();
	int res = 0;
	for (int i = 0; i < in.size() - 1;i++)
		res += min(in[i], pace);
	
	return res;
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("1.out");

	int T;
	fin >> T;

	for (int i = 1; i <= T; i++) {
		int N;
		fin >> N;
		vector<int> vals(N);
		for (int j = 0; j < N; j++)
			fin >> vals[j];
		fout << "Case #" << i << ": " << solve1(vals) << " " << solve2(vals) << "\n";
	}

	fout.close();
	fin.close();
}