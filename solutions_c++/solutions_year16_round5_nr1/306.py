#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <complex>

typedef long long lld;
typedef unsigned long long llu;

#define INF 1000000001
#define INFL 1000000000000000001ll
#define MOD 1000000007

#define MAXN 20005

using namespace std;

int tests, n;
int dp[MAXN][MAXN], dp2[MAXN];
string s;

int main() {
	cin >> tests;
	for (int test = 1 ; test <= tests ; test ++) {
		cin >> s;
		n = s.size();
		for (int l = 1 ; l < n ; l += 2) {
			for (int i = 0 ; i < n - l ; i ++) {
				int j = i + l;
				//dp[i][j] = max(max(dp[i + 1][j], dp[i][j - 1]), dp[i + 1][j - 1] + 1 + (s[i] == s[j]));
				dp[i][j] = dp[i + 1][j - 1] + 1 + (s[i] == s[j]);
				for (int k = 1 ; k < l ; k += 2) dp[i][j] = max(dp[i][j], dp[i][i + k] + dp[i + k + 1][j]);
				//printf("XXXXX %d %d : %d\n", i, j, dp[i][j]);
			}
		}
		for (int i = 0 ; i < n ; i ++) {
			dp2[i] = 0;
			if (i % 2 == 1) dp2[i] = max(dp2[i], dp[0][i]);
			if (i != 0) dp2[i] = max(dp2[i], dp2[i - 1]);
			for (int j = i % 2 ; j < i ; j ++) dp2[i] = max(dp2[i], dp2[j] + dp[j + 1][i]);
			//printf("LLLLL %d : %d\n", i, dp2[i]);
		}
		cout << "Case #" << test << ": ";
		cout << dp2[n - 1] * 5 << endl;
	}
	return 0;
}