#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;

int getAns(string s) {
	s.push_back('+');
	int ans = 0;
	for (int i=0; i<s.size()-1; i++) {
		if (s[i] != s[i+1]) ans++;
	}
	return ans;
}

int main() {
	ifstream fin("B-large.in");
	assert(fin);
	ofstream fout("pb_large.out");
	assert(fout);
	int test;
	fin >> test;
	for (int cur = 1; cur <= test; cur++) {
		string s;
		fin >> s;
		fout << "Case #" << cur << ": " << getAns(s) << endl;
	}
	return 0;
}