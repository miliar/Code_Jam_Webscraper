#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#define POW2(k) (1<<(k))
#define POW2L(k) (1ULL<<(k))
#define INSIDE(a, b) (POW2(a) & (b))
#define MERGE(a, b) (POW2(a) | (b))
#define LOWBIT(v) ((v)&(-(v)))
#define INF 0x3f3f3f3f
#define EPS 1e-10
using namespace std;

const double PI = acos(-1.0);

typedef pair<int, int> pii;
typedef long long LL;
typedef unsigned long long ULL;

template<class T1, class T2> inline bool ChkMax(T1 &a, const T2 &b) { if (a < b) { a = b; return true; } return false; }
template<class T1, class T2> inline bool ChkMin(T1 &a, const T2 &b) { if (a > b) { a = b; return true; } return false; }

#define MAXN
#define MOD 

const char *s[] = {
	"Bad magician!",
	"Volunteer cheated!"
};

int m[2][4][4];
int r[2];

int solve() {
	set<int> c;
	for (int i = 0; i < 4; ++i) {
		c.insert(m[0][r[0]][i]);
	}
	int cnt = 0;
	int tar = 0;
	for (int i = 0; i < 4; ++i) {
		if (c.find(m[1][r[1]][i]) != c.end()) {
			tar = m[1][r[1]][i];
			++cnt;
		}
	}
	if (cnt == 1) {
		return tar;
	} else if (cnt == 0) {
		return 18;
	} else {
		return 17;
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "r", stdin);
 	freopen("out", "w", stdout);
#endif

	int dataset;
	scanf("%d", &dataset);
	for (int cas = 1; cas <= dataset; ++cas) {
		for (int i = 0; i < 2; ++i) {
			cin >> r[i];
			--r[i];
			for (int a = 0; a < 4; ++a){
				for (int b = 0; b < 4; ++b) {
					cin >> m[i][a][b];
				}
			}
		}
		printf("Case #%d: ", cas);
		int ret = solve();
		if (ret > 16) {
			cout << s[ret - 17] << endl;
		} else {
			cout << ret << endl;
		}
	}

	return 0;
}
