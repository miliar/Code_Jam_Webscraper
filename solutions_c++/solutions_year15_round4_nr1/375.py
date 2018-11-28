#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
const int dr[]={0,0,-1,1}, dc[]={-1,1,0,0};
typedef long long LL;
typedef pair<int,int> PT;

int TC, R, C;
char gd[101][101];

int srch(int r, int c, int i) {
	do {
		r += dr[i]; c += dc[i];
	} while (r >= 0 && r < R && c >= 0 && c < C && gd[r][c] == '.');
	if (!(r >= 0 && r < R && c >= 0 && c < C)) return 1; else return 2;
}

int main() {
	scanf("%d", &TC);
	FOR(tc,1,TC+1) {
		scanf("%d%d", &R, &C);
		FOR(r,0,R) scanf("%s", gd[r]);
		int ans = 0;
		FOR(r,0,R) FOR(c,0,C) {
			int i=0;
			if (gd[r][c] == '.') continue;
			if (gd[r][c] == '>') i=1;
			if (gd[r][c] == '<') i=0;
			if (gd[r][c] == '^') i=2;
			if (gd[r][c] == 'v') i=3;
			int x = srch(r, c, i);
			if (x == 1) {
				ans++;
				bool gotit = false;
				FOR(j,0,4) if (srch(r, c, j) == 2) {gotit=true; break;}
				if (!gotit) {ans = -1; goto done;}
			}
		}
		done:;
		printf("Case #%d: ", tc);
		if (ans == -1) puts("IMPOSSIBLE"); else printf("%d\n", ans);
	}
}
