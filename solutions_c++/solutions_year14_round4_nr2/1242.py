#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

const int INF = (1<<29);

int solve0(int N, int *A) {
	int ans = INF;
	static int B[1010];
	memcpy(B, A, sizeof(*A)*N);
	sort(B, B+N);
	do {
		int prev = -1;
		int z = 0;
		for (z = 0; z < N; z++) {
			if (prev > B[z])
				break;
			prev = B[z];
		}
		for (; z < N; z++) {
			if (prev < B[z])
				break;
			prev = B[z];
		}
		if (z != N)
			continue;
		static int C[1010];
		memcpy(C, A, sizeof(*A)*N);
		int r = 0;
		for (int j = 0; j < N; j++) {
			for (int k = j; k < N; k++) {
				if (C[k] == B[j]) {
					r += k-j;
					for (k--; k >= j; k--) {
						C[k+1] = C[k];
					}
					break;
				}
			}
		}
		ans = min(ans, r);
	} while (next_permutation(B, B+N));
	return ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int N;
		scanf("%d", &N);
		static int A[1010];
		for (int j = 0; j < N; j++) {
			scanf("%d", &A[j]);
		}
		int ans = solve0(N, A);
		printf("Case #%d: %d\n", i+1, ans);
	}
}
