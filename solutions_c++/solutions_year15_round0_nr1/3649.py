#include<cstdio>

int main() {
	int T; scanf("%d", &T);
	for(int _ = 0; _ < T; _++) {
		int N; scanf("%d", &N);
		int res = 0, cnt = 0;
		for(int i = 0; i <= N; i++) {
			char c; scanf(" %c", &c);
			c -= '0';
			if(c) {
				int diff = i - cnt;
				if(diff > 0) {
					res += diff;
					cnt += diff;
				}
				cnt += c;
			}
		}
		printf("Case #%d: %d\n", _+1, res);
	}
	return 0;
}
