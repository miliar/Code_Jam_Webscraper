/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

#define P 0
#define N 1

const int MN = 19;

struct state {
	long long c, j, ans;
};

state dp[MN][MN][2];

bool isBad(state x, int k) {
	if (k == P && x.ans < 0) return true;
	if (k == N && x.ans > 0) return true;
	return false;
}

string getString(long long a, int n) {
	string temp;
	stringstream ss;
	ss << a;
	temp = ss.str();
	int sz = temp.size();
	string ret(n - sz, '0');
	return ret + temp;
}

void upDate(state &a, state b, int k) {
	if (isBad(a, k)) a = b;
	else {
		if (k == P) {
			if (a.ans > b.ans) a = b;
			else if (a.ans < b.ans) return ;
			else if (a.c > b.c) a = b;
			else if (a.c < b.c) return ;
			else if (a.j > b.j) a = b;
		} else {
			if (a.ans < b.ans) a = b;
			else if (a.ans > b.ans) return ;
			else if (a.c > b.c) a = b;
			else if (a.c < b.c) return ;
			else if (a.j > b.j) a = b;
		}
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;
	scanf("%d", &T);
	while (T--) {
		char a[MN], b[MN];
		scanf("%s %s", a, b);
		int n, i, j, k, l;
		n = strlen(a);

		long long diff = 0, fact = 1, tempFact, f[MN];

		for (i = 0; i < n - 1; ++i) fact *= 10;
		tempFact = fact;

		for (i = 0; i < n; ++i) f[i] = fact, fact /= 10;

		for (i = 0; i < n; ++i) {
			if (a[i] != '?') diff += f[i] * (a[i] - '0');
		}

		for (i = 0; i < n; ++i) {
			if (b[i] != '?') diff -= f[i] * (b[i] - '0');
		}

		for (i = 0; i <= n; ++i) {
			for (j = 0; j <= n; ++j) {
				for (k = 0; k < 2; ++k) {
					if (k == P) dp[i][j][k].ans = -1;
					else dp[i][j][k].ans = 1;
				}
			}
		}

		if (diff <= 0) dp[0][0][N] = {0, 0, diff};
		if (diff >= 0) dp[0][0][P] = {0, 0, diff};

		for (i = 0; i <= n; ++i) {
			for (j = 0; j <= n; ++j) {
				for (k = 0; k < 2; ++k) {
					if (isBad(dp[i][j][k], k)) continue;
					state curState = dp[i][j][k];

					if (i == n) ;
					else if (a[i] != '?') dp[i + 1][j][k] = {curState.c * 10 + (a[i] - '0'), curState.j, curState.ans};
					else {
						state nxt = curState;
						for (l = 0; l < 10; ++l) {
							nxt.ans = curState.ans + l * f[i];
							nxt.c = curState.c * 10 + l;
							if (nxt.ans >= 0) upDate(dp[i + 1][j][P], nxt, P);
							if (nxt.ans <= 0) upDate(dp[i + 1][j][N], nxt, N);
						}
					}

					if (j == n) ;
					else if (b[j] != '?') dp[i][j + 1][k] = {curState.c, curState.j * 10 + (b[j] - '0'), curState.ans};
					else {
						state nxt = curState;
						for (l = 0; l < 10; ++l) {
							nxt.ans = curState.ans - l * f[j];
							nxt.j = curState.j * 10 + l;
							if (nxt.ans >= 0) upDate(dp[i][j + 1][P], nxt, P);
							if (nxt.ans <= 0) upDate(dp[i][j + 1][N], nxt, N);
						}
					}
				}
			}
		}

		long long ba = -5, bb = -5;

		if (isBad(dp[n][n][P], P)) ba = dp[n][n][N].c, bb = dp[n][n][N].j;
		else if (isBad(dp[n][n][N], N)) ba = dp[n][n][P].c, bb = dp[n][n][P].j;
		else {
			state po = dp[n][n][P], no = dp[n][n][N];
			if (po.ans < -no.ans) ba = po.c, bb = po.j;
			else if (po.ans > -no.ans) ba = no.c, bb = no.j;
			else if (po.c > no.c) ba = no.c, bb = no.j;
			else if (po.c < no.c) ba = po.c, bb = po.j;
			else if (po.j > no.j) ba = no.c, bb = no.j;
			else ba = po.c, bb = po.j;
		}

//		cout << isBad(dp[n][n][N], N) << ' ' << isBad(dp[n][n][P], P) << endl;

		printf("Case #%d: %s %s\n", K, getString(ba, n).c_str(), getString(bb, n).c_str());
		++K;
	}
	return 0;
}
