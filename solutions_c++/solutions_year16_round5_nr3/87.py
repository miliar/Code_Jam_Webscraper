#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void solve() {
	static int tc = 1;
	cout << "Case #" << tc << ": ";
	tc++;
	int N, S;
	cin >> N >> S;
	vector<vi> pos(N, vi(3));
	vector<vi> vel(N, vi(3));
	rep(i,0,N) {
		rep(j,0,3) cin >> pos[i][j];
		rep(j,0,3) cin >> vel[i][j];
	}
	auto D = [&](int a, int b) {
		double delta = 0;
		rep(i,0,3) {
			double d = pos[a][i] - pos[b][i];
			delta += d * d;
		}
		return sqrt(delta);
	};
	vector<double> dist(N, 1e9);
	set<pair<double, int>> Q;
	dist[0] = 0;
	Q.emplace(0.0, 0);
	while (!Q.empty()) {
		pair<double, int> cur = *Q.begin();
		Q.erase(Q.begin());
		rep(i,0,N) {
			double nd = max(cur.first, D(cur.second, i));
			if (nd < dist[i]) {
				if (dist[i] != 1e9) {
					Q.erase(pii(dist[i], i));
				}
				dist[i] = nd;
				Q.emplace(dist[i], i);
			}
		}
	}
	cout << fixed << setprecision(9);
	cout << dist[1] << endl;
}

int main() {
	int N;
	cin.sync_with_stdio(false);
	cin >> N;
	while (N --> 0) solve();
}
