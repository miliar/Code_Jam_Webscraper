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

const ll MOD = 1000002013;

enum { OPEN, CLOSE };

struct Ev {
	int where;
	int type;
	int count;
	Ev() {}
	Ev(int w, int t, int c) : where(w), type(t), count(c) {}
	inline bool operator < (const Ev& rhs) const
	{
		if (where != rhs.where) return where < rhs.where;
		return type < rhs.type;
	}
};

inline ll costFunc(ll C, ll diff)
{
	return (C*diff - (diff * (diff - 1)) / 2) % MOD;
}

ll solve(void)
{
	ll n;
	int m;
	static ll o[1024], e[1024], p[1024];
	scanf("%lld%d", &n, &m);
	FOR(i, m) {
		scanf("%lld%lld%lld", o + i, e + i, p + i);
	}
	vector<Ev> evs;
	FOR(i, m) {
		evs.push_back(Ev(o[i], OPEN, p[i]));
		evs.push_back(Ev(e[i], CLOSE, p[i]));
	}
	sort(evs.begin(), evs.end());
	//
	vector<pair<int, int> > current; // cost, count
	ll totalCost = 0;
	REP(i, evs) {
		if (i && evs[i - 1].where != evs[i].where) {
			ll diff = evs[i].where - evs[i - 1].where;
			REP(j, current) totalCost = ((totalCost + (costFunc(current[j].first, diff) * current[j].second) % MOD) % MOD);
			REP(j, current) current[j].first -= diff;
		}
		if (evs[i].type == OPEN) {
			current.push_back(make_pair((int) n, evs[i].count));
		} else {
			int toRemove = evs[i].count;
			while (toRemove > 0) {
				if (toRemove >= current.back().second) {
					toRemove -= current.back().second;
					current.pop_back();
				} else {
					current.back().second -= toRemove;
					toRemove = 0;
				}
			}
		}
	}
	ll totalCostUnmodified = 0;
	FOR(i, m) {
		totalCostUnmodified = ((totalCostUnmodified + (costFunc(n, e[i] - o[i]) * p[i]) % MOD) % MOD);
	}
	ll res = totalCostUnmodified + MOD - totalCost;
	return res;
}

int main(void)
{
// 	freopen("/home/vesko/gcj/a.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: %d\n", tc, (int) (solve() % (ll) MOD));
	}
	return 0;
}
