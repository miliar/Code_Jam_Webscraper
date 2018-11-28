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

		int ex, er, ec;
		scanf("%d%d%d", &ex, &er, &ec);
		if (er > ec) {
			int t = er;
			er = ec;
			ec = t;
		}
		if ((er * ec) % ex != 0)
			printf("Case #%d: RICHARD\n", ecount);
		else {
			if (ex <= 2)
				printf("Case #%d: GABRIEL\n", ecount);
			else if (ex <= 3) {
				if (er <= 1)
					printf("Case #%d: RICHARD\n", ecount);
				else
					printf("Case #%d: GABRIEL\n", ecount);
			}
			else {
				if (er <= 2)
					printf("Case #%d: RICHARD\n", ecount);
				else
					printf("Case #%d: GABRIEL\n", ecount);
			}
		}
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
