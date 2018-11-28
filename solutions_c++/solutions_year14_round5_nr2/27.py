#pragma comment(linker, "/STACK:100000000")
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;
#define int64 long long
#define ldb long double
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define taskname "task_b"
const ldb pi = acos(-1.0);
const int inf = (int) 1e9;
const int N = 111;
const int S = N * 10;
const int H = 222;
int ans[N][H][S], n, p, q, t, hp[N], cost[N];

void relax(int& a, int b) {
	a = max(a, b);
}

int main() {
	assert(freopen(taskname".in", "r", stdin));
	assert(freopen(taskname".out", "w", stdout));
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		scanf("%d%d%d", &p, &q, &n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &hp[i], &cost[i]);
		hp[n] = 0;
		for (int i = 0; i <= n; ++i)
			for (int j = 0; j < H; ++j)
				for (int k = 0; k < S; ++k)
					ans[i][j][k] = -inf;
		ans[0][hp[0]][1] = 0;
		for (int i = 0; i < n; ++i)
			for (int j = hp[i]; j > 0; --j)
				for (int k = 0; k < S; ++k) {
					if (ans[i][j][k] < 0) continue;
					if ((k > 0) && (j <= p)) relax(ans[i + 1][hp[i + 1]][k - 1], ans[i][j][k] + cost[i]);
					if ((k > 0) && (j > p)) relax(ans[i][j - p][k - 1], ans[i][j][k]);
					if (j <= q) relax(ans[i + 1][hp[i + 1]][k + 1], ans[i][j][k]);
					if (j > q) relax(ans[i][j - q][k + 1], ans[i][j][k]);
				}
		printf("Case #%d: %d\n", it + 1, *max_element(ans[n][0], ans[n][0] + S));
	}
	return 0;
}

