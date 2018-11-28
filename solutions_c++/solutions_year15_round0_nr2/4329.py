#include <cstdio>

int T, D, P[1010];
int ans = 1000000007;

int main() {
	scanf("%d", &T);
	for(int tc=1; tc<=T; tc++) {
		scanf("%d", &D);
		for(int i=0; i<D; i++) scanf("%d", &P[i]);
		ans = 1000000007;
		for(int lim=1; lim<1000; lim++) {
			int sum = 0;
			for(int i=0; i<D; i++) sum += (P[i]+lim-1)/lim - 1;
			if( sum+lim < ans ) ans = sum+lim;
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}