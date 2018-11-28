#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for(int i = 0;i < n;++i)
#define FOR(i, a, b) for(int i = a;i < b;++i)

const int MAX = 1010;
int n, a[MAX], m, sol;

int f(int x) {
	int r = 0;
	REP(i, n) if(a[i] > x) r += a[i] % x ? a[i]/x: a[i]/x - 1;
	return r + x;
}

int solve() {
	m = 0; sol = MAX;
	REP(i, n) m = max(m, a[i]);
	FOR(i, 1, m + 1) sol = min(sol, f(i));
	return sol;
}

int main() {
	int t;
	cin >> t;
	REP(i, t) {
		cin >> n;
		REP(i, n) cin >> a[i];
		cout << "Case #" << i + 1 << ": " << solve() << "\n";
	}
}