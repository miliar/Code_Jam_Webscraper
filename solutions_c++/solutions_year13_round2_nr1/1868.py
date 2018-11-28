#include <cstdio>
#include <algorithm>
#include <cmath>

#define INF 1000000

int almostLog(int a, int exp) {
	int result = 0;
	while(exp >= a) {
		a += a-1;
		++result;
	}
	return result;
}

int almostExp(int a, int exp) {
	while(exp >= a) {
		a += a-1;
	}
	return a;
}

int main() {
	int T, N;
	int A, a[101], mobeSize[101], best[101], temp;

	scanf("%d", &T);
	for(int testCase = 1; testCase <= T; ++testCase) {
		scanf("%d %d", &A, &N);
		for(int i = 1; i <= N; ++i)
			scanf("%d", &a[i]);

		if(A == 1) {
			printf("Case #%d: %d\n", testCase, N);
			continue;
		}

		std::sort(a+1, a+N+1);
		
		mobeSize[0] = A;
		best[0] = 0;
		for(int i = 1; i <= N; ++i) {
			best[i] = INF;
			for(int j = 0; j < i; ++j) {
				temp = best[j] + i - j - 1 + almostLog(mobeSize[j], a[i]);
				//printf( "%d %d: temp %d a[i] %d mobeSize[j] %d log %d\n", i, j, temp, a[i], mobeSize[j], almostLog(mobeSize[j], a[i]));
				if(temp < best[i]) {
					best[i] = temp;
					mobeSize[i] = almostExp(mobeSize[j], a[i]) + a[i];
				}
			}
		}

		int result = best[N];
		for(int i = 0; i <= N; ++i) {
			result = std::min(result, best[i] + N-i);
		}
		printf("Case #%d: %d\n", testCase, result);
	}

	return 0;
}
