#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iomanip>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

typedef pair<int, int> pii;
typedef long long ll;

int N, K;
double P[200];
double take[200];
double res = 0;
double best = 0;

int as, bs;
void rec(int ind, double d) {
	if (ind >= K) {
		// cout << d << endl;
		res += d;
		return;
	}
	if (as > 0) {
		as--;
		rec(ind + 1, d * take[ind]);
		as++;
	}
	if (bs > 0) {
		bs--;
		rec(ind + 1, d * (1 - take[ind]));
		bs++;
	}
}

void rec1(int ind, int took) {
	if (took > K) return;
	if (ind >= N) {
		if (took != K) return;
		res = 0;
		rec(0, 1);
		best = max(res, best);
		return;
	}
	if (N - ind < K - took) return;
	rec1(ind + 1, took);
	take[took] = P[ind];
	rec1(ind + 1, took + 1);
}

void solve() {
	cin >> N >> K;
	res = 0;
	best = 0;
	REP(i, N) {
		cin >> P[i];
	}
	sort(P, P+N);
	REP(i, K/2) take[i] = P[i];
	reverse(P, P+N);
	REP(i, K/2) take[i + K/2] = P[i];
	as = bs = K / 2;
	rec1(0,0);
	// rec(0, 1);
	cout << fixed << setprecision(10) << best;
}

int main() {
	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << (i+1) << ": ";
		solve();
		cout << endl;
	}
}