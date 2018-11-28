#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vl = vector<ll>;
using vvl=vector<vl>;
using vb=vector<bool>;
using vs=vector<string>;
using pll=pair<ll,ll>;
const ll oo = 0x3f3f3f3f3f3f3f3fLL;
const double eps = 1e-9;
#define sz(c) ll((c).size())
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define FR(i,a,b) for(ll i = (a); i < (b); i++)
#define FRD(i,a,b) for(ll i = ll(b)-1;i>=(a);i--)
#define TR(X) ({if(1) cerr << "TR: " << (#X) << " = " << (X) << endl; })

int main() {
	ios_base::sync_with_stdio(false);
	int tc;
	cin >> tc;
	FR(a,0,tc) {
		string s;
		int k;
		cin >> s >> k;
		int idx = 0;
		int changes = 0;
		while(idx <= s.size() - k) {
			if(s[idx] == '-') {
				FR(b,idx,idx+k) {
					s[b] = '-' + '+' - s[b];
				}
				changes++;
			}
			idx++;
		}
		bool bad = false;
		FR(b,idx,s.size()) {
			if(s[b] == '-') {
				bad = true;
				break;
			}
		}
		if(bad) {
			cout << "Case #" << a+1 << ": IMPOSSIBLE\n";
		} else {
			cout << "Case #" << a+1 << ": " << changes << '\n';
		}
	}
}
