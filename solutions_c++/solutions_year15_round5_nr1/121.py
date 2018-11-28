#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vb> vvb;
typedef vector<vs> vvs;
typedef vector<vl> vvl;

int inf = 0x3f3f3f3f;
double eps = 10e-8;
ll mod = 1000000007ll;

#define rep(k, a, b) for (int k = (a); k < int(b); k++)
#define sz(a) int(a.size())
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define x first
#define y second
#define mi(r, c, v) vvi(r, vi(c, v))
#define rrep(k, a, b) for (int k = (a); k >= int(b); k--)
#define irep(k, a) for (auto& k : (a))
#define md(r, c, v) vvd(r, vd(c, v))
#define mb(r, c, v) vvb(r, vb(c, v))
#define ms(r, c, v) vvs(r, vs(c, v))
#define ml(r, c, v) vvl(r, vl(c, v))
#define mc(r, c, v) vs(r, string(c, v))
#define add(i, j) ((i) + (j)) % mod
#define mul(i, j) ((i) * (j)) % mod
#define bits(n) int(__builtin_popcount(n))

auto ls = [](pii p1, pii p2) -> bool {return p1.y < p2.y ? true : (p1.y > p2.y ? false : (p1.x < p2.x ? true : false)); };

int main() {
	int T, n, d, as, cs, rs, am, cm, rm;
	cin >> T;
	rep(X, 0, T) {
		cin >> n >> d;
		vi s(n), m(n);
		vector<pii> win(n);
		cin >> s[0] >> as >> cs >> rs;
		cin >> m[0] >> am >> cm >> rm;
		win[0] = { s[0], s[0] };

		rep(i, 1, n) {
			s[i] = (s[i - 1] * as + cs) % rs;
			m[i] = (m[i - 1] * am + cm) % rm;
			win[i] = { min(win[m[i] % i].x, s[i]), max(win[m[i] % i].y, s[i]) };
		}
		sort(all(win));

		int result = 0;
		priority_queue <pii, vector<pii>, decltype(ls)> q(ls);
		rrep(i, n - 1, 0) {
			q.push(win[i]);
			int up = win[i].x + d;
			while (!q.empty() && q.top().y > up)
				q.pop();
			result = max(result, sz(q));
		}
		printf("Case #%d: %d\n", X + 1, result);
	}
}
