#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <assert.h>
#include <set>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

const double INF = 1e99;

double g(double avail, double bets[], int n, ll level, int addon)
{
	if (level == 0) return 0;
	double a[37] = {0};
	FOR(i, n) a[i] = bets[i];
	ll myBet[37] = {0};
	ll spent = 0;
	FOR(i, 37) {
		if (a[i] > level) continue;
		myBet[i] = level - a[i];
		avail -= myBet[i];
		spent += myBet[i];
		a[i] = level;
	}
	if (avail < 0) return -INF;
	vector<pair<ll, int> > vv;
	FOR(i, 37) {
		if (a[i] == level) vv.push_back(make_pair(myBet[i], i));
	}
	
	if (addon > avail) return -INF;
	if (addon > (int) vv.size()) return -INF;
	sort(vv.begin(), vv.end());
	FOR(i, addon) {
		a[vv[i].second]++;
		spent++;
	}
	int nBets = 0;
	FOR(i, 37) if (a[i] == level) nBets++;
	if (nBets == 0) return -INF;
	double expect = 0;
	FOR(i, 37) {
		assert(a[i] >= level);
		if (a[i] == level) {
			expect += myBet[i] * 36.0 / nBets;
		}
	}
	return expect - spent;
}

double f(double avail, double bets[], int n, ll level)
{
	double maxProfit = -INF;
	FOR(addon, n + 1) {
		maxProfit = max(maxProfit, g(avail, bets, n, level, addon));
	}
	return maxProfit;
}

double ternary(double avail, double bets[], int n, ll L, ll R)
{
	double answer = -INF;
	while (R - L > 10) {
		ll p1 = (2 * L + 1 * R) / 3;
		ll p2 = (1 * L + 2 * R) / 3;
		double f1 = f(avail, bets, n, p1);
		double f2 = f(avail, bets, n, p2);
		answer = max(answer, f1);
		answer = max(answer, f2);
		if (f1 > f2)
			R = p2;
		else
			L = p1;
	}
	for (ll x = 0; x <= 1000; x++) {
		answer = max(answer, f(avail, bets, n, x));
	}
	for (ll x = L; x <= R; x++) {
// 		printf("%lld -> %.10lf\n", x, f(avail, bets, n, x));
		answer = max(answer, f(avail, bets, n, x));
	}
	return answer;
}

void solve(void)
{
	double avail;
	int n;
	double bets[37];
	scanf("%lf%d", &avail, &n);
	FOR(i, n) scanf("%lf", &bets[i]);
	double maxProfit = -INF;
 	ll L = 0, R = (ll) 1e13;
 	while (L != R) {
 		ll M = (L + R + 1) / 2;
 		if (f(avail, bets, n, M) <= -INF)
 			R = M - 1;
 		else
 			L = M;
 	}
 	set<ll> all;
 	all.insert(R);
 	all.insert(0);
 	FOR(i, n)
 		all.insert(bets[i]);
 	vector<ll> z;
 	for (set<ll>::iterator i = all.begin(); i != all.end(); ++i)
 		z.push_back(*i);
 	int k = (int) z.size();
 	FOR(i, k - 1) {
 		maxProfit = max(maxProfit, ternary(avail, bets, n, z[i], z[i + 1]));
 	}
 	
/* 	double xMaxProfit = -INF;
 	FOR(i, 1024)
 		xMaxProfit = max(xMaxProfit, f(avail, bets, n, i));
 	if (xMaxProfit != maxProfit) {
 		printf("Boo: %lf vs %lf\n", xMaxProfit, maxProfit);
 	}
 	*/
	printf("%.10lf\n", maxProfit);
}

int main(void)
{
//  	freopen("/home/vesko/gcj/A-small-attempt1.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}

