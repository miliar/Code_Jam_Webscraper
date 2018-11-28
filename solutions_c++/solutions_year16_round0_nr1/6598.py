#include <cstdio>

int process(int N) {
	int cur = N;
	int flag = 0;
	while (flag != (1 << 10) - 1) {
		int temp = cur;
		while (temp > 0) {
			flag |= (1 << (temp % 10));
			temp /= 10;
		}
		cur += N;
	}
	return cur - N;
}

int main() {
	int T,N;
	scanf("%d",&T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d",&N);
		printf("Case #%d: ", tc);
		if (N == 0)
			printf("INSOMNIA\n");
		else
			printf("%d\n",process(N));
	}
	return 0;
}