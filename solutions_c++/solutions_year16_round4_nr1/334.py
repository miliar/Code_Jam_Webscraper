#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

typedef long long i64;
typedef double db;

const int N = 5e3 + 10;

int n, _r, _p, _s;
char s[N], t[N];
bool sol;

inline void Check(int a, int b, int l) {
	bool le = 0;
	for (int i = 0; i < l; ++i) {
		if (t[a + i] < t[b + i]) {
			le = 1;
			break;
		}
		else if (t[a + i] > t[b + i])
			break;
	}
	if (!le) {
		for (int i = 0; i < l; ++i)
			swap(t[a + i], t[b + i]);
	}
}

void Calc() {
	int R = 0, P = 0, S = 0;
	for (int i = 1; i <= n; ++i) {
		if (t[i] == 'R') ++R;
		if (t[i] == 'P') ++P;
		if (t[i] == 'S') ++S;
	}
	if (R != _r || P != _p || S != _s)
		return;
	if (!sol) {
		sol = 1;
		for (int i = 1; i <= n; ++i)
			s[i] = t[i];
	}
	else {
		bool le = 0;
		for (int i = 1; i <= n; ++i) {
			if (t[i] < s[i]) {
				le = 1;
				break;
			}
			else if (t[i] > s[i])
				break;
		}
		if (!le) {
			for (int i = 1; i <= n; ++i)
				swap(s[i], t[i]);
		}
	}
}

void Dfs(char c, int l, int r) {
	if (l == r) {
		t[l] = c;
		return;
	}
	int m = (l + r) >> 1;
	char a, b;
	a = c;
	if (c == 'R') b = 'S';
	if (c == 'S') b = 'P';
	if (c == 'P') b = 'R';
	Dfs(a, l, m);
	Dfs(b, m + 1, r);
	Check(l, m + 1, m - l + 1);
	if (l == 1 && r == n)
		Calc();
}

int main() {

	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; ++t) {
		printf("Case #%d: ", t);
		scanf("%d %d %d %d", &n, &_r, &_p, &_s);
		n = 1 << n;
		sol = 0;
		Dfs('R', 1, n);
		Dfs('P', 1, n);
		Dfs('S', 1, n);
		if (!sol) 
			puts("IMPOSSIBLE");
		else {
			for (int i = 1; i <= n; ++i)
				printf("%c", s[i]);
			puts("");
		}
	}

	return 0;
}
