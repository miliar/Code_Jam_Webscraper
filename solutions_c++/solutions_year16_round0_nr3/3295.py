#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for(int i=0; i<int(n); ++i)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
typedef long long ll;



ll modpow(ll b, ll p, ll mod) { assert(p>=0 && mod>=2); ll a=1; for(ll k=b%mod; p; p>>=1, k=k*k%mod) if (p&1) a=a*k%mod; return a; }

int TC;
void solve() {
	int N, J;
	cin >> N >> J;
	cout << endl;

	vector<int> keep = { 2, 3, 5, 7, 11 };
	for(ll s=0; s<=1LL<<N; s++) {
		if ((s&1) == 0) continue;
		if ((s>>(N-1)&1) == 0) continue;
		vector<ll> ans;
		for(int k=2; k<=10; k++) {
			vector<int> rem(sz(keep));
			rep(i, N) {
				rep(j, sz(keep)) {
					rem[j] += (modpow(k, i, keep[j]) * ((s>>i) & 1));
					rem[j] %= keep[j];
				}
			}
			int j = 0;
			for(; j<sz(keep); j++) if (rem[j] == 0) break;
			if (j == sz(keep)) break;
			ans.push_back(keep[j]);
		}
		if (sz(ans) != 9) continue;
		rep(i, N) cout << (s>>(N-1-i)&1); cout << ' ';
		rep(i, sz(ans)) {
			if (i) cout << ' ';
			cout << ans[i];
		}
		cout << endl;
		J--;
		if (J <= 0) break;
	}
}
int main() {
	int T; cin >> T;
	for(int TC=1; TC<=T; TC++) {
		cout << "Case #" << TC << ": ";
		solve();
	}
}

