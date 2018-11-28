#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 15;

int n,r,p,s;
int dp[N][3][3] = {0};
char PRS[] = "PRS";
string S[N][3];

inline void pre () {
	for (int i = 0;i < 3;i ++) {
		for (int j = 0;j < 3;j ++) {
			dp[0][i][j] = 0;
		}
		dp[0][i][i] = 1;
		S[0][i] = PRS[i];
	}
	for (int i = 1;i < N;i ++) {
		for (int j = 0;j < 3;j ++) {
			for (int k = 0;k < 3;k ++) {
				dp[i][j][k] = dp[i-1][j][k]+dp[i-1][(j+1)%3][k];
			}

			string L = S[i-1][j],R = S[i-1][(j+1)%3];
			string t1 = L+R,t2 = R+L;
			if (t1 < t2) {
				S[i][j] = t1;
			} else {
				S[i][j] = t2;
			}
		}
	}
}

inline void solve () {
	scanf ("%d %d %d %d", &n, &r, &p, &s);

	string ans;
	for (int i = 0;i < 3;i ++) {
		if (dp[n][i][0] == p and dp[n][i][1] == r and dp[n][i][2] == s) {
			if (ans.size () == 0) {
				ans = S[n][i];
			} else if (S[n][i] < ans) {
				ans = S[n][i];
			}
		}
	}

	if (ans.size () == 0) {
		printf ("IMPOSSIBLE\n");
	} else {
		cout << ans << endl;
	}
}

int main () {
	pre ();

	int tt;
	scanf ("%d", &tt);

	for (int c = 1;c <= tt;c ++) {
		printf ("Case #%d: ", c);
		solve ();
	}
}