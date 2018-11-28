#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

long K, C, S;

vector<long long> solve() {
	vector<long long> ret;
	
	if (C > K) C = K;

	long long kpc = 1;
	for (int i = 0; i < C; ++i) kpc *= K;
	long long num = 0;
	long long start = 0;
	while (num != K) {
		if (C == 1)
			ret.push_back(start + num + 1);
		else {
			kpc /= K;
			start += num * kpc;
			--C;
		}
		++num;
	}
	return ret;
}


int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int c;
	fin >> c;
	for (int tc = 1; tc <= c; ++tc) {
		fin >> K >> C >> S;
		vector<long long> ret = solve();
		fout << "Case #" << tc << ": ";
		if (ret.size() > S) fout << "IMPOSSIBLE" << endl;
		else{
			for (int i = 0; i < ret.size(); ++i)
				fout << ret[i] << ' ';
			fout << endl;
		}

	}
}