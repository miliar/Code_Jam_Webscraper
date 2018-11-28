#include <stdio.h>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <string.h>
using namespace std;
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<int> vi;
#define X first
#define Y second
#define all(c)	(c).begin(), (c).end()
#define sz(x)	((int) (x).size())
#define fill(c, v)	memset((c), (v), sizeof((c)))

struct triad {
	int x, o, t;
	triad(int a=0, int b=0, int c=0) : x(a), o(b), t(c) {}
};

int main() {
	char board[4][6];
	int T;
	cin >> T;
	for(int c=1; c <= T; c++) {
		for(int j=0; j < 4; j++) scanf("%s", board[j]);
		vector<triad> situations;

		// Check rows
		for(int i=0; i < 4; i++) {
			triad t;
			for(int j=0; j < 4; j++) {
				switch(board[i][j]) {
					case 'X': t.x++; break;
					case 'O': t.o++; break;
					case 'T': t.t++; break;
				}
			}
			situations.push_back(t);
		}


		// Check cols

		for(int i=0; i < 4; i++) {
			triad t;
			for(int j=0; j < 4; j++) {
				switch(board[j][i]) {
					case 'X': t.x++; break;
					case 'O': t.o++; break;
					case 'T': t.t++; break;
				}
			}
			situations.push_back(t);
		}

		// Check diags
		triad t, u;
		for(int i=0; i < 4; i++) {
			switch(board[i][i]) {
				case 'X': t.x++; break;
				case 'O': t.o++; break;
				case 'T': t.t++; break;
			}
			switch(board[i][3-i]) {
				case 'X': u.x++; break;
				case 'O': u.o++; break;
				case 'T': u.t++; break;
			}
		}
		situations.push_back(t);
		situations.push_back(u);

		// Check completion
		int dots = 0;
		for(int i=0; i < 4; i++)
			for(int j=0; j < 4; j++)
				if (board[i][j] == '.') {
					dots = 1; 
					break;
				}
		bool flag = false;
		for(int i=0; i < sz(situations); i++) {
			if (situations[i].x == 4 || (situations[i].x == 3 && situations[i].t == 1)) {
				flag = true;
				cout << "Case #" << c << ": X won" << endl;
				break; 
			} else if (situations[i].o == 4 || (situations[i].o == 3 && situations[i].t == 1)) {
				flag = true;
				cout << "Case #" << c << ": O won" << endl;
				break; 
			} 
		}

		if (!flag && dots) {
			cout << "Case #" << c << ": Game has not completed" << endl;
		} else if (!flag) {
			cout << "Case #" << c << ": Draw" << endl;
		}
 
	}
	return 0;
}