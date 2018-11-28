//By Lin
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <bitset>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>
#include <queue>

#define X first
#define Y second
#define mp make_pair
#define sqr(x) ((x) * (x))
#define Rep(i, n) for(int i = 0; i<(n); i++)
#define foreach(it, n) for(__typeof(n.begin()) it = n.begin(); it != n.end(); it++)

using namespace std;
typedef long long LL;
typedef pair<int, int> pii;

#define esp 1e-8
#define N 100010
#define MOD 1000000007

int n, R, P, S;
char ss[5] = "PRS";
string dp[50][3];

bool check(string s) {
	int a = 0, b = 0, c = 0;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == 'P') a++;
		if (s[i] == 'R') b++;
		if (s[i] == 'S') c++;
	}
	return a == P && b == R && c == S;
}

int main() {
	int cas, tt = 0;
	cin >> cas;
	dp[1][0] = string("PR");
	dp[1][1] = string("RS");
	dp[1][2] = string("PS");
	for (int i = 2; i <= 13; i++) {
		Rep(j, 3) {
			int g = j, h = (j + 1) % 3;
			string L = dp[i - 1][g];
			string R = dp[i - 1][h];
			if (L < R) dp[i][j] = L + R;
			else dp[i][j] = R + L;
		}
	}
	while (cas --) {
		scanf("%d%d%d%d", &n, &R, &P, &S);
		vector<string> ans;
		Rep(i, 3) {
			string s = dp[n][i];
			if (check(s)) {
				ans.push_back(s);
			}
		}
		sort(ans.begin(), ans.end());
		printf("Case #%d: ", ++tt);
		if (ans.size() == 0) puts("IMPOSSIBLE");
		else {
			printf("%s\n", ans[0].c_str());
		}
	}
	return 0;
}
