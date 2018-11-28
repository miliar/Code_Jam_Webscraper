#include<cstdio>
#include<string.h>
#define INF 99999999
int T, K, len, ans;
char c, S[1002];
int main() {
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		ans = len = 0;
		scanf("%s %d", S, &K);
		len = strlen(S);
		for(int i = 0; i < len-K+1; i++) {
			if(S[i] != '+') {
				for(int j = 0; j < K; j++) {
					S[i+j] = S[i+j] == '+' ? '-' : '+';
				}
				ans++;
			}
		}
		for(int i = len-K; i < len; i++) {
			if(S[i] != '+') ans = INF;
		}
		if(ans < INF) printf("Case #%d: %d\n", t, ans);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}
