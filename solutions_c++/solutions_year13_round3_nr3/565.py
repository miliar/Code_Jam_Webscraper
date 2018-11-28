#include <cstdio>
#include <algorithm>
using namespace std;

struct Attack {
	int day, w, e, str;
	bool operator <(const Attack b) const {
		return day < b.day;
	}
};

struct Range {
	int from, to, str, day;
};
Attack att[1000000];
Range rg[10000];

int main() {
	int tc;
	scanf("%d", &tc);
	for(int cs=1; cs<=tc; cs++) {
		printf("Case #%d: ", cs);
		int tribe, ai = 0;
		scanf("%d", &tribe);
		for(int i=0; i<tribe; i++) {
			int d, n, w, e, s, Dd, Dp, Ds;
			scanf("%d %d %d %d %d %d %d %d", &d, &n, &w, &e, &s, &Dd, &Dp, &Ds);
			for(int j=0; j<n; j++) {
				Attack a;
				a.day = d;
				a.w = w;
				a.e = e;
				a.str = s;
				d += Dd;
				w += Dp;
				e += Dp;
				s += Ds;
				att[ai++] = a;
			}
		}
		sort(att, att+ai);
		int success=0, ri=0;
		
		for(int i=0; i<ai; i++) {
			Attack c = att[i];
			Range avail;
			bool can = true;
			avail.from = c.w;
			avail.to = c.e;
			for(int j=0; j<ri; j++) {
				Range &cr = rg[j];
				if(cr.day < c.day && cr.from <= avail.from && avail.from <= cr.to && cr.str >= c.str) {
					avail.from = cr.to;
					if(avail.from >= avail.to) {
						can = false;
						break;
					}
				} else if (cr.day < c.day && cr.from <= avail.to && avail.to <= cr.to && cr.str >= c.str) {
					avail.to = cr.from;
					if(avail.from >= avail.to) {
						can = false;
						break;
					}
				} 
			}
			if(can) {
				Range ra;
				ra.from = c.w;
				ra.to = c.e;
				ra.str = c.str;
				ra.day = c.day;
				rg[ri++] = ra;
				success++;
			}
		}

		printf("%d\n", success);
	}
	return 0;
}
