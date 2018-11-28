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

int n, t;
bool a[N];

int dfs(int d, bool p) {
	if (d == 0) return a[d] != p;
	if (a[d] == p) return dfs(d - 1, p);
	return dfs(d - 1, !p) + 1;
}

int main() {
	freopen("try.in", "r", stdin);
	freopen("try.out", "w", stdout);

	scanf("%d", &t);
	rep(tt, t) 
	{
		string s;
		cin >> s;
		n = s.length();
		rep(i, n) a[i] = (s[i] == '+');
		printf("Case #%d: %d\n", tt + 1, dfs(n - 1, true));
	}
}