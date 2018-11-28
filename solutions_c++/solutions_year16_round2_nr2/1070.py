#include <bits/stdc++.h>
using namespace std;

char C[19], J[19];
int mini, Jmini;
char Ca[19], Ja[19];

void dfs(char* C, char* J) {
	int q = 0;

	for (char* p = C; *p; ++p) {
		if (*p == '?') {
			q++;
			for (char c = '0'; c <= '9'; ++c) {
				*p = c;
				dfs(C, J);
				*p = '?';
			}
		}
	}

	for (char* p = J; *p; ++p) {
		if (*p == '?') {
			q++;
			for (char c = '0'; c <= '9'; ++c) {
				*p = c;
				dfs(C, J);
				*p = '?';
			}
		}
	}

	if (!q) {
		int c = atoi(C), j = atoi(J);
		if (abs(c - j) < mini
		 || abs(c - j) == mini && j < Jmini) {
			mini = abs(c - j);
			Jmini = j;
			strcpy(Ca, C);
			strcpy(Ja, J);
		}
	}
}

void solve() {
	scanf("%s%s", C, J);

	mini = Jmini = 1 << 30;

	dfs(C, J);

	printf("%s %s\n", Ca, Ja);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
