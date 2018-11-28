#include <stdio.h>

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

	for (ecount = 1; ecount <= ecase; ecount++) {
		if (ecount < caseStart || ecount > caseEnd)
			continue;
	
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d START\n", ecount);


		double ec, ef, ex;
		scanf("%lf%lf%lf", &ec, &ef, &ex);
		double answer = ex / 2.0;
		double rate = 2.0;
		double pass = 0.0;
		while (true) {
			double nt = ec / rate;
			double newRate = rate + ef;
			double tnext = pass + nt + ex / (newRate);
			if (pass + nt > answer)
				break;
			if (tnext < answer)
				answer = tnext;
			pass += nt;
			rate += ef;
		}
		printf("Case #%d: %.7lf\n", ecount, answer);
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
