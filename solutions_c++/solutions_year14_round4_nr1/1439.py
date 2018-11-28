// .... .... .....!
// ...... ......!
// .... ....... ..... ..!

#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define sz(x) (int((x).size()))
#define pb push_back
#define all(X) (X).begin(),(X).end()
#define X first
#define Y second

template<class P, class Q> inline void smin(P &a, Q b) { if (b < a) a = b; }
template<class P, class Q> inline void smax(P &a, Q b) { if (a < b) a = b; }

typedef long long ll;
typedef pair<int, int> pii;

////////////////////////////////////////////////////////////////////////////////

const int maxn = 10000 + 100;

int n;
int x;
int s[maxn];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int tt; cin >> tt;
	for(int tc = 1; tc <= tt; tc++) {
		cin >> n >> x;
		rep(i, n) cin >> s[i];
		sort(s, s+n);

		int ans = 0;
		int p = n-1;
		rep(i, n) {
			if(i > p) break;
			while(p > i && s[i] + s[p] > x) p--, ans++;
			if(p > i) p--, ans++;
			else { ans++; break; }
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}

	{ return 0; }
}

