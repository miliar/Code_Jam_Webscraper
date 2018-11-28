#include<bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define UPD(a,b) { a = a + (b); }

double A[222], B[222], dp[222][222];
int n, k;
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		cin >> n >> k;
		For(i,1,n) scanf("%lf", &A[i]);
		sort(A + 1, A + n + 1);
		double ans2 = 0;
		For(x,0,k) {
			int p = 0;
			For(j,1,x) B[++p] = A[j];
			For(j,n - (k - x) + 1, n) B[++p] = A[j];
			memset(dp, 0, sizeof dp);
			dp[0][0] = 1.0;
			For(i,0,k - 1) For(j,0,i) {
				UPD(dp[i + 1][j + 1], dp[i][j] * B[i + 1]);
				UPD(dp[i + 1][j], dp[i][j] * (1 - B[i + 1]));
			}
			if (dp[k][k / 2] > ans2) {
				ans2 = dp[k][k / 2];
			}
		}
		printf("%.12f\n", ans2);
	}
	return 0;
}
