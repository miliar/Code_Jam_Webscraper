#include <bits/stdc++.h>
using namespace std;


int main() {
	int T;
	scanf("%d", &T);

	for (int testcase = 1; testcase <= T; testcase++) {
		int answer = 0, d;

		scanf("%d", &d);
		int p[d + 5];
		int bound = 0;
		for (int i = 0; i < d; i++) {
			scanf("%d", &p[i]);
			bound = max(bound, p[i]);
		}

		answer = bound;

		for (int i = 1; i <= bound; i++) {
			int temp = 0;
			for (int j = 0; j < d; j++) {
				temp += p[j] / i;
				if (p[j] % i == 0) temp--;
			}
			answer = min(answer, temp + i);
		}

		printf("Case #%d: %d\n", testcase, answer);
	}
	return 0;
}
