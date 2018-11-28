#include <bits/stdc++.h>
using namespace std;

string S;
const int MAXN = 100;

int dp[2][MAXN + 10];
int A[MAXN + 10];

int main() {
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int T; fin >> T;
	for(int cs = 1; cs <= T; cs++) {
		fin >> S; int L = S.size();
		for(int i = 0; i < L; i++) A[i] = S[i] == '+';
		dp[0][L] = 1;
		dp[1][L] = 0;
		for(int i = L-1; i >= 0; i--) {
			for(int c = 0; c <= 1; c++) {
				// AB
				// AB -> BB -> AA
				// AA
				if(A[i] == c) dp[c][i] = min(dp[c][i+1], 1 + dp[1-c][i+1]);
				else dp[c][i] = 2 + dp[1-c][i+1];
			}
		}
		int rs = dp[A[0]][0];
		fout << "Case #" << cs << ": " << rs << "\n";
	}
	fout.flush();
}
