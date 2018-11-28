//In the name of God

#include <bits/stdc++.h>

using namespace std;


typedef long long ll;
typedef pair<int, int> pii;

template<class P, class Q> inline P smin(P &a, Q b) { if (b < a) a = b; return a; }
template<class P, class Q> inline P smax(P &a, Q b) { if (a < b) a = b; return a; }

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define int long long
const int N = 1e3 + 5;

ofstream fout("a.out");
#define cout fout

int read() { int x; cin >> x; return x; }

int mark[N];

int32_t main() {
	ios_base :: sync_with_stdio(false); cin.tie(0); cout.tie(0);
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		memset(mark, 0, sizeof mark);
		cout << "Case #" << tt << ": ";
		int k, c, s;
		cin >> k >> c >> s;
		int kc = 1;
		if (s * c < k) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		int cur = 0;
		rep(i, s) {
			long long p = 0;
			rep(j, c)
				p *= k, p += min(k - 1, cur), cur = min(cur + 1, k);
			cout << p + 1 << ' ';
			if (cur == k)
				break;
		}
		cout << '\n';
	}
}













