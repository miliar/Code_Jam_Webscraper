#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

#define range(i,a,b) for(int i = (a), _n = (b); i < _n; ++i)
#define fo(i,n) range(i,0,n)
#define pb push_back

const int BLANK = 0, UP = 1, DOWN = 2, LEFT = 3, RIGHT = 4;
const int DC[] = {0, 0, 0, -1, 1}, DR[] = {0, -1, 1, 0, 0};
const int DIR = 5;

const int MAX_R = 110, MAX_C = MAX_R, MAX_N = MAX_R * MAX_C;
int R, C, grid[MAX_R][MAX_C], nextR[MAX_R][MAX_C], nextC[MAX_R][MAX_C];
int anyR[MAX_C], anyC[MAX_R];

inline bool in(int r, int c) {
	return r >= 0 && r < R && c >= 0 && c < C;
}

int solve() {
	int res = 0;
	fo(r,R) fo(c,C) if(grid[r][c] != BLANK) {
		int dr = DR[grid[r][c]], dc = DC[grid[r][c]];
		int tr = r, tc = c;
		bool found = false;
		tr += dr; tc += dc;
		while (in(tr,tc)) {
			if (grid[tr][tc] != BLANK) {
				found = true;
				break;
			}
			tr += dr; tc += dc;
		}
		if (!found) {
			if (anyR[c] > 1 || anyC[r] > 1) {
				res += 1;
			} else {
				return -1;
			}
		}
	}
	return res;
}

int main() {
	int T;
	cin >> T;
	range(testCase, 1, T+1) {
		cin >> R >> C;
		fo(r,R) anyC[r] = false;
		fo(c,C) anyR[c] = false;
		fo(r, R) fo(c, C) {
			char d;
			cin >> d;
			grid[r][c] = (d == '.' ? BLANK : (d == '^' ? UP : (d == 'v' ? DOWN : (d == '<' ? LEFT : RIGHT))));
			if(grid[r][c] != BLANK) {
				anyR[c] += 1;
				anyC[r] += 1;
			}
		}
		int res = solve();
		cout << "Case #" << testCase << ": ";
		if (res != -1) {
			cout << res;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
}