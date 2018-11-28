#include<bits/stdc++.h>
using namespace std;

string s[105];

map<char, int> dx, dy;
int n, m;
bool valid(int x, int y) {
	if (x < 0 || y < 0 || x >= n || y >= m)
		return false;
	return true;
}

bool safe(int i, int j, char c) {
	int x = i + dx[c];
	int y = j + dy[c];
	while (valid(x, y)) {
		if (s[x][y] != '.')
			break;
		x += dx[c];
		y += dy[c];
	}
	if (valid(x, y))
		return true;
	return false;
}


int main() {
	freopen("/home/ahmed_ossama/Round 2/Task A/A-small-attempt0.in", "r", stdin);
	freopen("/home/ahmed_ossama/Round 2/Task A/A-small-attempt0.out", "w", stdout);
	dx['^'] = -1;
	dy['^'] = 0;
	dx['v'] = 1;
	dy['v'] = 0;

	dx['<'] = 0;
	dy['<'] = -1;
	dx['>'] = 0;
	dy['>'] = 1;
	int id = 1;
	char C[4] = {'^', 'v', '>', '<'};
	int t;
	cin >> t;
	while (t--) {
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			cin >> s[i];
		bool good = true;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (s[i][j] == '.')
					continue;
				char c = s[i][j];
				if (safe(i, j, c))
					continue;
				ans++;
				for (int k = 0; k < 4; k++) {
					if (safe(i, j, C[k])) {
						s[i][j] = C[k];
						break;
					}
				}
				if (safe(i, j, s[i][j]))
					continue;
				good = false;
			}
		}
		cout << "Case #" << id++ << ": ";
		if (!good) {
			cout << "IMPOSSIBLE\n";
		}
		else
			cout << ans << endl;

	}


}

