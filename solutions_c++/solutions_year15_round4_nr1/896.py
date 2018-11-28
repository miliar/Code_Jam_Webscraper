#include <bits/stdc++.h>
using namespace std;

int freq1[105], freq2[105];
char grid[105][105];
int test, r, c;

map<char, pair<int, int> > dir;

void preprocess() {
	dir['^'] = make_pair(-1, 0);
	dir['>'] = make_pair(0, 1);
	dir['v'] = make_pair(1, 0);
	dir['<'] = make_pair(0, -1);
}

bool check(int i, int j) {
	pair<int, int> curr = dir[grid[i][j]];
	int curx = i, cury = j;
	while (1) {
		curx += curr.first;
		cury += curr.second;
		if (curx >= r || curx < 0 || cury >= c || cury < 0) {
			return false;
		}
		if(grid[curx][cury] != '.') return true;
	}
	return false;
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	preprocess();
	cin >> test;
	for (int t = 1; t <= test; t++) {
		fill(freq1, freq1 + 105, 0);
		fill(freq2, freq2 + 105, 0);
		cout << "Case #" << t << ": ";
		cin >> r >> c;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cin >> grid[i][j];
				if(grid[i][j] != '.'){
					freq1[i]++;
					freq2[j]++;
				}
			}
		}
		int ans = 0;
		bool ok = false;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(grid[i][j] == '.') continue;
				if(freq1[i] == 1 && freq2[j] == 1) {
					cout << "IMPOSSIBLE\n";
					ok = true;
					break;
				}
				if(!check(i,j))	ans++;
			}
			if(ok) break;
		}
		if(ok) continue;
		cout << ans << "\n";
	}
	return 0;
}