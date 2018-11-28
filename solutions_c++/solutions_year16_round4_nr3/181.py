#include <bits/stdc++.h>

using namespace std;

vector<vector<vector<int>>> walker = {
	{	//false
		{1,-1,0},
		{0,0,-1},
		{3,1,0},
		{2,0,1},
	},
	{	//true
		{3,+1,0},
		{2,0,1},
		{1,-1,0},
		{0,0,-1},
	},
};

pair<int, int> placeFromId(int id, int R, int C) {
	if (id < C) return {-1,id};
	if (id < R+C) return {id-C, C};
	if (id < 2*C+R) return {R, C-(id-R-C)-1};
	return {R-(id-2*C-R)-1,-1};
}

int idFromPlace(int x, int y, int R, int C) {
	if (y == -1) return 2*C+R+(R-x-1);
	if (x == R) return R+C+(C-y-1);
	if (y == C) return C+x;
	return y;
}

bool verify(vector<vector<int>> &grid, vector<pair<int, int>> pairs) {
	int R = grid.size();
	int C = grid[0].size();
	
	set<pair<pair<int, int>,int>> seen;
	
	for (auto p : pairs) {
		auto cur = placeFromId(p.first, R, C);
		int pdir;
		
		if (cur.first == -1) {
			cur.first = 0;
			pdir = 1;
		}
		if (cur.second == -1) {
			cur.second = 0;
			pdir = 0;
		}
		if (cur.first == R) {
			cur.first = R-1;
			pdir = 3;
		}
		if (cur.second == C) {
			cur.second = C-1;
			pdir = 2;
		}
		
		while (cur.first >= 0 && cur.first < R && cur.second >= 0 && cur.second < C) {
			if (seen.count({cur, pdir})) return false;
			seen.insert({cur,pdir});
			seen.insert({cur,walker[grid[cur.first][cur.second]][pdir][0]});
			
			int dx = walker[grid[cur.first][cur.second]][pdir][1];
			int dy = walker[grid[cur.first][cur.second]][pdir][2];
			pdir = walker[grid[cur.first][cur.second]][pdir][0];
			
			cur.first += dx;
			cur.second += dy;
			pdir = (pdir + 2) % 4;
		}
		
		int res = idFromPlace(cur.first, cur.second, R, C);
		if (res != p.second) return false;
	}
	return true;
}

void doCase(int t) {
	int R,C;
	cin >> R >> C;
	int N = R+C;
	vector<pair<int, int>> pairs(N);
	for (int i=0; i<N; i++) {
		cin >> pairs[i].first >> pairs[i].second;
		pairs[i].first--;
		pairs[i].second--;
	}
	int K = R*C;
	
	vector<vector<int>> grid(R,vector<int>(C));
	
	cout << "Case #" << t << ":" << endl;
	for (int i=0; i<(1<<K); i++) {
		for (int j=0; j<R; j++) {
			for (int k=0; k<C; k++) {
				if (i & (1 << (j*C+k))) grid[j][k] = 1;
				else grid[j][k] = 0;
			}
		}
		
		/*for (int j=0; j<R; j++) {
			for (int k=0; k<C; k++) {
				if (grid[j][k] == 1) cerr << "\\";
				else cerr << "/";
			}
			cerr << endl;
		}*/
		
		if (!verify(grid, pairs)) continue;
		
		for (int j=0; j<R; j++) {
			for (int k=0; k<C; k++) {
				if (grid[j][k] == 1) cout << "\\";
				else cout << "/";
			}
			cout << endl;
		}
		return;
	}
	
	cout << "IMPOSSIBLE" << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++) doCase(i+1);
	return 0;
}
