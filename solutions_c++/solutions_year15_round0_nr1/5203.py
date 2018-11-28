#include <cstdio>

int T, N;
char in[1010];

int main() {
	scanf("%d", &T);
	for(int tc=1; tc<=T; tc++) {
		scanf("%d%s", &N, in);
		int need = 0, cnt = 0;
		for(int i=0; i<=N; i++) {
			if( cnt < i ) {
				need += i - cnt;
				cnt = i;
			}
			cnt += in[i] - '0';
		}
		printf("Case #%d: %d\n", tc, need);
	}
	return 0;
}