#include <iostream>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)

int dp[1024][1024][101];
int H[101], G[101];

void do_case(int case_no) {
	int P, Q, N;
	cin >> P >> Q >> N;
	FOR(i,0,N) cin >> H[i] >> G[i];
	int be = 0;
	memset(dp,-1,sizeof(dp));
	dp[0][0][0] = 0;
	FOR(i,0,1001) {
		for(int j=0;j<=i+1;j++) {
			if (dp[i][j][N] != -1) be = max(be,dp[i][j][N]);
			FOR(k,0,N) if (dp[i][j][k] != -1) {
				int nt = (H[k]-1) / Q;
				int hp = H[k] - (nt * Q);
				int ni = i + nt;
				dp[ni+1][j][k+1] = max(dp[ni+1][j][k+1],dp[i][j][k]);
				int mo = ni + 1 - j;
				int mt = ((hp-1) / P) + 1;
				if (mt <= mo) {
					int nj = j + mt;
					dp[ni][nj][k+1] = max(dp[ni][nj][k+1],dp[i][j][k] + G[k]);
				}
			}
		}
	}
	cout << "Case #" << case_no << ": " << be << endl;
}

int main() {
	int T, te = 1;
	cin >> T;
	while(T) {
		do_case(te);
		T--;
		te++;
	}
	return 0;
}
