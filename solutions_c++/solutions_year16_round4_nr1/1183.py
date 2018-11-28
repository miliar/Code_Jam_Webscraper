#include <stdio.h>
#include <string.h>

int er, ep, es, en;
int numEle;

char seed[4] = "PRS";

const int S = 5000;
int round;
char ans[5000];
bool ansFound;

int lose[3] = {2, 0, 1};

void dfs(int level, int start, char *ans) {
	if (level == 0) {
		ans[0] = seed[start];
		ans[1] = '\0';
	}
	else {
		char a[S];
		char b[S];
		dfs(level - 1, start, a);
		dfs(level - 1, lose[start], b);
		if (strcmp(a, b) < 0)
			sprintf(ans, "%s%s", a, b);
		else
			sprintf(ans, "%s%s", b, a);
	}
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

	for (ecount = 1; ecount <= ecase; ecount++) {
		if (ecount < caseStart || ecount > caseEnd)
			continue;
	
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d START\n", ecount);

		int ecnt[3];
		scanf("%d%d%d%d", &en, &ecnt[1], &ecnt[0], &ecnt[2]);
		round = 0;
		int t = en;
		while (t > 0) {
			round++;
			t /= 2;
		}

		ans[0] = 'Z';

		for (int i = 0; i < 3; i++) {
			int cnt[3];
			cnt[0] = cnt[1] = cnt[2] = 0;
			cnt[i] = 1;
			for (int j = 0; j < en; j++) {
				int ncnt[3];
				ncnt[0] = cnt[0] + cnt[1];
				ncnt[1] = cnt[1] + cnt[2];
				ncnt[2] = cnt[2] + cnt[0];
				cnt[0] = ncnt[0];
				cnt[1] = ncnt[1];
				cnt[2] = ncnt[2];
				//printf("round %d: %d %d %d\n", j, cnt[0], cnt[1], cnt[2]);
			}
			if (cnt[0] == ecnt[0] && cnt[1] == ecnt[1] && cnt[2] == ecnt[2]) {
				//printf("get in %d\n", i);
				char tmp[S];
				dfs(en, i, tmp);
				if (strcmp(tmp, ans) < 0) {
					strcpy(ans, tmp);
				}
			}
		}

		//printf("hello\n");
		if (ans[0] == 'Z')
			printf("Case #%d: IMPOSSIBLE\n", ecount);
		else
			printf("Case #%d: %s\n", ecount, ans);

		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
