#include <cstdio>
#include <algorithm>
using namespace std;

int T, N, M, A[1<<7][1<<7], B[1<<7][1<<7], R[1<<7], C[1<<7];

int main(void){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++) {
		scanf("%d %d", &N, &M);
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= M; j ++) {
				scanf("%d", &A[i][j]);
				B[i][j] = 100;
				R[i] = C[j] = 0;
			}
		for (int r = 1; r <= N; r ++) {
			for (int c = 1; c <= M; c ++) {
				R[r] = max(R[r], A[r][c]);
			}
		}
		for (int c = 1; c <= M; c ++) {
			for (int r = 1; r <= N; r ++) {
				C[c] = max(C[c], A[r][c]);
			}
		}
		for (int r = 1; r <= N; r ++) {
			for (int c = 1; c <= M; c ++)
				B[r][c] = min(B[r][c], min(R[r], C[c]));
		}
		bool S = true;
		for (int i = 1; i <= N; i ++) {
			for (int j = 1; j <= M; j ++) {
				if (A[i][j] != B[i][j]) S = false;
			}
		}
		printf("Case #%d: ", t);
		if (S) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}