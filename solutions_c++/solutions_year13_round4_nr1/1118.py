#include <map>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;
const LL MOD = 1000002013ll;

map <pair<LL, LL>, LL> s, tmp;
map <pair<LL, LL>, LL>::iterator it, jt;
LL n, m;
LL o, e, p;

LL lost1(LL o1, LL e1) {
	LL x = e1 - o1;
	LL r = n * x - x * (x - 1) / 2;
	return r;
}

LL lost(LL o1, LL e1, LL o2, LL e2) {
	LL r1 = (lost1(o1, e1) + lost1(o2, e2)); //% MOD;
	LL r2 = (lost1(o1, e2) + lost1(o2, e1)); //% MOD;
	LL r = (r1 - r2); //% MOD;
	return r;
}

int main() {
	int tc, cn = 0;	

	scanf("%d", &tc);
	while (tc--) {
		s.clear();
		scanf("%lld%lld", &n, &m);
		for (int i=0; i<m; ++i) {
			scanf("%lld%lld%lld", &o, &e, &p);
			s[make_pair(o, e)] += p;
		}
		LL tot = 0;
		while (true) {
//			tmp = s;
			bool ff = false;
			for (it=s.begin(); it!=s.end(); ++it) {
				for (jt=s.begin(); jt!=s.end(); ++jt) {
					LL o1 = it->first.first, e1 = it->first.second, p1 = it->second;
					LL o2 = jt->first.first, e2 = jt->first.second, p2 = jt->second;
					p = min(p1, p2);
					if (p == 0) continue;
					if (o1 <= o2 && o2 <= e1) {
						LL lose = lost(o1, e1, o2, e2);
						if (lose <= 0) continue;
						lose %= MOD;
						tot = (tot + lose * p) % MOD;

						s[make_pair(o1, e1)] -= p;
						s[make_pair(o2, e2)] -= p;
						s[make_pair(o1, e2)] += p;
						s[make_pair(o2, e1)] += p;

						ff = true;
					}
				}
			}
//			s = tmp;
			if (!ff) break;
		}
		printf("Case #%d: %lld\n", ++cn, tot);
	}

	return 0;
}
