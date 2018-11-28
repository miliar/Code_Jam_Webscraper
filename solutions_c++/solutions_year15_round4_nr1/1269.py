#include <iostream>
#include <vector>
#include <string>
#include <assert.h>
#include <iomanip>

using namespace std;

char line[101][101];

int solve(int R, int C) {
/*
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			who[r][c] = -1;
		}
	}
*/
	int count = 0;
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			char x = line[r][c];
			if (x != '.') {
				bool golden = false;
				bool canbe = false;
				for (int rr = r + 1; rr < R; rr++) {
					if (line[rr][c] != '.') {
						canbe = true;
						if (x == 'v') golden = true;
					}
				}
				for (int rr = r - 1; rr >= 0; rr--) {
					if (line[rr][c] != '.') {
						canbe = true;
						if (x == '^') golden = true;
					}
				}
				for (int cc = c + 1; cc < C; cc++) {
					if (line[r][cc] != '.') {
						canbe = true;
						if (x == '>') golden = true;
					}
				}
				for (int cc = c - 1; cc >= 0; cc--) {
					if (line[r][cc] != '.') {
						canbe = true;
						if (x == '<') golden = true;
					}
				}
				if (golden) {
					;
				} else {
					if (canbe) {
						count++;
					} else {
						return -1;
					}
				}
			}
		}
	}
	return count;
}

int main(int argc, const char * argv[]) {
	if (argc == 2) {
		freopen(argv[1], "r", stdin);
	}
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int R, C;
		cin >> R >> C;
		for (int i = 0; i < R; i++) {
			cin >> line[i];
		}
		int result = solve(R, C);
		if (result == -1) {
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << t << ": " << result << endl;
		}
	}
    return 0;
}
