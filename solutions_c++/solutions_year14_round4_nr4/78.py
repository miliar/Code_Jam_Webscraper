#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

const double pi = acos(-1.);
const double eps = 1e-6;

int g[110][30], tag[110], n, m;
char s[110][110];
int calc()
{
	int sum = 0;
	for (int i = 0; i < m; i++) {
		int now = 0;
		int total = 0;
		memset(g, -1, sizeof g);
		bool flag = 0;
		for (int j = 0; j < n; j++) {
			if (tag[j] != i) continue;
			flag = 1;
			now = 0;
			int len = strlen(s[j]);
			for (int x = 0; x < len; x++) {
				if (g[now][s[j][x] - 'A'] == -1)
					g[now][s[j][x] - 'A'] = ++total;
				now = g[now][s[j][x] - 'A'];
			}
		}
		if (!flag) return 0;
		sum += total + 1;
	}
	return sum;
}
int best = 0, way;
void dfs(int a)
{
	if (a == n) {
		int ans = calc();
		if (ans > best) {
			best = ans;
			way = 1;
		} else if (ans == best) way++;
		return;
	}
	for (int i = 0; i < m; i++) {
		tag[a] = i;
		dfs(a + 1);
	}
}
int main()
{
	int ca = 0;
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int T;
	for (scanf("%d", &T); T; T--) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", s[i]);
		}
		best = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", ++ca, best, way);
	}
}
