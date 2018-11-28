#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;

int getAns(const string& s) {
	int ans=0;
	int acc=s[0]-'0';
	for (int i=1; i<s.size(); i++) {
		if (acc < i) {
			ans += i-acc;
			acc += i-acc;
		}
		acc += s[i]-'0';
	}
	return ans;
}


int main() {
	ifstream fin("A-large.in");
	assert(fin);
	ofstream fout("pa_large.out");
	assert(fout);
	int test;
	fin >> test;
	for (int count=1; count <= test; count++) {
		int sMax;
		fin >> sMax;
		string s;
		fin >> s;
		fout << "Case #" << count << ": " << getAns(s) << endl;
	}
	fin.close();
	fout.close();

	return 0;
}