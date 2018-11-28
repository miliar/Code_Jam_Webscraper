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

ll T, K, C, S;

void solve(ll t) {
	ll x = 1;
	for (ll i = 0; i < C - 1; i++) {
		x *= K;
	}

	printf("Case #%lld:", t + 1);
	for (ll i = 0, p = 1; i < K; i++, p += x) {
		printf(" %lld", p);
	}
	printf("\n");
}

int main() {
	cin >> T;
	rep(i, T) {
		cin >> K >> C >> S;
		solve(i);
	}
	return 0;
}


