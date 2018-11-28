#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)

int t;
int n, am[123][123], am2[123][123], rep[123], wc[123], mc[123], ans;
char str[123];
int findr(int a) {
	return rep[a] = (a == rep[a] ? a : findr(rep[a]));
}
void join(int a, int b) {
	//printf("j %d %d\n", a, b);
	a = findr(a); b = findr(b);
	if (a==b) return;
	wc[a] += wc[b];
	mc[a] += mc[b];
	rep[b] = a;
}
bool good() {
	fo(i,0,2*n) rep[i] = i;
	fo(i,0,n) wc[i] = 1, mc[i] = 0;
	fo(i,n,2*n) wc[i] = 0, mc[i] = 1;
	fo(i,0,n) fo(j,0,n) if (am2[i][j]) join(i, n + j);
	fo(i,0,n) fo(j,0,n) if (findr(i) == findr(n + j) && !am2[i][j]) return 0;
	int tot = 0;
	fo(i,0,2*n) if (rep[i] == i && wc[i] + mc[i] > 1) {
		tot += min(wc[i], mc[i]);
	}
	return tot == n;
}
int main() {
	scanf("%d", &t);
	fo(_,1,t+1) {
		printf("Case #%d: ", _);
		scanf("%d", &n);
		ans = 999;
		fo(i,0,n) {
			scanf("%s", str);
			fo(j,0,n) am[i][j] = str[j] - '0';
		}

		fo(i,0,1<<(n*n)) {
			fo(j,0,n) fo(k,0,n) {
				int x = n*j + k;
				am2[j][k] = am[j][k];
				if (i & (1<<x)) am2[j][k] = 1;
			}
			if (good()) {
				ans = min(ans, __builtin_popcount(i));
				//fo(ii,0,n) fo(jj,0,n) printf("%d%c", am2[ii][jj], jj==n-1 ? '\n' : ' ');
				//puts("");
			}
		}

		printf("%d\n", ans);
	}

	return 0;
}