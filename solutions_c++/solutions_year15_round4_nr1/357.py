#include <iostream>
#include <math.h>
#include <fstream>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define pair<int, int> PII

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int T, R, C;
char board[100][100];
bool valid[100][100];

int main() {
	fin >> T;
	for (int t = 1; t <= T; ++t) {
		fin >> R >> C;
		for (int i = 0; i < R; ++i)
			fill_n(valid[i], C, false);
		for (int i = 0; i < R; ++i)
			for (int c = 0; c < C; ++c)
				fin >> board[i][c];

		int toswitch = 0;
		bool poss = true;

//		printf("Case %d: R= %d, C= %d\n", t, R, C);
		for (int r = 0; poss && r < R; ++r)
			for (int c = 0; poss && c < C; ++c) {
//				printf("board[%d][%d] = %c, val = %d\n", r, c, board[r][c], valid[r][c]);
				if (board[r][c] != '.' && !valid[r][c]) {
//					printf("checking pos %d %d\n", r, c);
					valid[r][c] = true;
					int cr = r;
					int cc = c;
					int lr = r;
					int lc = c;
					char dir = board[r][c];
					if (dir == '<')
						cc--;
					else if (dir == '>')
						cc++;
					else if (dir == '^')
						cr--;
					else
						cr++;
					while (cr >= 0 && cr < R && cc >= 0 && cc < C && !valid[cr][cc]) {
						if (board[cr][cc] != '.') {
							dir = board[cr][cc];
							valid[cr][cc] = true;
							lr = cr;
							lc = cc;
						}
						if (dir == '<')
							cc--;
						else if (dir == '>')
							cc++;
						else if (dir == '^')
							cr--;
						else
							cr++;
					}
					if (!(cr >= 0 && cr < R && cc >= 0 && cc < C)) {
//						printf("if (%d %d), (%d %d)\n", cr, cc, lr, lr);
						poss = false;
						for (int r = 0; r < R; ++r)
							if (board[r][lc] != '.' && r != lr)
								poss = true;
						for (int c = 0; c < C; ++c)
							if (board[lr][c] != '.' && c != lc)
								poss = true;
						toswitch++;
					}
/*					for (int r = 0; poss && r < R; ++r)
						for (int c = 0; poss && c < C; ++c)
							printf("board[%d][%d] %c, valid %d\n", r, c, board[r][c], valid[r][c]);
*/				}
			}

//		printf("Case %d\n", t);
		if (poss)
			fout << "Case #" << t << ": " << toswitch << endl;
		else
			fout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
	}

	return 0;
}
