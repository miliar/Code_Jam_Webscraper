#include<stdio.h>
#include<string.h>

char buf[1024];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int K;
		int ret = 0;
		scanf(" %s%d", buf, &K);
		int n = strlen(buf);
		for (int i = 0; i < n - K + 1; i++) {
			if (buf[i] == '-') {
				for (int j = 0; j < K; j++) {
					buf[i + j] = buf[i + j] == '+' ? '-' : '+';
				}
				ret++;
			}
		}
		for (int i = n - K + 1; i < n; i++) {
			if (buf[i] == '-') {
				ret = -1;
				break;
			}
		}
		if (ret < 0) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		} else {
			printf("Case #%d: %d\n", t, ret);
		}
	}
	return 0;
}