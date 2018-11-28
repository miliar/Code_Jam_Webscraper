#include <bits/stdc++.h>
using namespace std;

string b[105];

int R, C;

bool f(int r, int c) {
	if(b[r][c] == '.') return false;
	if(b[r][c] == '>') {
		for(int i = c+1; i < C; i++)
			if(b[r][i] != '.') return false;
		return true;
	}
	if(b[r][c] == '<') {
		for(int i = c-1; i >= 0; i--)
			if(b[r][i] != '.') return false;
		return true;
	}
	if(b[r][c] == '^') {
		for(int i = r-1; i >= 0; i--)
			if(b[i][c] != '.') return false;
		return true;
	}
	if(b[r][c] == 'v') {
		for(int i = r+1; i < R; i++)
			if(b[i][c] != '.') return false;
		return true;
	}
}

bool g(int r, int c) {
	for(int i = 0; i < R; i++)
		if(b[i][c] != '.' && i != r) return true;
	for(int i = 0; i < C; i++)
		if(b[r][i] != '.' && i != c) return true;
	return false;
}

int main () {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> R >> C;
		for(int i = 0; i < R; i++)
			cin >> b[i];
		int res = 0;
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				bool x = f(i, j);
				bool y = g(i, j);
				if(x && y)
					res++;
				else if(x) {
					res = -1;
					break;
				}
			}
			if(res == -1)
				break;
		}
		if(res == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
	return 0;
}
