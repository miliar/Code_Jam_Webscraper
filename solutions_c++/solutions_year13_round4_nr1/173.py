#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

#define INF (1<<29)
typedef long long ll;

const int MAXM = 1500;
const ll MOD = 1000002013;

struct Event {
	Event(): station(-1), delta(0) {}
	Event(int st, ll d): station(st), delta(d) {}
	int station;
	ll delta;
	bool operator < (const Event &e) const {
		if (station == e.station) {
			return delta > e.delta;
		}
		return station < e.station;
	}
};

int T, N, M;
vector<Event> events;

ll norm(ll a) {
	if (a < 0) a += MOD;
	if (a >= MOD) a-= MOD;
	return a;
}

ll sum1To(ll to) {
	return (to*(to+1)/2)%MOD;
}

ll sum(ll from, ll to) {
	if (from > to) return 0;
	return norm(sum1To(to) - sum1To(from-1));
}

ll costFor(int from, int to, ll count) {
	int dist = to-from;
	return (count*sum(N-dist+1, N))%MOD;
}

ll ssum(const multiset<Event> &s) {
	ll tot = 0;
	for (const Event &e : s) {
		tot += e.delta;
	}
	return tot;
}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d%d", &N, &M);
		ll orig = 0;
		REP(m,M) {
			int from, to;
			ll count;
			scanf("%d%d%lld", &from, &to, &count);
			events.push_back(Event(from, count));
			events.push_back(Event(to, -count));
			orig += costFor(from, to, count);
			orig %= MOD;
		}

		sort(events.begin(), events.end());

		ll total = 0;
		multiset<Event> rem;

		for (Event &e : events) {
			int st = e.station;
			ll delta = e.delta;
			if (delta > 0) {
				rem.insert(e);
			} else {
				delta = -delta;
				while (delta > 0) {
					if (rem.empty()) DEBUG("AAA");
					auto it = --rem.end();
					Event drop = *it;
					rem.erase(it);
					if (drop.delta > delta) {
						total += costFor(drop.station, st, delta);
						drop.delta -= delta;
						delta = 0;
						rem.insert(drop);
					} else if (drop.delta < delta) {
						total += costFor(drop.station, st, drop.delta);
						delta -= drop.delta;
					} else {
						total += costFor(drop.station, st, delta);
						delta = 0;
					}
					total %= MOD;
				}
			}
		}

		events.clear();
		printf("Case #%d: %lld\n", t+1, norm(orig - total));
	}
	return 0;
}
