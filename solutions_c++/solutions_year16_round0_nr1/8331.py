#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <numeric>
#include <bitset>
#include <complex>
#define rep(x, to) for (int x = 0; x < (to); x++)
#define REP(x, a, to) for (int x = (a); x < (to); x++)
#define foreach(itr, x) for (typeof((x).begin()) itr = (x).begin(); itr != (x).end(); itr++)
#define EPS (1e-14)
#define _PA(x,N) rep(i,N){cout<<x[i]<<" ";}cout<<endl;
#define _PA2(x,H,W) rep(i,(H)){rep(j,(W)){cout<<x[i][j]<<" ";}cout<<endl;}

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef complex<double> Complex;
typedef vector< vector<int> > Mat;

ll T;
ll N;
ll ans;

void add(set<ll> &S, ll x) {
	while (x != 0) {
		S.insert(x % 10);
		x /= 10;
	}
}

ll solve() {
	if (N == 0) {
		return -1;
	}

	set<ll> S;
	ll p = 1;
	while (S.size() != 10) {
		add(S, p * N);
		p++;
	}

	return (p - 1) * N;
}

int main() {
	cin >> T;
	rep(i, T) {
		cin >> N;
		ans = solve();
		if (ans == -1) {
			printf("Case #%d: INSOMNIA\n", i + 1);
		} else {
			printf("Case #%d: %lld\n", i + 1, ans);
		}
	}
	return 0;
}


