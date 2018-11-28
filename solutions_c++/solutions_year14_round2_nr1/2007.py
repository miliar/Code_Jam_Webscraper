#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

char ss[110][110];

int memo[110][110];

int cmptwo(int a, int b) {
	if (a == b) return 0;
	if (memo[a][b] != -1) return memo[a][b];
	int la, lb, i, j, r;
	la = strlen(ss[a]);
	lb = strlen(ss[b]);
	i = 0; j = 0;
	r = 0;
	while (i < la || j < lb) {
		if (i == la) {
			r += (lb-j);
			break;
		}
		if (j == lb) {
			r += (la-i);
			break;
		}
		if (ss[a][i] == ss[b][j]) {
			i++; j++;
		} else if (ss[a][i] == ss[a][i-1]) {
			i++;
			r++;
		} else if (ss[b][j] == ss[b][j-1]) {
			j++;
			r++;
		}
	}
	memo[a][b] = r;
	memo[b][a] = r;
	return r;
}

int main() {
	int T, N, i, j, l, ub, c, r;
	string ts[110];
	bool inv;
	c = 1;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		for (i=0; i<N; i++) scanf("%s", ss[i]);
		ub = 0;
		for (i=0; i<N; i++) {
			l = strlen(ss[i]);
			ts[i] = ss[i][0];
			for (j=1; j<l; j++) {
				if (ss[i][j] != ss[i][j-1]) ts[i].push_back(ss[i][j]);
				else ub++;
			}
		}
		inv = false;
		for (i=1; i<N && !inv; i++) {
			if (ts[i].compare(ts[i-1]) != 0) inv = true;
		}
		if (inv) {
			printf("Case #%d: Fegla Won\n", c++);
			continue;
		}
		memset(memo, -1, sizeof memo);
		for (i=0; i<N; i++) {
			r = 0;
			for (j=0; j<N; j++) {
				r += cmptwo(i, j);
			}
			ub = min(ub, r);
		}
		printf("Case #%d: %d\n", c++, ub);
	}
	return 0;
}
