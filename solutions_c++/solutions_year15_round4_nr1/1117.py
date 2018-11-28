#include <iostream>
#include <string>
using namespace std;

const int dx[4] = {1,0,-1,0};
const int dy[4] = {0,-1,0,1};
int r,c;
char map[110][110];

int toDir(char arrow) {
	switch (arrow) {
	case 'v':
		return 0;
	case '<':
		return 1;
	case '^':
		return 2;
	case '>':
		return 3;
	default:
		return -1;
	}
}

bool findNextArrow(int x, int y, int dir) {
	int tx = x + dx[dir];
	int ty = y + dy[dir];
	while (true) {
		if (tx<0 || tx>=r || ty<0 || ty>=c)
			return false;
		if (map[tx][ty]!='.')
			return true;
		tx += dx[dir];
		ty += dy[dir];
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int Tn, T;
	cin >> Tn;
	for (T=1; T<=Tn; T++) {
		cin >> r >> c;
		int i,j;
		for (i=0;i<r;i++) {
			string row;
			cin >> row;
			for (j=0;j<c;j++)
				map[i][j] = row[j];
		}
		
		int ans = 0;
		bool fail = false;
		for (i=0;i<r;i++) {
			for (j=0;j<c;j++) 
				if (map[i][j] != '.') {
					if (!findNextArrow(i, j, toDir(map[i][j]))) {
						bool found = false;
						for (int dir=0; dir<4; dir++)
							if (dir!=toDir(map[i][j]) && findNextArrow(i, j, dir)) {
								found = true;
								break;
							}
						if (found) {
							ans++;
						}
						else {
							fail = true;
							break;
						}
					}
				}
			if (fail) break;
		}
		cout << "Case #" << T << ": ";
		if (fail)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
}