#include <string>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <queue>
#pragma warning(disable:4996)

using namespace std;
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define rep(i,n) for (int i=0; i<n; i++)
#define FOR(i,a,b) for (int i=a; i<b; i++)
#define ll long long
#define N 111

int n, m, t, p[N];
int *a[N];
int b[N][N];

bool cmp(const int *a, const int *b) {
	rep(i, n) if (a[i] != b[i]) return a[i] < b[i];
	return false;
}


bool judge(int k, int p) {
	rep(i, n) 
		if (b[k][i] > 0) 
			if (b[k][i] != a[p][i] || (k && a[p][i] <= b[k - 1][i])) return false;
	return true;
}
bool judge2(int k, int p) {
	rep(i, n) 
		if (b[i][k] > 0)
			if (b[i][k] != a[p][i] || (k && a[p][i] <= b[i][k - 1])) return false;
	return true;
}

bool finish;
void dfs(int d) {
	if (finish) return;
	if (d == m) {
		rep(i, n) rep(j, n) if (!b[i][j]) return;
		finish = true;
		rep(i, 2 * n) if (!p[i]) {
			rep(j, n) if (i < n) printf(" %d", b[i][j]); else printf(" %d", b[j][i-n]);
			printf("\n");  break;
		}
		return;
	}
	int c[50];
	rep(k, n) if (!p[k] && judge(k, d)) { 
		rep(i, n) c[i] = b[k][i], b[k][i] = a[d][i];
		p[k] = 1;
		dfs(d + 1); 
		p[k] = 0;
		rep(i, n) b[k][i] = c[i]; break;
	}
	rep(k, n) if (!p[k+n] && judge2(k, d)) {
		rep(i, n) c[i] = b[i][k], b[i][k] = a[d][i];
		p[k + n] = 1;;
		dfs(d + 1); 
		p[k + n] = 0;
		rep(i, n) b[i][k] = c[i]; break;
	}
}
int main() {
	freopen("try.in", "r", stdin);
	freopen("try.out", "w", stdout);

	cin >> t;
	rep(tt, t) 
	{
		finish = false;
		cin >> n;
		m = n * 2 - 1;
		rep(i, m) {
			a[i] = new int[n];
			rep(j, n) cin >> a[i][j];
		}
		memset(b, 0, sizeof(b));
		memset(p, 0, sizeof(p));
		sort(a, a + m, cmp);
		rep(i, n) p[0] = 1, b[0][i] = a[0][i];
		printf("Case #%d:", tt + 1);
		dfs(1);
	}
}