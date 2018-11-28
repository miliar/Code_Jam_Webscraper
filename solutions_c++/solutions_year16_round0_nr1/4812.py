#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T, N;
int h[10];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		printf("Case #%d: ", t);
		if (N == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		memset(h, 0, sizeof(h));
		int ans, cnt = 0;
		for (ans = N; cnt < 10; ans += N) {
			for (int tmp = ans; tmp; tmp /= 10) {
				if (h[tmp % 10] == 0) {
					h[tmp % 10] = 1;
					cnt++;
				}
			}
		}
		printf("%d\n", ans - N);
	}
	return 0;
}