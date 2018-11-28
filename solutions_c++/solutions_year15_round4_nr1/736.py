#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <iostream>
#include <sstream>
#include <cctype>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> ii;

int r, c;
char grid[111][111];
int cnt[111][111];
int change[111][111];

void solve() {
	scanf("%d%d", &r, &c);
	REP(i, r) REP(j, c) {
		cnt[i][j] = 0;
		change[i][j] = 0;
		scanf(" %c", &grid[i][j]);
	}
	REP(i, r) {
		int j = 0;
		while (j<c && grid[i][j]=='.') j++;
		if (j<c) {
			cnt[i][j]++;
			if (grid[i][j]=='<') change[i][j] = 1;
		}
		j = c-1;
		while (j>=0 && grid[i][j]=='.') j--;
		if (j>=0) {
			cnt[i][j]++;
			if (grid[i][j]=='>') change[i][j] = 1;
		}
	}
	REP(j, c) {
		int i = 0;
		while (i<r && grid[i][j]=='.') i++;
		if (i<r) {
			cnt[i][j]++;
			if (grid[i][j]=='^') change[i][j] = 1;
		}
		i = r-1;
		while (i>=0 && grid[i][j]=='.') i--;
		if (i>=0) {
			cnt[i][j]++;
			if (grid[i][j]=='v') change[i][j] = 1;
		}
	}
	int ans=0;
	REP(i, r) REP(j, c) {
		if (cnt[i][j]==4) {
			printf("IMPOSSIBLE\n"); return ;
		}
		ans += change[i][j];
	}
	printf("%d\n", ans);
}

int main() {
	int t; scanf("%d", &t);
	REP(i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
