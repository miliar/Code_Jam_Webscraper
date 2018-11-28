#include <iostream>
#include <cstring>

using namespace std;

char map[105][105];
bool up[105][105];
bool dow[105][105];
bool lef[105][105];
bool rig[105][105];

void testcase(int t) {
	int R, C;
	cin >> R >> C;

	memset(up, 1, sizeof(up));
	memset(dow, 1, sizeof(dow));
	memset(lef, 1, sizeof(lef));
	memset(rig, 1, sizeof(rig));

	for (int r = 0; r < R; ++r)
		cin >> map[r];

	// Bordo sinistro
	for (int r = 0; r < R; ++r) {
		int c = 0;
		while (c < C && map[r][c] == '.') ++c;
		if (c < C)
			lef[r][c] = false;
	}

	// Bordo destro
	for (int r = 0; r < R; ++r) {
		int c = C - 1;
		while (c >= 0 && map[r][c] == '.') --c;
		if (c >= 0)
			rig[r][c] = false;
	}

	// Bordo top
	for (int c = 0; c < C; ++c) {
		int r = 0;
		while (r < R && map[r][c] == '.') ++r;
		if (r < R)
			up[r][c] = false;
	}

	// Bordo bottom
	for (int c = 0; c < C; ++c) {
		int r = R - 1;
		while (r >= 0 && map[r][c] == '.') --r;
		if (r >= 0)
			dow[r][c] = false;
	}

	int ans = 0;
	for (int r = 0; r < R; ++r) {
		for (int c = 0; c < C; ++c) {
			if (!up[r][c] && !dow[r][c] && !lef[r][c] && !rig[r][c]) {
				cout << "Case #" << t << ": IMPOSSIBLE\n";
				return;
			}
			if (map[r][c] == '^' && !up[r][c]) ++ans;
			if (map[r][c] == '<' && !lef[r][c]) ++ans;
			if (map[r][c] == '>' && !rig[r][c]) ++ans;
			if (map[r][c] == 'v' && !dow[r][c]) ++ans;
		}
	}

	cout << "Case #" << t << ": " << ans << "\n";
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
		testcase(t);
}