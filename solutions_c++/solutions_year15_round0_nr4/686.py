#include <fstream>
#include <cassert>
using namespace std;

const char * const RICHARD = "RICHARD";
const char * const GABRIEL = "GABRIEL";

bool isGarrielWin(int X, int R, int C) {
	if (X >= 7) return false;
	if (R * C % X != 0) return false;
	if (R > C) swap(R, C);

	if (X <= 2) return true;
	if (X == 3) return R >= 2;
	if (X == 4) return R >= 3;
	return false;
}

int main() {
	ifstream fin("D-small-attempt0.in");
	ofstream fout("pd_small.out");
	assert(fin && fout);
	int test;
	fin >> test;
	for (int count=1; count<=test; count++) {
		int X, R, C;
		fin >> X >> R >> C;
		fout << "Case #" << count << ": " << (isGarrielWin(X, R, C) ? GABRIEL : RICHARD) << endl; 
	}
	fin.close();
	fout.close();
	return 0;
}