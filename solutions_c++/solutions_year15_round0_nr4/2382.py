#include <fstream>
#include <string>

using namespace std;

ifstream fin("D-small-attempt0.in");
ofstream fout("out.txt");

int res[5][5][5];

int main() {
	int tests;
	fin >> tests;
	int x, r, c;
	string ans;
	res[2][1][1] = 1;
	res[2][1][3] = 1;
	res[2][3][3] = 1;
	res[3][1][1] = 1;
	res[3][1][2] = 1;
	res[3][1][3] = 1;
	res[3][1][4] = 1;
	res[3][2][2] = 1;
	res[3][2][4] = 1;
	res[3][4][4] = 1;
	res[4][1][1] = 1;
	res[4][1][2] = 1;
	res[4][1][3] = 1;
	res[4][1][4] = 1;
	res[4][2][2] = 1;
	res[4][2][3] = 1;
	res[4][2][4] = 1;
	res[4][3][3] = 1;
	for(int test = 0; test < tests; ++test) {
		fin >> x >> r >> c;
		if(r > c) {
			swap(r, c);
		}
		if(res[x][r][c]) {
			ans = "RICHARD";
		} else {
			ans = "GABRIEL";
		}
		fout << "Case #" << test + 1 << ": " << ans << endl;
	}
	return 0;
}
