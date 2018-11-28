#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 101;
const int INF = 10000;

long long int t, a, n, d[MAXN], res[MAXN][MAXN], wyn;

long long int f(int foo, int bar) {
	if(foo < 2) return INF;
	long long int ret = 0;
	while(foo <= bar) {
		foo += foo-1;
		ret++;
	}
	return ret;
}

long long int ops(int foo, int bar) {
	long long int ret = bar;
	while(foo--) {
		ret += ret-1;
	}
	return ret;
}

int main() {
	scanf("%d",&t);
	for(int ct=1;ct<=t;ct++) {
		scanf("%d%d",&a,&n);
		wyn = n;
		for(int i=1;i<=n;i++) scanf("%d",&d[i]);
		sort(d+1, d+n+1);
		for(int i=0;i<=n;i++) for(int j=0;j<=n;j++) res[i][j] = 0;
		if(a>d[1]) res[1][0] = a+d[1];
		for(int i=1;i<=n;i++) if(ops(i, a) > d[1]) res[1][i] = ops(i, a)+d[1];
		for(int i=2;i<=n;i++) {
			for(int j=0;j<=n;j++) {
				for(int k=j;k<=n;k++) {
					if(ops(k-j, res[i-1][j]) > d[i]) {
						res[i][k] = max(res[i][k], ops(k-j, res[i-1][j])+d[i]);
						//printf("%d %d %d %d %d %d\n", i, k, d[i], res[i-1][j]+ops(k-j, res[i-1][j]), res[i-1][j]+ops(k-j, res[i-1][j])+d[i], res[i][k]);
					}
				}
			}
		}
		for(int i=1;i<=n;i++) {
			for(int j=0;j<=n;j++) if(res[i][j] > 0) wyn = min(wyn, j+(n-i));
		}
		printf("Case #%d: %d\n", ct, wyn);
	}
	return 0;
}
