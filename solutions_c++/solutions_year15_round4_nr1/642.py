#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define	For(i,a,b)				for(int i=(a);i<(b);++i)
#define	rep(i,n)				For(i,0,(n))

typedef	vector<string>			VS;

const int cdx[] = {0, 1, 0, -1};
const int cdy[] = {1, 0, -1, 0};


int check(const VS &grid, char c, int x, int y, int dx, int dy)
{
	for(; 0 <= x && x < grid[0].size() && 0 <= y && y < grid.size() ; x += dx, y += dy) {
		if(grid[y][x] == '.')
			continue;

		if(grid[y][x] != c)
			return 0;

		rep(i, 4) {
			for(int tx = x + cdx[i], ty = y + cdy[i] ; 0 <= tx && tx < grid[0].size() && 0 <= ty && ty < grid.size() ; tx += cdx[i], ty += cdy[i]) {
				if(grid[ty][tx] != '.')
					return 1;
			}
		}
		throw -1;
	}
	return 0;
}

string solve()
{
	try {
		int R, C;

		cin >> R >> C;

		VS grid(R);
		getline(cin, grid[0]);
		rep(i, R)
			getline(cin, grid[i]);

		int res = 0;
		rep(i, R) {
			res += check(grid, '<', 0, i, 1, 0);
			res += check(grid, '>', C - 1, i, -1, 0);
		}
		rep(j, C) {
			res += check(grid, '^', j, 0, 0, 1);
			res += check(grid, 'v', j, R - 1, 0, -1);
		}

		return to_string(res);
	} catch(...) {
		return "IMPOSSIBLE";
	}
}

int main()
{
	int T;

	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}
