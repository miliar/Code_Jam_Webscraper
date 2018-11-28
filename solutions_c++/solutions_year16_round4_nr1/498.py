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

string construct(char c, int d) {
	if (d == 0)
		return string(1, c);
	string s1, s2;
	if (c == 'R') {
		s1 = construct('R', d - 1);
		s2 = construct('S', d - 1);
	} else if (c == 'S') {
		s1 = construct('S', d - 1);
		s2 = construct('P', d - 1);
	} else if (c == 'P') {
		s1 = construct('P', d - 1);
		s2 = construct('R', d - 1);
	}

	if (s1 < s2)
		return s1 + s2;
	else
		return s2 + s1;
}

int main() {
	int T, n, p, r, s;
	cin >> T;
	rep(X, 1, T + 1) {
		cin >> n >> r >> p >> s;
		string init = "RPS", ans = "Z";
		irep(c, init) {
			string tour = construct(c, n);
			int ri = 0, pi = 0, si = 0;

			irep(t, tour) {
				if (t == 'R')
					ri++;
				else if (t == 'P')
					pi++;
				else if (t == 'S')
					si++;
			}
			if (ri == r && pi == p && si == s) {
				if (tour < ans)
					ans = tour;
			}
		}

		if (ans == "Z")
			printf("Case #%d: IMPOSSIBLE\n", X);
		else
			printf("Case #%d: %s\n", X, ans.c_str());
	}
}
