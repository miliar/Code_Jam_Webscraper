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
using namespace std;

#define REP(i, m, n) for(int i=(m); i<int(n); ++i)
#define rep(i, n) for(int i=0; i<int(n); ++i)
#define each(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define pb push_back                                                                          
#define mp make_pair
#define def(a, x) __typeof(x) a = x
#define fi first
#define se second
typedef long long ll;
typedef pair<ll, ll> PI;
const int dx[] = {1, 0, -1, 0, 1, 1, -1, -1}, dy[] = {0, 1, 0, -1, 1, -1, 1, -1};


//#include <debug.h>
const ll MOD = 1000002013;
vector<PI> A;
ll rec(int l, int r) {
	if (l+1 >= r) return 0;
	ll m = 1e10;
	ll a = l;
	ll c = A[l].second;
	for(int i=l+1; i<r ; i++) {
		if (m > c) {
			m = c;
			a = i;
		}
		c += A[i].second;
	}
//	cout << A << endl;
//	cout << l << " " << r << " " << c << endl;
	assert(c == 0);

	A[l].second -= m;
	A[r-1].second += m;
	ll d = A[r-1].first - A[l].first;
	ll S = 0;
	S += (d-1)*d/2 % MOD * m %MOD;
	S += rec(l, a);
	S %= MOD;
	S += rec(a, r);
	S %= MOD;
	return S;
}
ll solve() {
	ll N, M;
	cin >> N >> M;
	map<ll, ll> B;
	ll S = 0;
	rep(i, M) {
		ll a, b, c;
		cin >> a >> b >> c;
		B[a] += c;
		B[b] += -c;
		S -= (b-a-1)*(b-a)/2 %MOD * c % MOD;
		S %= MOD;
	}

	A.clear();
	each(it, B) if (it->second) A.pb(mp(it->first, it->second));
//	cout << A << endl;
	S += rec(0, sz(A)) % MOD;
	S %= MOD;
	return (S%MOD+MOD)%MOD;
}

int main() {
	int T; cin >> T;
	for(int t=1; t<=T; t++)
		cout << "Case #" << t << ": " << solve() << endl;
}

