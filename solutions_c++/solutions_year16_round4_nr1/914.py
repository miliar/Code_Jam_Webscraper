#include <bits/stdc++.h>

using namespace std;

char s[13][3][4100];
char ans[4100];
void dfs(int p, int q) {
	if (q == 0) {
		if (strcmp(s[p-1][0], s[p-1][1]) <= 0) {
			strcpy(s[p][q], s[p-1][0]);
			strcpy(s[p][q]+(1<<(p-1)), s[p-1][1]);
		}
		else {
			strcpy(s[p][q], s[p-1][1]);
			strcpy(s[p][q]+(1<<(p-1)), s[p-1][0]);
		}
	}
	if (q == 1) {
		if (strcmp(s[p-1][1], s[p-1][2]) <= 0) {
			strcpy(s[p][q], s[p-1][1]);
			strcpy(s[p][q]+(1<<(p-1)), s[p-1][2]);
		}
		else {
			strcpy(s[p][q], s[p-1][2]);
			strcpy(s[p][q]+(1<<(p-1)), s[p-1][1]);
		}
	}
	if (q == 2) {
		if (strcmp(s[p-1][0], s[p-1][2]) <= 0) {
			strcpy(s[p][q], s[p-1][0]);
			strcpy(s[p][q]+(1<<(p-1)), s[p-1][2]);
		}
		else {
			strcpy(s[p][q], s[p-1][2]);
			strcpy(s[p][q]+(1<<(p-1)), s[p-1][0]);
		}
	}
}
		
void init() {
	strcpy(s[0][0],"P");
	strcpy(s[0][1], "R");
	strcpy(s[0][2], "S");
	for (int i = 1; i <= 12; i++) 
		for (int j = 0; j < 3; j++) dfs(i, j);
}
int sum(int p, int q, char c) {
	int ret = 0;
	for (int i = 0; i < (1<<p); i++) 
		if(s[p][q][i] == c) ret++;
	return ret;
}
int main() {
	init();
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		int n, r, p, ss;
		scanf("%d%d%d%d", &n, &r, &p, &ss);
		ans[0] = 'Z';
		for (int i = 0; i < 3; i++) {
			if (r==sum(n,i,'R')&&p==sum(n,i,'P')&&ss==sum(n,i,'S')) {
				if (strcmp(s[n][i], ans) < 0) {
					strcpy(ans, s[n][i]);
				}
			}
		}
		printf("Case #%d: ", tt);
		if (ans[0] == 'Z') puts("IMPOSSIBLE");
		else puts(ans);
	}
	return 0;
}

