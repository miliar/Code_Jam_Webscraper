#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
using namespace std;

vector<int> readAndGetAns(ifstream& fin) {
	int n;
    fin >> n;
	int count[2601] = {0};
	for (int i=0; i<2*n-1; i++) {
		for (int j=0; j<n; j++) {
			int h;
			fin >> h;
			count[h]++;
		}
	}
	vector<int> ans;
	for (int h=1; h<=2500; h++) {
		if (count[h] % 2 == 1) {
			ans.push_back(h);
		}
	}
	assert(ans.size() == n);
	return ans;
}

int main() {
	ifstream fin("B-large.in");
	assert(fin);
	ofstream fout("pb-large.out");
	assert(fout);
	int all;
	fin >> all;
	for (int test=1; test<=all; test++) {
		fout << "Case #" << test << ":";
		vector<int> ans = readAndGetAns(fin);
		for (int i=0; i<ans.size(); i++) {
			fout << ' ' << ans[i];
		}
		fout << endl;
	}
	fin.close();
	fout.close();
	return 0;
}