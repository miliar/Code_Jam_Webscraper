#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 100010;
char s[MAXN];
int t[][4] = {
	{0, 1, 2, 3},
	{1, 0, 3, 2},
	{2, 3, 0, 1},
	{3, 2, 1, 0},
};

int sgn[][4] = {
	{1, 1, 1, 1},
	{1, -1, 1, -1},
	{1, -1, -1, 1},
	{1, 1, -1, -1},
};

int numof(char sym) {
	if (sym == 'i') {
		return 1;
	} else if (sym == 'j') {
		return 2;
	} else {
		return 3;
	}
}

void solve() {
	int l, x;
	scanf("%d %d", &l, &x);
	scanf("%s", s);
	for (int i = 0; i < x; ++i) {
    	for (int j = 0; j < l; ++j) {
    		s[i * l + j] = s[j];
    	}
	}
	int m = x * l;
	int sign = 1;
	int cur = 0;
	int st = 0;
//	cerr << l << ' ' << x << endl;
	for (int i = 0; i < m; ++i) {
		sign *= sgn[cur][numof(s[i])];
		cur = t[cur][numof(s[i])];
//		cerr << cur << ' ' << sign << endl;
		if (st == 0 && sign == 1 && cur == 1) {
			++st;
			cur = 0;
		} else if (st == 1 && sign == 1 && cur == 2) {
			++st;
			cur = 0;
		}
	}
	if (st == 2 && sign == 1 && cur == 3) {
		printf("YES\n");
	} else {
		printf("NO\n");
	}
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int t = 1; t <= tt; ++t) {
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}