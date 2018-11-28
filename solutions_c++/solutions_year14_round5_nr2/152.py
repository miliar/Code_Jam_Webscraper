#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <map>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

int n, p, q;
int h[101], g[101];
int beststrategy[250];

int dp[101][1101];

int f(int pos, int movesToSpare)
{
	if (pos == n) return 0;
	movesToSpare = min(movesToSpare, 1100);
	int& d = dp[pos][movesToSpare];
	if (d != -1) return d;
	d = 0;
	// can we take out the current monster?
	if (movesToSpare >= beststrategy[h[pos]])
		d = max(d, g[pos] + f(pos + 1, movesToSpare - beststrategy[h[pos]]));
	// skip the current monster?
	d = max(d, f(pos + 1, movesToSpare + (h[pos] - 1) / q + 1));
	return d;
}

int solve(void)
{
	memset(beststrategy, 0x1f, sizeof(beststrategy));
	for (int H = 1; H <= 200; H++)
		for (int preDiana = 0; preDiana <= 10; preDiana++)
			for (int kula = 0; kula <= 10; kula++)
				if (H - preDiana * p > 0 && H - preDiana * p - kula * q > 0 && H - (preDiana + 1) * p - kula * q <= 0)
					beststrategy[H] = min(beststrategy[H], preDiana + 1 - kula);
	
	//
	memset(dp, 0xff, sizeof(dp));
	return f(0, 1);
}

int main(void)
{
// 	freopen("/home/vesko/gcj/b.in", "rt", stdin);
	int TC;
	cin >> TC;
	for (int T = 1; T <= TC; T++) {
		cin >> p >> q >> n;
		FOR(i, n) cin >> h[i] >> g[i];
		printf("Case #%d: %d\n", T, solve());
	}
	return 0;
}
