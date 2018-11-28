#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

char s[105][105];
int dir[4][2] = { 1, 0, 0, 1, -1, 0, 0, -1 };
int main() {
	int t, cas = 0;
	int n, m;
	int i, j, k;
	bool flag;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; ++i) {
			scanf("%s", s[i]);
		}
		flag = true;
		int ans = 0;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				if (s[i][j] == '.')
					continue;
				int cost = 2;
				for (k = 1; i + k < n; ++k) {
					if (s[i + k][j] != '.') {
						if (s[i][j] == 'v')
							cost = min(cost, 0);
						else
							cost = min(cost, 1);
						break;
					}
				}
				for (k = 1; j + k < m; ++k) {
					if (s[i][j + k] != '.') {
						if (s[i][j] == '>')
							cost = min(cost, 0);
						else
							cost = min(cost, 1);
						break;
					}
				}
				for (k = 1; i - k >= 0; ++k) {
					if (s[i - k][j] != '.') {
						if (s[i][j] == '^')
							cost = min(cost, 0);
						else
							cost = min(cost, 1);
						break;
					}
				}
				for (k = 1; j - k >= 0; ++k) {
					if (s[i][j - k] != '.') {
						if (s[i][j] == '<')
							cost = min(cost, 0);
						else
							cost = min(cost, 1);
						break;
					}
				}
				if (cost == 2)
					flag = false;
				ans += cost;
			}
		}
		if (flag == false)
			printf("Case #%d: IMPOSSIBLE\n", cas);
		else
			printf("Case #%d: %d\n", cas, ans);
	}
}
