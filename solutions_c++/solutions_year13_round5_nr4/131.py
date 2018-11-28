#include <stdio.h>
#include <string.h>

double ans[22][1100000];
bool find[22][1100000];

double dfs(int level, int state) {
	if (find[level][state] == false) {
		find[level][state] = true;
		if (state == 0) {
			ans[level][state] = 0.0;
		}
		else {
			double re = 0.0;
			for (int i = 0; i < level; i++) {
				int j;
				for (j = 0; j < level; j++) {
					int p = (i + j) % level;
					if (state & (1 << p)) {
						int tstate = state ^ (1 << p);
						re += level - j + dfs(level, tstate);
						break;
					}
				}
			}
			ans[level][state] = re / level;
		}
	}
	return ans[level][state];
}

int main() {
	int ecase, ecount;

	//for (int i = 0; i < 8; i++)
	//	printf("%.10lf\n", dfs(3, i));

	char input[220];
	int len;

	scanf("%d", &ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		scanf("%s", input);
		len = strlen(input);
		int s = 0;
		for (int i = len-1; i >= 0; i--) {
			s = s * 2 + (input[i] == '.' ? 1 : 0);
		}
		double ans = dfs(len, s);
		printf("Case #%d: %.15lf\n", ecount, ans);
		fprintf(stderr, "Case #%d: %.15lf\n", ecount, ans);
	}

	return 0;
}
