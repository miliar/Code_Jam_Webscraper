#include <cstdio>
#include <queue>
#include <set>
#include <algorithm>
#include <assert.h>
using namespace std;

#define MOD 1000002013

struct point {
	int numpeople;
	int x;
	bool operator<(point const& o) const {
		return x < o.x;
	}
};

point on[1005];
point off[1005];
priority_queue<point> q;

int main() {
	int ncases;
	scanf("%d", &ncases);
	for (int casenum = 1; casenum <= ncases; casenum++) {
		int n, m;
		scanf("%d %d", &n, &m);
		long long normalCost = 0;
		for (int i = 0; i < m; i++) {
			int o, e, p;
			scanf("%d %d %d", &o, &e, &p);
			on[i].numpeople = p;
			off[i].numpeople = p;
			on[i].x = o;
			off[i].x = e;
			long long dist = e - o;
			long long perperson = (dist*n - ((dist-1)*dist)/2) % MOD;
			long long cost = (perperson * (long long) p) % MOD;
			normalCost = (normalCost + cost) % MOD;
		}
		sort(on, on + m);
		sort(off, off + m);
		int oni = 0, offi = 0;
		long long totalCost = 0;
		while (offi < m) {
			if (oni < m && on[oni].x <= off[offi].x) {
				q.push(on[oni]);
				oni++;
			} else {
				int c = off[offi].numpeople;
				int x = off[offi].x;
				offi++;
				while (c > 0) {
					assert(q.size() > 0);
					point p = q.top();
					q.pop();
					int quant;
					if (p.numpeople > c) {
						quant = c;
						p.numpeople -= c;
						c = 0;
						q.push(p);
					} else {
						quant = p.numpeople;
						c -= p.numpeople;
					}
					long long dist = x - p.x;
					long long perperson = (dist*n - ((dist-1)*dist)/2) % MOD;
					long long cost = (perperson * (long long) quant) % MOD;
					totalCost = (totalCost + cost) % MOD;
				}
			}
		}
		long long ans = (normalCost - totalCost) % MOD;
		if (ans < 0) ans += MOD;
		printf("Case #%d: %lld\n", casenum, ans);
	}
}
