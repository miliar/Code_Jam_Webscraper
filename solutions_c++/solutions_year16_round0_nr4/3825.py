#include<stdio.h>

void process() {
	int K, C, S;
	scanf("%d%d%d", &K, &C, &S);

	if (C == 1) {
		if (S < K)
			printf("IMPOSSIBLE\n");
		else {
			for (int i = 1; i <= K; i++) {
				printf("%d ", i);
			}
			printf("\n");
		}
		return;
	}
	//C>=2
	if (S < (K + 1) / 2) {
		printf("IMPOSSIBLE\n");
		return;
	}

	long long pt = 2;
	long long t = 0;
	for (int i = 0; i < (K + 1) / 2; i++) {
		
		printf("%lld ", t + (pt > K ? K : pt));
		pt += 2;
		t += (K * 2);
	}

	
	printf("\n");
}
int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int testcase; scanf("%d", &testcase);
	for (int i = 1; i <= testcase; i++) {
		printf("Case #%d: ", i);
		process();
	}

	
	return 0;
}