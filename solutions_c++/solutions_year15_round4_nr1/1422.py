#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define sz size()
typedef long long ll;
typedef vector<int> vi;
const int oo = (int)1e9;

// ^, v, <, >
int dx[] = {-1, 1, 0, 0};
int dy[] = { 0, 0,-1, 1};
char ch[] = {'^', 'v', '<', '>'};
int t, r, c;
char s[110][110];

int main() {
	scanf("%d", &t);
	int xx = 1;
	while (t--) {
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; i++) {
			scanf("%s", s[i]);
		}
		int ans = 0;
		for (int i = 0; i < r; i++) {
			if (ans == -1) break;
			for (int j = 0; j < c; j++) {
				if (ans == -1) break;
				if (s[i][j] == '.') continue;
				bool found = 0;
				for (int k = 0; k < 4; k++) {
					if (ch[k] == s[i][j]) {
						int nx = i + dx[k];
						int ny = j + dy[k];
						while (nx >= 0 && ny >= 0 && nx < r && ny < c) {
							if (s[nx][ny] != '.') {
								found = 1; break;
							}
							nx += dx[k];
							ny += dy[k];
						}
					}
				}
				if (!found) {
					bool can = 0;
					for (int k = 0; k < 4; k++) {
						int nx = i + dx[k];
						int ny = j + dy[k];
						while (nx >= 0 && ny >= 0 && nx < r && ny < c) {
							if (s[nx][ny] != '.') {
								can = 1; break;
							}
							nx += dx[k];
							ny += dy[k];
						}
						if (can) break;
					}
					if (!can) {
						ans = -1;
					} else ans++;
				}
			}
		}
		printf("Case #%d: ", xx++);
		if (ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
