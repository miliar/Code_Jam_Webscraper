#include <stdio.h>
#include <algorithm>

using namespace std;

struct A {
	double r, t;
	A(double _r = 0.0, double _t = 0.0) : r(_r), t(_t) {}
	bool operator < (const A &r) const {
		return t < r.t;
	}
};


double max(double a, double b) {
	if (a > b)
		return a;
	else
		return b;
}

int main(int argc, char *argv[]) {
	int ecase, ecount;
	int caseStart = -1, caseEnd = 9999999;
	scanf("%d", &ecase);

	if (argc > 1) {
		if (sscanf(argv[1], "%d", &caseStart) == 1) {
			if (argc > 2)
				sscanf(argv[2], "%d", &caseEnd);
		}
		if (caseEnd < caseStart)
			caseEnd = caseStart;
		if (caseEnd != 9999999 && caseEnd >= 1 && caseStart <= 0)
			caseStart = 1;
		if (caseStart > 0)
			fprintf(stderr, "....................DEBUG MODE ENABLED (FROM CASE %d to %d)\n", caseStart, caseEnd);
	}

	int en;
	double ev, et;
	A ef[100];

	for (ecount = 1; ecount <= ecase; ecount++) {
		if (ecount < caseStart || ecount > caseEnd)
			continue;
	
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d START\n", ecount);

		scanf("%d%lf%lf", &en, &ev, &et);
		for (int i = 0; i < en; i++) {
			double tr, tt;
			scanf("%lf%lf", &tr, &tt);
			ef[i] = A(tr, tt);
		}
		sort(ef, ef+en);

		if (en == 1) {
			if (ef[0].t == et)
				printf("Case #%d: %.10lf\n", ecount, ev / ef[0].r);
			else
				printf("Case #%d: IMPOSSIBLE\n", ecount);
		}
		else if (en == 2) {
			if (ef[0].t == et && ef[1].t == et) {
				printf("Case #%d: %.10lf\n", ecount, ev / (ef[0].r + ef[1].r));
			}
			else if (ef[0].t == et)
				printf("Case #%d: %.10lf\n", ecount, ev / ef[0].r);
			else if (ef[1].t == et)
				printf("Case #%d: %.10lf\n", ecount, ev / ef[1].r);
			else if (ef[0].t < et && et < ef[1].t) {
				double dt0 = et - ef[0].t;
				double dt1 = ef[1].t - et;
				double nv0 = ev * dt1 / (dt0 + dt1);
				double nv1 = ev * dt0 / (dt0 + dt1);
				double t0 = nv0 / ef[0].r;
				double t1 = nv1 / ef[1].r;
				double ans = max(t0, t1);
				//printf("nv01 %lf %lf  target: %lf\n", nv0, nv1, nv0 * ef[0].t );
				printf("Case #%d: %.10lf\n", ecount, ans);
			}
			else {
				printf("Case #%d: IMPOSSIBLE\n", ecount);
			}
		}
		else {
			fprintf(stderr, "case cannot handle\n");
			return 0;
		}
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
