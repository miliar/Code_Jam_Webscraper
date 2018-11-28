#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

#define INF 2000000000

#define forn(i, n) for(int i = 0; i < (int)n; ++i)

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;

const int MAXN = 100100;
string s[MAXN];
int f[MAXN];
int m, n;
int size = 0;
int to[MAXN][26];
int cnti[MAXN];
int roots[MAXN];
int cmax = 0;
int ccount = 0;

int add() {
	int ret = size++;
	forn(i, 26) {
		to[ret][i] = 0;
	}
	return ret;
}

int go(int u, int sym) {
	if (!to[u][sym]) {
		to[u][sym] = add();
	}
	return to[u][sym];
}

void gen(int str) {
	if (str >= m) {
		size = 0;
		forn(i, n) {
			roots[i] = add();
			if (cnti[i] == 0) {
				return;
			}
		}
		forn(i, m) {
			int u = roots[f[i]];
//			cout << f[i] << ' ' ;
			forn(j, s[i].length()) {
				u = go(u, s[i][j] - 'A');
			}
		}
//		cout << endl;
		if (size > cmax) {
			cmax = size;
			ccount = 1;
		} else if (size == cmax) {
			++ccount;
		}
		return;
	}
	forn(i, n) {
		f[str] = i;
		++cnti[i];
		gen(str + 1);
		--cnti[i];
	}
}

void solve() {
	scanf("%d %d", &m, &n);
	forn(i, m) {
		cin >> s[i];
	}
	cmax = 0;
	ccount = 0;
	gen(0);
	printf("%d %d\n", cmax, ccount);
}

int main(int argc, char **argv) {
//	freopen("input.txt", "r", stdin);
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int tt;
	scanf("%d\n", &tt);
	forn(t, tt) {
		printf("Case #%d: ", t + 1);
		solve();
	}
	return 0;
}
