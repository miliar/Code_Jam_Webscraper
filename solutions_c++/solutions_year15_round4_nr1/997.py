#include <iostream>
using namespace std;

#define MAXN 128

char m[MAXN][MAXN], dir[4] = {'^', '<', '>', 'v'};

bool valid(int x, int y) {
	if (m[x][y] == '.') return true;
	
	int dx, dy;
	if (m[x][y] == '^') { dx = -1; dy = 0; }
	else if (m[x][y] == '<') { dx = 0; dy = -1; }
	else if (m[x][y] == '>') { dx = 0; dy = 1; }
	else { dx = 1; dy = 0; }
	
	do {
		x += dx; y += dy;
	} while (m[x][y] == '.');
	return m[x][y] != 'x';
}

int main() {
	int T, t, R, C, i, j, k, RES;
	bool FLAG;
	
	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> R >> C;
		for (i=1; i<=R; i++) for (j=1; j<=C; j++) cin >> m[i][j];
		for (i=0; i<=R+1; i++) m[i][0] = m[i][C+1] = 'x';
		for (j=0; j<=C+1; j++) m[0][j] = m[R+1][j] = 'x';
		
		RES = 0; FLAG = true;
		for (i=1; i<=R; i++) for (j=1; j<=C; j++) if (!valid(i,j)) {
			for (k=0; k<4; k++) {
				m[i][j] = dir[k];
				if (valid(i, j)) break;
			}
			if (k == 4) FLAG = false;
			else RES++;
		}
		cout << "Case #" << t << ": ";
		if (FLAG) cout << RES << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
