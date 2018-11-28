#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
using namespace std;

long long getTileId(int start, int C, int K) {
	long long id = start;
	for (int i = start+1; i < start + C; i++) {
		id = (id-1)*K;
		if (i <= K) id += i;
		else id += K;
	}
	return id;
}

vector<long long> getAns(int K, int C, int S) {
	vector<long long> ret;
	for (int i=1; i<=K; i+=C){
		ret.push_back(getTileId(i, C, K));
	}
	return ret;
}

int main() {
	ifstream fin("D-large.in");
	assert(fin);
	ofstream fout("pd-large.out");
	assert(fout);
	int test;
	fin >> test;
	for (int cur = 1; cur <= test; cur++) {
		int K, C, S;
		fin >> K >> C >> S;
		fout << "Case #" << cur << ":";
		if (C * S < K) {
			fout << " IMPOSSIBLE" << endl;
		} else {
			vector<long long> ans = getAns(K, C, S);
			for (long long x : ans) {
				fout << ' ' << x; 
			}
			fout << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}