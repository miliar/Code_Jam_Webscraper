#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

int n;

pair<ll, ll> rangeFor(ll index, int level)
{
	if (level == 0) return make_pair(0LL, (1LL << n) - 1);
	pair<ll, ll> pp = rangeFor(index/2, level - 1);
	if (index % 2 == 1)
		pp.first = pp.first * 2 + 1;
	else
		pp.second &= (pp.second - 1);
	return pp;
}

pair<ll, ll> solve(int nn, ll p)
{
	n = nn;
	p--;
	ll maxi = -1;
	int level = n;
	ll i = p;
	while (i >= 0) {
		maxi = max(maxi, rangeFor(i, level).second);
		if (i % 2) {
			maxi = max(maxi, rangeFor(i - 1, level).second);
		}
		i = i/2 - 1;
		level--;
	}
	ll mini = (1LL << n);
	i = p + 1;
	level = n;
	while (i < (1LL << level)) {
		mini = min(mini, rangeFor(i, level).first);
		if (i % 2 == 0)
			mini = min(mini, rangeFor(i + 1, level).first);
		i = i/2 + 1;
		level--;
	}
	
	return make_pair(mini-1, maxi);
}

int main(void)
{
// 	freopen("/home/vesko/gcj/b.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		int n; ll p;
		scanf("%d%lld", &n, &p);
		pair<ll, ll> pf = solve(n, p);
		printf("%lld %lld\n", pf.first, pf.second);
	}
	/*
	int a[16] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
	int mini[5][16];
	int maxi[5][16];
	FOR(i, 5) FOR(j, 16) {
		mini[i][j] = 999;
		maxi[i][j] = -999;
	}
	int cnt=0;
	do {
		int b[16];
		FOR(i, 16) b[i] = a[i];
		FOR(j, 5) {
			int d = 16>>j;
			FOR(i, 16) mini[j][i/d] = min(mini[j][i/d], b[i]);
			FOR(i, 16) maxi[j][i/d] = max(maxi[j][i/d], b[i]);
			int c[16];
			FOR(i, 8) {
				c[0 + i] = min(b[i * 2], b[i * 2 + 1]);
				c[8 + i] = max(b[i * 2], b[i * 2 + 1]);
			}
			memcpy(b, c, sizeof(b));
		}
		random_shuffle(a, a + 16);
		if (cnt++ == 10000000) {
			cnt = 0;
			printf("\n====================\n\n");
			FOR(j, 5) {
				int setsize = 16>>j;
				FOR(i, 1<<j) {
					printf("Level %d, from [%d..%d], min = %d, max = %d\n", j, i * setsize, (i + 1) * setsize - 1, mini[j][i], maxi[j][i]);
				}
			}
		}
	} while(1);
	*/
	return 0;
}
