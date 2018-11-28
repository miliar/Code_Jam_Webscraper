#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

vector<string> f;

char dc[6] = "^<v>.";
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

int r, c;

bool inside(int x, int y) {
	return 0 <= x && x < r && 0 <= y && y < c;
}

void solve() {
	cin >> r >> c;
	f.resize(r);
	for (auto &s: f) {
		cin >> s;
		assert(s.size() == size_t(c));
	}
	int ans = 0;
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) if (f[i][j] != '.') {
			char *sp = strchr(dc, f[i][j]);
			assert(sp);
			int myd = sp - dc;
			assert(myd < 4);
			//E(i, j, myd, dx[myd], dy[myd]);
			bool possible = false;
			int cost = 1;
			for (int d = 0; d < 4; ++d) {
				int x = i, y = j;
				bool arrow = false;
				x += dx[d];
				y += dy[d];
				while (inside(x, y)) {
					if (f[x][y] != '.') {
						arrow = true;
						break;
					}
					x += dx[d];
					y += dy[d];
				}
				if (!arrow)
					continue;
				possible = true;
				cost = min(cost, int(d != myd));
			}
			if (!possible) {
				cout << "IMPOSSIBLE";
				return;
			}
			ans += cost;
		}
	}
	cout << ans;
}

int main() {
	int tcase;
	cin >> tcase;
	for (int t = 0; t < tcase; ++t) {
		cout << "Case #" << (t + 1) << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}
