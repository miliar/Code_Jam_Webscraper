#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cmath>
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REP1(i, n) for (int i = 1; i <= (n); ++i)
#define FOR(i, a, b) for (int i = (a); i <= (b); ++i)
#define CLR(x, n) memset(x, n, sizeof(x))
#define maxN 110
using namespace std;

void setIO(string name) {
	string in_f = name + ".in";
	string out_f = name + ".out";
	freopen(in_f.c_str(), "r", stdin);
	freopen(out_f.c_str(), "w", stdout);
}

int ht[maxN][maxN];
int n, m;
bool cut[maxN][maxN];
bool row[maxN], col[maxN];

void init() {
	scanf("%d%d", &n, &m);
	REP1(i, n) REP1(j, m) scanf("%d", ht[i] + j);
	CLR(cut, 0);
}

void solve() {
	REP1(h, 100) {
		CLR(row, 1), CLR(col, 1);
		REP1(i, n) REP1(j, m) {
			if (ht[i][j] > h) row[i] = col[j] = 0;
		}
		REP1(i, n) {
			if (row[i]) {
				REP1(j, m) if (ht[i][j] == h) cut[i][j] = 1;
			}
		}
		REP1(j, m) {
			if (col[j]) {
				REP1(i, n) if (ht[i][j] == h) cut[i][j] = 1;
			}
		}
	}
	REP1(i, n) REP1(j, m) {
		if (!cut[i][j]) {
			puts("NO");
			return;
		}
	}
	puts("YES");
}

int main() {
//	setIO("2");
	int TT;
	scanf("%d", &TT);
	REP1(i, TT) {
		printf("Case #%d: ", i);
		init();
		solve();
	}
	return 0;
}
