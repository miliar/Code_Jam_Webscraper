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
#define N 101

int n, m, t, a[33];

void dfs(int d) {
	if (m == 0) return;
	if (d >= n-3) {
		rep(i, n) printf("%d", a[i]);
		FOR(i, 3, 12) printf(" %d", i);
		printf("\n");
		m--;
		return;
	}
	dfs(d + 1);
	a[d] = a[d + 1] = 1;
	dfs(d + 2);
	a[d] = a[d + 1] = 0;
}

string name;

int main() {
	freopen("try.in", "r", stdin);
	freopen("try.out", "w", stdout);

	cin >> t;
	rep(tt, t) 
	{
		cin >> name;
		string ans = "";
		for (auto i : name)
			if (ans == "") ans = i; else
			if (i >= ans[0]) ans = i + ans; else ans += i;
		printf("Case #%d: ", tt + 1);
		cout << ans << endl;
	}
}