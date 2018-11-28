#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using u32 = uint32_t;
using vi = vector<int>;    using vvi = vector<vi>;
using vb = vector<bool>;   using vvb = vector<vb>;
using vl = vector<ll>;     using vvl = vector<vl>;
using vd = vector<double>; using vvd = vector<vd>;

#define MAXC(c, x) (c = max(c, x))
#define MINC(c, x) (c = min(c, x))

#define REP(i,n) for(auto i = 0 * (n), i##_len = (n); i < i##_len; ++i)
#define ALL(c) (c).begin(), (c).end()
#define FOR(i,s,n) for(ll i=s, i##_len=(ll)(n); i<i##_len; ++i)
#define TEN(x) ((ll)1e##x)
const ll mod = TEN(9) + 7;

const ll INF = 1e9;

int main() {
	#ifdef INPUT_FROM_FILE
	ifstream cin("sample.in");
	ofstream cout("sample.out");
	#endif
	cin.tie(0);
	ios_base::sync_with_stdio(false);
	cout << fixed << setprecision(50);

	ll n; cin >> n;
	REP(i, n) {
		string s; ll k;
		cin >> s >> k;
		ll cnt = 0;
		REP(j, s.size() - k + 1) if(s[j] == '-') {
			cnt++;
			REP(l, k) s[j + l] = s[j + l] == '-' ? '+' : '-';
		}
		cout << "Case #" << i + 1 << ": ";
		if ([&] {
			REP(j, s.size()) if (s[j] == '-') {
				cout << "IMPOSSIBLE" << endl;
				return 0;
			}
			return 1;
		}()) {
			cout << cnt << endl;
		}
	}

}