#include <iostream>
#include <math.h>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <string>
#include <vector>

using namespace std;

ifstream fin("D-small-attempt0.in");
ofstream fout("D-small-attempt0.out");

int T, R, C;
char board[100][100];

set<vector<int> > fstline;

bool isOkay(int r, int c) {
	int eq = 0;
	eq += board[r][(c + C - 1) % C] == board[r][c];
	if (r > 0)
		eq += board[(r + R - 1) % R][c] == board[r][c];
	eq += board[r][(c + 1) % C] == board[r][c];
	if (r < R - 1)
	eq += board[(r + 1) % R][c] == board[r][c];
	return eq == board[r][c];
}

long long int rec(int r, int c) {
	long long int result = 0;
	for (int n = 1; n <= 3; ++n) {
		board[r][c] = n;

		bool valid = true;
		if (r > 0)
			valid = isOkay(r-1, c);
		if (r == R - 1 && c > 1)
			valid = valid && isOkay(r, c - 1);
		if (r == R - 1 && c == C - 1) {
			valid = valid && isOkay(r, c);
			valid = valid && isOkay(r, 0);
		}
//		printf("%d %d -> valid -> %d\n", r, c, valid);
		if (valid) {
			if (c == C - 1 && r == R - 1) {
				vector<int> v;
				for(int k = 0; k < R; ++k)
					for(int j = 0; j < C; ++j)
						v.push_back(board[k][j]);
				if (fstline.find(v) == fstline.end()) {
					result += 1;
					for(int i = 0; i < C; ++i){
						vector<int> v;
						for(int k = 0; k < R; ++k)
							for(int j = 0; j < C; ++j)
								v.push_back(board[k][(i + j) % C]);
						fstline.insert(v);
					}
				}


/*				for (int r = 0; r < R; ++r) {
					for (int c = 0; c < C; ++c)
						printf("%d, ", board[r][c]);
					printf("\n");
				}*/
//				printf("\n");
			}
			else if (c == C - 1) {
//				printf("res += rec(%d %d) (r + 1, 0)\n", r + 1, 0);
				result += rec(r + 1, 0);
			}
			else {
//				printf("res += rec(%d %d) (r, c + 1)\n", r, c+1);
				result += rec(r, c + 1);
			}
		}
	}
	return result % 1000000007;
}

int main() {
	fin >> T;
	for (int t = 1; t <= T; ++t) {
		fin >> R >> C;
		fstline.clear();
		printf("Case %d: %d %d\n", t, R, C);
		fout << "Case #" << t << ": " << rec(0,0) << endl;
	}

	return 0;
}
