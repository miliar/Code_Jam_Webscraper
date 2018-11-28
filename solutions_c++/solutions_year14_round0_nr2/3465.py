#include <stdio.h>
#include <string.h>
#include <math.h>
#define MIN(a,b) a<b?a:b
double c, f, x;
void input();
int main() {
	int T, tc;
	for(scanf("%d", &T), tc = 1; tc <= T; tc++) {
		input();
		double r = 2, t = 0, ans = x/r;
		while(t < ans) {
			t += c / r;
			r += f;
			ans = MIN(ans, t+x/r);
		}
		printf("Case #%d: %.7lf\n", tc, ans);
	}
	return 0;
}
void input() {
	int cd[2], fd[2], xd[2];
	char sc[10], sf[10], sx[10];
	scanf("%d.%s", &cd[0], sc);
	scanf("%d.%s", &fd[0], sf);
	scanf("%d.%s", &xd[0], sx);
	sscanf(sc, "%d", &cd[1]);
	sscanf(sf, "%d", &fd[1]);
	sscanf(sx, "%d", &xd[1]);
	int clen = strlen(sc), flen = strlen(sf), xlen = strlen(sx);
	c = (double)cd[0] + cd[1] / pow(10, clen);
	f = (double)fd[0] + fd[1] / pow(10, flen);
	x = (double)xd[0] + xd[1] / pow(10, xlen);
}
