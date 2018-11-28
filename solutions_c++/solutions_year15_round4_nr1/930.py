#include<cstdio>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<sstream>
#include<cmath>
#include<cctype>
#include<cassert>
#include<cstring>
#include<cstdlib>

using namespace std;

const int debug = 0;
#define DEBUG(x) cout<<">> "<<#x<<':'<<(x)<<endl
const int inf = 1000000000;

vector<string> grid;
int R, C;
int res;

string move = "^>v<";
int dir[][2] = {
	-1, 0,
	0, 1,
	1, 0,
	0, -1
};

bool inside(int r, int c) {
	return r >= 0 && r < R && c >= 0 && c < C;
}

int main() {
	int test, cases = 1;
	cin >> test;
	for (cases = 1; cases <= test; cases++) {
		cin >> R >> C;
		grid.clear();
		for (int i = 0; i < R; i++) {
			string s; cin >> s; grid.push_back(s);
		}
		int res = 0;
		bool imp = false;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (grid[i][j] != '.') {
					int r = i, c = j;
					int p = 0;
					for (; grid[i][j] != move[p]; p++);
					bool yes = true;
					while(true) {
						r = r + dir[ p ][ 0 ];
						c = c + dir[ p ][ 1 ];
						if (!inside(r, c)) {
							yes = false;
							break;
						} else if (grid[r][c] != '.') break;
					}
					if (!yes) {
						bool ok = false;
						for (int r = 0; r < R; r++) {
							if (r == i) continue;
							if (grid[r][j] != '.') ok = true;
						}
						for (int c = 0; c < C; c++) {
							if (c == j) continue;
							if (grid[i][c] != '.') ok = true;
						}
						if (ok) {
							res++;
						} else {
							imp = true;
						}
					}
				}
			}
		}
		printf("Case #%d: ", cases);
		if (imp) cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;

	}
	return 0;
}
