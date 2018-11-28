#include <cstdio>
#include <algorithm>
#include <stack>
using namespace std;

#define MOD 1000002013ull;

struct evt {
	bool plus;
	int time;
	int count;
};

struct ticket {
	int from, count;
};

bool operator<(evt a, evt b) {
	if (a.time < b.time) return true;
	if (a.time == b.time && a.plus && !b.plus) return true;
	return false;
}

int n;

unsigned long long pr(unsigned long long d) {
	unsigned long long res = d*n; res %= MOD;
	unsigned long long tmp = d*(d-1)/2; tmp %= MOD;
	res += MOD; res -= tmp; res %= MOD;
	return res;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		unsigned long long should = 0, did = 0;
		
		int m;
		scanf("%d %d", &n, &m);
		evt evts[2*m];
		for (int i = 0; i < m; ++i) {
			int o, e, p;
			scanf("%d %d %d", &o, &e, &p);
			evts[2*i].plus = true;
			evts[2*i].time = o;
			evts[2*i].count = p;
			evts[2*i+1].plus = false;
			evts[2*i+1].time = e;
			evts[2*i+1].count = p;
			
			unsigned long long d = e-o;
			//printf("price: %llu * %d\n", pr(d), p);
			should += pr(d)*p; should %= MOD;
		}
		sort(evts, evts+2*m);
		//printf("total: %llu\n", should);
		
		stack<ticket> s;
		
		for (int i = 0; i < 2*m; ++i) {
			
			//printf("evts[%d] = (%d, %d, %d)\n", i, evts[i].plus, evts[i].time, evts[i].count);
			if (evts[i].plus) {
				ticket t; t.from = evts[i].time; t.count = evts[i].count;
				s.push(t);
			} else {
				int need = evts[i].count;
				while (need > 0) {
					ticket t = s.top(); s.pop();
					unsigned long long d = evts[i].time - t.from;
					unsigned long long price = 0;
					if (d > 0) price = pr(d);
					
					if (t.count > need) {
						//printf("using %d tickets from %d at %d (not all), paid: %llu * %d\n", need, t.from, evts[i].time, price, need);
						did += price*need; did %= MOD;

						t.count -= need;
						need = 0;
						s.push(t);
					} else {
						//printf("using %d tickets from %d at %d (all), paid: %llu * %d\n", t.count, t.from, evts[i].time, price, t.count);
						did += price*t.count; did %= MOD;

						need -= t.count;
					}
				}
			}
		}
		
		unsigned long long res = should + MOD;
		res -= did;
		res %= MOD;
		printf("Case #%d: %llu\n", tt, res);
	}
}
