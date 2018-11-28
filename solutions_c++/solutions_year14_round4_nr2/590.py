#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#define RD(x)      scanf("%d", &x)
#define REP(i, n)  for (int i=0; i<(n); i++)
#define FOR(i, n) for (int i=1; i<=(n); i++)
#define pii        pair<int, int>
#define mp         make_pair
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

using namespace std;
#define  N   1160
#define  M   22222
#define  eps 1e-9
#define  pi  acos(-1.0)
#define  inf 0XFFFFFFFll
#define  mod 9999991ll
#define  LL  long long

int a[N];
int Main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; RD(T);
	FOR(_T, T) {
		int n; RD(n);
		FOR(i, n) RD(a[i]);
		int l = 1, r = n;
		int ans = 0;
		while (l < r) {
			int val = a[l], w = l;
			for (int i=l; i<=r; i++) {
				if (a[i] < val) {
					val = a[i];
					w = i;
				}
			}
			if (r - w > w - l) {
				ans += w - l;
				for (int i=w; i>l; i--)
					a[i] = a[i-1];
				l++;
			} else {
				ans += r - w;
				for (int i=w; i<r; i++)
					a[i] = a[i+1];
				r--;
			}
		}
		printf("Case #%d: %d\n", _T, ans);
	}
	return 0;
}
int main() {
	return Main();
}
