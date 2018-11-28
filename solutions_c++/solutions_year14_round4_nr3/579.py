#include <iostream>
#include <cstdio>
#include <cassert>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <sstream>
#include <cstdlib>
#include <numeric>
#include <bitset>
#include <deque>
#include <iomanip>
using namespace std;

#define REP(i, m, n) for(int i=(m); i<int(n); ++i)
#define rep(i, n) for(int i=0; i<int(n); ++i)
#define each(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define FILL(a, c) fill_n(reinterpret_cast<__typeof(c)*>(a), sizeof(a) / sizeof(__typeof(c)), (c))
template<class T> void fill_n(const T *first, size_t n, const T &value) { for(; n>0; --n) *const_cast<T*>(first++) = value; }
#define pb push_back                                                                          
#define mp make_pair
#define def(a, x) __typeof(x) a = x
#define fi first
#define se second
typedef long long ll;
typedef pair<ll, ll> PI;
const int dx[] = {1, 0, -1, 0, 1, 1, -1, -1}, dy[] = {0, 1, 0, -1, 1, -1, 1, -1};

const int INF = 1<<29;

void solve() {
	int W, H, B;
	cin >> W >> H >> B;
	map<int, int> ys;
	pair<pair<int, int>, pair<int, int> > A[1010];
	rep(i, B) {
		int x0, x1, y0, y1;
		cin >> x0 >> y0 >> x1 >> y1;
		ys[y0] = ys[y1] = 0;
		rep(k, 7) ys[y0+k-3] = ys[y1+k-3] = 0;
		A[i] = mp(mp(x0, y0), mp(x1, y1));
	}
	int cnt=0;
	each(it, ys) it->second = cnt++;
	cnt = H; //
	int X[W+10][cnt+10];
	FILL(X, 0);
	rep(i, B) {
		int x0 = A[i].fi.fi, y0 = A[i].fi.se, x1 = A[i].se.fi, y1 = A[i].se.se;
//		y0 = ys[y0], y1 = ys[y1];
		for(int x=x0; x<=x1; x++)
		for(int y=y0; y<=y1; y++)
			X[x][y] = 1;
	}
	rep(i, cnt+10) X[W][i] = 1;

//	cout << W << " " << H << " " << B << endl;
//	rep(j, cnt) { rep(i, W) { cout << X[i][j] << " "; } cout << endl; }


	priority_queue<pair<int, pair<int, int> > > q;
	int dist[W+10][cnt+10];
	FILL(dist, INF);
	rep(i, cnt) q.push(mp(-!X[W][i], mp(W, i)));
	int ans = W;
	while(!q.empty()) {
		int d = -q.top().fi, x = q.top().se.fi, y = q.top().se.se;
		q.pop();
		if (x == 0) {
			ans = min(ans, d);
			continue;
		}
		if (dist[x][y] <= d) continue;
		dist[x][y] = d;
		rep(k, 8) {
			int ax = x+dx[k], ay = y+dy[k];
			if (0 <= ax && 0 <= ay && ax <= W && ay <= cnt)
				q.push(mp(-(d + !X[ax][ay]), mp(ax, ay)));
		}
	}
	cout << ans << endl;
}

int main() {
	int T; cin >> T;
	for(int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		solve();
	}
}

