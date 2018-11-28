#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int N, R, P, S;
string ans[20][3];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	ans[0][0] = "P";
	ans[0][1] = "R";
	ans[0][2] = "S";
	for (int n = 1; n <= 12; n ++) {
		ans[n][0] = min(ans[n-1][0] + ans[n-1][1], ans[n-1][1] + ans[n-1][0]);
		ans[n][1] = min(ans[n-1][1] + ans[n-1][2], ans[n-1][2] + ans[n-1][1]);
		ans[n][2] = min(ans[n-1][2] + ans[n-1][0], ans[n-1][0] + ans[n-1][2]);
	}
	int test, nCase = 0;
	scanf("%d", &test);
	while (test --) {
		scanf("%d%d%d%d", &N, &R, &P, &S);
		string ret = "Z";
		for (int i = 0; i < 3; i ++) {
			int r = 0, p = 0, s = 0;
			for (int j = 0; j < ans[N][i].size(); j ++) {
				if (ans[N][i][j] == 'R') r ++;
				if (ans[N][i][j] == 'P') p ++;
				if (ans[N][i][j] == 'S') s ++;
			}
			if (r == R && p == P && s == S) {
				ret = min(ret, ans[N][i]);
			}
		}
		if (ret == "Z") ret = "IMPOSSIBLE";
		printf("Case #%d: ", ++ nCase);
		cout << ret << endl;
	}
	return 0;
}
