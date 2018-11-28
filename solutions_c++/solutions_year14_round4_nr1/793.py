#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

int N, X;
int S[10000];
int V[10000];

int getAns(void) {
	int ret = N;

	sort(S, S + N);
	
	for (int i = 0; i < N; i++)
		V[i] = 0;

	int small_idx = 0;

	for (int i = N - 1; i >= 0; i--) {
		if (V[i])
			continue;

		if (0 <= small_idx && small_idx < i && small_idx < N) {
			if (S[i] + S[small_idx] <= X) {
				ret --;
				V[small_idx] = 1;
				small_idx++;
			}
		}
	}

	return ret;
}

int main(void) {
	int testNum;
	scanf("%d", &testNum);
	for (int testCase = 1; testCase <= testNum; testCase++) {

		scanf("%d %d", &N, &X);

		for (int i = 0; i < N; i++) {
			scanf("%d", &S[i]);
		}

		printf("Case #%d: %d\n", testCase, getAns());

	}

	return 0;
}
