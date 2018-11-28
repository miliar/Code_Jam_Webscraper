#include <iostream>
#include <fstream>
#include <cassert>
#include <algorithm>
using namespace std;

void printLastWord(const string& s, int r, ofstream& fout) {
	if (r == 0) {
		return;
	}
	int maxPos = 0;
	char maxc = s[0];
	for (int i=0; i<r; i++) {
		if (s[i] > maxc) {
			maxc = s[i];
			maxPos = i;
		}
	}  
	for (int i=0; i<r; i++) {
		if (s[i] == maxc) {
			fout << maxc;
		}
	}
	printLastWord(s, maxPos, fout);
	for (int i=maxPos+1; i<r; i++) {
		if (s[i] != maxc) {
			fout << s[i];
		}
	}
}

int main() {
	ifstream fin("A-large.in");
	assert(fin);
	ofstream fout("pa-large.out");	
	assert(fout);
	int tot;
	fin >> tot;
	for (int test=1; test<=tot; test++) {
		string s;
		fin >> s;
		fout << "Case #" << test << ": ";
		printLastWord(s, s.size(), fout);
		fout << endl;
	}
	fin.close();
	fout.close();
	return 0;
}