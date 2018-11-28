#pragma comment(linker, "/STACK:500000000")
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <bitset>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

#define y0 y0ChloeGraceMoretz
#define y1 y1ChloeGraceMoretz
#define ll long long
int nextInt() { int n; scanf("%d", &n); return n; }
ll nextLong() { ll n; scanf("%lld", &n); return n; }
const double PI = acos(-1.0);
const double EPS = 1e-9;
const int INF = (int)2e9;

int n;

int findmax(const vector<int> &v) {
	int pos = 0;
	for (int i = 1; i < v.size(); i++) {
		if (v[pos] < v[i]) {
			pos = i;
		}
	}
	return pos;
}

int minmax(const vector<int> &v, int cnt) {
	int l = 0, r = v[findmax(v)];
	while (l < r) {
		int m = (l + r) / 2;
		vector<int> ret(v);
		for (int c = 0; c < cnt; c++) {
			int pos = findmax(ret);
			int num = ret[pos];
			ret.push_back(ret[pos] - m);
			ret[pos] = m;
		}
		int pos = findmax(ret);
		if (ret[pos] <= m) {
			r = m;
		} else {
			l = m + 1;
		}
	}
	return l;
}

int main() {
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
	int t = nextInt();
	for (int tt = 1; tt <= t; ++tt) {
		n = nextInt();
		vector<int> tmp;
		for (int i = 0; i < n; i++) {
			tmp.push_back(nextInt());
		}
		int maxpos = findmax(tmp);
		int ans = (int)1e9;
		for (int k = 0; k <= tmp[maxpos]; ++k) {
			ans = min(ans, k + minmax(tmp, k));
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}