#include <bits/stdc++.h>
using namespace std;

#define TRACE(x) cout << #x << " = " << x << endl

int N, M;
vector<string> board;

char arrows[] = {'<', '>', '^', 'v'};

// enum states = LEFT, RIGHT, UP, DOWN -- 4 states possible
bool allowed[105][105][4];

void setAllow(int x, int y) {
	for (int d = 0; d < 4; d++)
		allowed[x][y][d] = 0;
	
	for (int i = 0; i < x; i++)
		if (board[i][y] != '.')
			allowed[x][y][2] = 1;
	
	for (int i = x+1; i < N; i++)
		if (board[i][y] != '.')
			allowed[x][y][3] = 1;
			
	for (int j = 0; j < y; j++)
		if (board[x][j] != '.')
			allowed[x][y][0] = 1;
			
	for (int j = y+1; j < M; j++)
		if (board[x][j] != '.')
			allowed[x][y][1] = 1;
}

int solve() {
	// compute allowed states
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (board[i][j] != '.') {
				setAllow(i, j);
			}
		}
	}
	
	// see which ones actually need to be changed
	// if NO allowed states for any arrow, return -1;
	int ans = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (board[i][j] != '.') {
				// can we stay the same?
				bool ok = false;
				for (int d = 0; d < 4; d++)
					if (allowed[i][j][d] && board[i][j] == arrows[d])
						ok = true;
				if (ok)
					continue;
				// anything allowed at all?	
				for (int d = 0; d < 4; d++)
					if (allowed[i][j][d])
						ok = true;
				if (!ok)
					return -1;
				else
					ans++;
			}
		}
	}
	return ans;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		board.clear();
		cin >> N >> M;
		for (int i = 0; i < N; i++) {
			string s;
			cin >> s;
			board.push_back(s);
		}
		cout << "Case #" << icase << ": ";
		int res = solve();
		if (res == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
	return 0;
}
