#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <inttypes.h>
#include <string>
#include <fstream>

using namespace std;


int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	string file = "D-small-attempt0.in";
	string outfile = "D-small-attempt0.out";
	ifstream fs(file, ios::in);
	ofstream ofs(outfile, ios::out);
	int T, j, X, R, C;


	char val;
	char  lookup[4][4][4] = {
			{
				{ 'G', 'G', 'G', 'G' },
				{ 'G', 'G', 'G', 'G' },
				{ 'G', 'G', 'G', 'G' },
				{ 'G', 'G', 'G', 'G' }
			},
			{
				{ 'R', 'G', 'R', 'G' },
				{ 'G', 'G', 'G', 'G' },
				{ 'R', 'G', 'R', 'G' },
				{ 'G', 'G', 'G', 'G' }
			},
			{
				{ 'R', 'R', 'R', 'R' },
				{ 'R', 'R', 'G', 'R' },
				{ 'R', 'G', 'G', 'G' },
				{ 'R', 'R', 'G', 'R' }
			},
			{
				{ 'R', 'R', 'R', 'R' },
				{ 'R', 'R', 'R', 'R' },
				{ 'R', 'R', 'R', 'G' },
				{ 'R', 'R', 'G', 'G' }
			}
	};

	fs >> T;
	for (j = 1; j <= T; j++){
		fs >> X >> R >> C;
		val = lookup[X - 1][R - 1][C - 1];
		ofs << "Case #" << j << ": " << (val == 'R' ? "RICHARD" : "GABRIEL") << endl;
	}
	fs.close();
	ofs.close();
	return 0;
}
