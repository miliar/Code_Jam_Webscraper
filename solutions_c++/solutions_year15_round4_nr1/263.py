#include <bits/stdc++.h>
using namespace std;

const int MAXR = 105;
int T, R, C;
char grid[MAXR][MAXR];

bool has(int r, int c, char dir) {
	switch(dir) {
		case '^':
			for(int k=r-1; k>=0; --k)
				if(grid[k][c]) return true;
			return false;
		case '>':
			for(int k=c+1; k<C; ++k)
				if(grid[r][k]) return true;
			return false;
		case 'v':
			for(int k=r+1; k<R; ++k)
				if(grid[k][c]) return true;
			return false;
		case '<':
			for(int k=c-1; k>=0; --k)
				if(grid[r][k]) return true;
			return false;
		default:
			break;
	}
	return false;
}

int main(){
	if(fopen("test.in","r")) {
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t) {
		cin >> R >> C;
		for(int i=0; i<R; ++i) for(int j=0; j<C; ++j) {
			cin >> grid[i][j];
			if(grid[i][j] == '.') grid[i][j] = 0;
		}
		bool works = true;
		int change = 0;
		for(int i=0; i<R; ++i) for(int j=0; j<C; ++j)
			if(grid[i][j]) {
				works &= has(i,j,'^') || has(i,j,'>') || has(i,j,'v') || has(i,j,'<');
				if(!has(i,j,grid[i][j])) ++change;
			}
		cout << "Case #" << t << ": ";
		if(works) cout << change << '\n';
		else cout << "IMPOSSIBLE\n";
	}
}
