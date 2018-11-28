#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int MAXN = 105;
int T, N;
string S;
int dp[MAXN][2];

int go()
{
	memset(dp, 0, sizeof(dp));
	for (int i = 1; i <= N; i++)
	{
		int idx = i - 1;
		while (idx >= 0 && S[idx] == S[i - 1])
			idx--;
		idx++;

		int type = (S[i - 1] == '+') ? 1 : 0;
		dp[i][type] = dp[i - 1][type];
		dp[i][!type] = min(dp[idx][type] + 1, dp[idx][!type] + 3);
	}
	return dp[N][1];
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	ios::sync_with_stdio(0);

	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> S;
		N = S.size();
		cout << "Case #" << t << ": " << go() << "\n";
	}

	return 0;
}