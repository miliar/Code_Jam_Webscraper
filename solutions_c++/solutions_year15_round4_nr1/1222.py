#include <algorithm>
#include <iostream>
#include <iomanip>
#include <queue>
#include <set>
#include <vector>

using namespace std;

string grid[101];

int dx[5] = { 1, -1, 0,  0, 0 };
int dy[5] = { 0,  0, 1, -1, 0 };
string dirs = "<>^v";

int walk(int x, int y, int d, bool hasPrev)
{
	//cout << "Walking on " << x << " / " << y << " = " << grid[x][y] << endl;
	if (grid[x][y] == '^') { if (d!=4) hasPrev = true; d = 1; }
	if (grid[x][y] == '<') { if (d!=4) hasPrev = true; d = 3; }
	if (grid[x][y] == '>') { if (d!=4) hasPrev = true; d = 2; }
	if (grid[x][y] == 'v') { if (d!=4) hasPrev = true; d = 0; }
	if (grid[x][y] == '#') {
		return hasPrev ? 1 : -1;
	}
	if (grid[x][y] == 'S') return 0;
	if (grid[x][y] != '.') grid[x][y] = 'S';
	return walk(x + dx[d], y + dy[d], d, hasPrev);
}

int solve()
{
	int r, c;
	cin >> r >> c;
	grid[0] = string(c+2, '#');
	for (int i=1; i<=r; i++) {
		cin >> grid[i];
		grid[i] = "#" + grid[i] + "#";
	}
	grid[r+1] = string(c+2, '#');
	
	int changes = 0;
	for (int i=1; i<=r; i++) {
		for (int j=1; j<=c; j++) {
			if (grid[i][j] == '.') continue;
			int w = walk(i, j, 4, false);
			//cout << "WALKING FROM " << i << "/" << j << " REQ " << w << " CHANGES" << endl;
			if (w < 0) {
				bool averted = false;
				for (int d=0; d<4; d++) {
					grid[i][j] = dirs[d];
					w = walk(i, j, 4, false);
					//cout << "USING " << d << " REQ " << w << " CHANGES" << endl;
					if (w >= 0) {
						changes += w + 1;
						averted = true;
						break;
					}
				}
				if (!averted) return -1;
			} else {
				changes += w;
			}
		}
	}
	
	return changes;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	for (int tn=1; tn<=t; tn++) {
		cout << "Case #" << tn << ": ";
		int answer = solve();
		if (answer < 0) cout << "IMPOSSIBLE";
		else cout << answer;
		cout << "\n";
	}
	return 0;
}