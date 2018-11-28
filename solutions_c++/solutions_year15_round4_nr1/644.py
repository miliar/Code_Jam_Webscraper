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



	int dirIdx[256];
	dirIdx['^'] = 0;
	dirIdx['>'] = 1;
	dirIdx['v'] = 2;
	dirIdx['<'] = 3;
	
	int gor[4];
	int goc[4];
	gor[0] = -1;   goc[0] = 0;
	gor[1] = 0;    goc[1] = 1;
	gor[2] = 1;    goc[2] = 0;
	gor[3] = 0;    goc[3] = -1;

	char eboard[101][101];
	int er, ec;
	for (ecount = 1; ecount <= ecase; ecount++) {
		if (ecount < caseStart || ecount > caseEnd)
			continue;
	
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d START\n", ecount);

		scanf("%d%d", &er, &ec);
		for (int i = 0; i < er; i++)
				scanf("%s", eboard[i]);
		
		int ans = 0;
		int fail = 0;
		for (int i = 0; i < er; i++)
			for (int j = 0; j < ec; j++)
				if (eboard[i][j] != '.') {
					bool test[4];
					int sum = 0;
					for (int k = 0; k < 4; k++) {
						int ngor = gor[k];
						int ngoc = goc[k];
						int nr = i + ngor;
						int nc = j + ngoc;

						while (true) {
							if (nr < 0 || nr >= er || nc < 0 || nc >= ec) {
								test[k] = false;
								break;
							}
							else if (eboard[nr][nc] != '.') {
								test[k] = true;
								sum++;
								break;
							}
							nr += ngor;
							nc += ngoc;
						}
					}
					int ndir = dirIdx[ eboard[i][j] ];
					if (test[ndir]);
					else if (sum == 0)
						fail++;
					else
						ans++;
				}

		if (fail > 0)
			printf("Case #%d: IMPOSSIBLE\n", ecount);
		else
			printf("Case #%d: %d\n", ecount, ans);
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
