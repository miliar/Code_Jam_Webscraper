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

int main() {
	int T, n;
	double x, v;
	cin >> T;
	rep(X, 0, T) {
		cin >> n >> v >> x;
		vd c(n), r(n);
		rep(i, 0, n)
			cin >> r[i] >> c[i];

		if (n == 1) {
			if (abs(c[0] - x) < eps)
				printf("Case #%d: %.8lf\n", X + 1, v / r[0]);
			else
				printf("Case #%d: IMPOSSIBLE\n", X + 1);
		} else {
			double rate = 0;
			if (abs(c[0] - x) < eps)
				rate += r[0];
			if (abs(c[1] - x) < eps)
				rate += r[1];
			if (rate > 0) {
				printf("Case #%d: %.8lf\n", X + 1, v / rate);
			} else {
				if (c[0] > c[1]) {
					swap(r[0], r[1]);
					swap(c[0], c[1]);
				}
				if (c[1] < x - eps || c[0] > x + eps) {
					printf("Case #%d: IMPOSSIBLE\n", X + 1);
				} else {
					double t1 = (x - c[0]) * v / (c[1] - c[0]) / r[1];
					double t2 = (x - c[1]) * v / (c[0] - c[1]) / r[0];
					printf("Case #%d: %.8lf\n", X + 1, max(t1, t2));
				}
			}
		}
	}
}
