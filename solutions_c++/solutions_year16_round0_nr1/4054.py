#include<cstdio>

int main() {
	int T; scanf("%d", &T);
	for (int _ = 0; _ < T; ++_) {
		int N; scanf("%d", &N);
		if (!N) {
			printf("Case #%d: INSOMNIA\n", _+1);
			continue;
		}
		bool does[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int cnt = 0;
		for (int x = N; x > 0; x/=10) {
			if (!does[x%10]) {
				cnt++;
				does[x%10] = 1;
			}
		}
		int res = N;
		while(cnt < 10) {
			res += N;
			for (int x = res; x > 0; x/=10) {
				if (!does[x%10]) {
					cnt++;
					does[x%10] = 1;
				}
			}
		}
		printf("Case #%d: %d\n", _+1, res);
	}
	return 0;
}
