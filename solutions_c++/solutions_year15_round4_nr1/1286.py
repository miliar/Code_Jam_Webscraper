#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for(int i=0; i<int(n); ++i)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
typedef long long ll;

int TC;
const int dx[] = {1, 0, -1, 0, 1, 1, -1, -1}, dy[] = {0, 1, 0, -1, 1, -1, 1, -1};




void solve() {
	int R, C;
	cin >> R >> C;
	string A[R];
	rep(i, R) cin >> A[i];

	const string dirs = ">v<^";
	int cnt = 0;
	rep(i, R) rep(j, C) {
		int p = dirs.find(A[i][j]);
		if (p == -1) continue;
		bool oks[4] = {};
		rep(d, 4) {
			oks[d] = false;
			int x = j, y = i;
			while(true) {
				x += dx[d];
				y += dy[d];
				if (!(x >= 0 && y >= 0 && x < C && y < R)) break;
				if (A[y][x] != '.') {
					oks[d] = true;
					break;
				}
			}
		}
		if (oks[p]) continue;
		bool ok = false;
		rep(d, 4) if (oks[d]) ok = true;
		if (ok) cnt++;
		else {
			cout << "IMPOSSIBLE" << endl;
			return;

		}
	}
	cout << cnt << endl;

}
int main() {
	int T; cin >> T;
	for(TC=1; TC<=T; TC++) {
		cout << "Case #" << TC << ": ";
		solve();
	}
}

