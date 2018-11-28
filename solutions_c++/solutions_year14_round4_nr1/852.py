#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
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

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int n, x;
int cnt[1000];

void solve() {
	scanf("%d%d", &n, &x);
	REP(i, 777) cnt[i] = 0;
	REP(i, n) { int y; scanf("%d", &y); cnt[y]++; }
	int res = 0;
	int l = 0; int r = 700;
	while (l<=r) {
		while (cnt[l]==0 && l<=r) l++;
		while (cnt[r]==0 && r>=l) r--;
		if (l>r) break;
		res++;
		cnt[r]--;
		if (l+r<=x && cnt[l]>0) cnt[l]--;
		//printf("%d %d %d\n", l, r, cnt[r]);
	}
	printf("%d\n", res);
}

int main() {
	int t; scanf("%d", &t);
	REP (i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
