#include <iostream>
#include <cstring>
#include <map>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

const int MAXN = 110;

map<char, int> dx, dy;

char a[MAXN][MAXN];
int r, c;

pii nxt[MAXN][MAXN];
bool reach[MAXN][MAXN];
int cntX[MAXN], cntY[MAXN];

bool isGood(int x, int y) {
	return (x >= 0 && y >= 0 && x < r && y < c);
}

int main() {
	dx['>'] = 0, dy['>'] = 1;
	dx['<'] = 0, dy['<'] = -1;
	dx['v'] = 1, dy['v'] = 0;
	dx['^'] = -1, dy['^'] = 0;
	int tt;
	cin >> tt;
	for (int o = 1; o <= tt; o++) {
		cin >> r >> c;
		memset(nxt, -1, sizeof nxt);
		memset(reach, false, sizeof reach);
		memset(cntX, 0, sizeof cntX);
		memset(cntY, 0, sizeof cntY);
		for (int i = 0; i < r; i++) {
			string tmp;
			cin >> tmp;
			for (int j = 0; j < c; j++) {
				a[i][j] = tmp[j];
				if (a[i][j] != '.')
					cntX[i]++, cntY[j]++;
			}
		}
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (a[i][j] != '.') {
					int cx = i, cy = j;
					int cdx = dx[a[i][j]], cdy = dy[a[i][j]];
					cx += cdx, cy += cdy;
					while(isGood(cx, cy)) {
						if (a[cx][cy] != '.') {
							nxt[i][j] = pii(cx, cy);
							reach[cx][cy] = true;
							break;
						}
						cx += cdx, cy += cdy;
					}
				}
			}
		int ans = 0;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (a[i][j] != '.' && cntX[i] == 1 && cntY[j] == 1)
					ans = -1;
			}
		if (ans != -1) {
			for (int i = 0; i < r; i++)
				for (int j = 0; j < c; j++)
					if (a[i][j] != '.' && nxt[i][j] == pii(-1, -1))
						ans++;
			cout << "Case #" << o << ": " << ans << endl;
		}
		else
			cout << "Case #" << o << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}
