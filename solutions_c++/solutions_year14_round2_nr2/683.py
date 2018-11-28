#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstring>
using namespace std;

long long dp[31][2][2][2];
int *bitA = new int[31];
int *bitB = new int[31];
int *bitK = new int[31];
//int *bitA = malloc(31*sizeof(int));
//int *bitB = malloc(31*sizeof(int));
//int *bitK = malloc(31*sizeof(int));
int A, B, K;

int *gao(int * tmp, int x) {
	for (int i = 0; i < 31; i++) {
		if ((x & (1 << i)) > 0) {
			tmp[i] = 1;
		} else {
			tmp[i] = 0;
		}
	}
	return tmp;
}

long dfs(int pos, int TA, int TB, int TK) {
	if (pos == -1)
		return 1;
	if (dp[pos][TA][TB][TK] != -1) {
		return dp[pos][TA][TB][TK];
	}
	long res = 0;
	for (int x = 0; x < 2; x++) {
		for (int y = 0; y < 2; y++) {
			int z = x & y;
			if ((TA == 0 || (x <= bitA[pos]))
					&& (TB == 0 || (y <= bitB[pos]))
					&& (TK == 0 || (z <= bitK[pos]))) {
				int TAA = TA == 1 && (x >= bitA[pos]) ? 1 : 0;
				int TBB = TB == 1 && (y >= bitB[pos]) ? 1 : 0;
				int TKK = TK == 1 && (z >= bitK[pos]) ? 1 : 0;
				res += dfs(pos - 1, TAA, TBB, TKK);
			}
		}
	}
	dp[pos][TA][TB][TK] = res;
	return res;
}

int main() {
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t) {
		cin>>A>>B>>K;
		A-=1;
		B-=1;
		K-=1;
		//*bitA = malloc(sizeof(int)*31);
		//*bitB = malloc(sizeof(int)*31);
		//*bitC = malloc(sizeof(int)*31);
		bitA = gao(bitA, A);
		bitB = gao(bitB, B);
		bitK = gao(bitK, K);
		int answer = 0;
		for (int i = 0; i < 31; i++) {
			for (int j = 0; j < 2; j++) {
				for (int k = 0; k < 2; k++) {
					for (int l = 0; l < 2; l++) {
						dp[i][j][k][l] = -1;
					}
				}
			}
		}
		cout<<"Case #"<<t<<": "<<(dfs(30, 1, 1, 1))<<endl;;
	}
}