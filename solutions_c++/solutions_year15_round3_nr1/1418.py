#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;

int getAns(int c, int w) {
	if (w==1) return c;
	if (c==w) return c;
	int n = c-w+1;
	int re = n % w;
	if (re == 1) return n/w+w;
	if (re == 0) return n/w+w;
	return n/w+w+1;
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("pa-large.out");
	assert(fin && fout);

	int test;
	fin >> test;
	for (int count=1; count<=test; count++) {
		int r, c, w;
		fin >> r >> c >> w;
		fout << "Case #" << count << ": " << (c/w)*(r-1)+getAns(c, w) << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}