#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <stdio.h>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <list>

#define SZ(a) (int(a.size()))
#define MEM(a, val) memset(a, val, sizeof(a))
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)
#define ALL(a) a.begin(), a.end()
#define REP(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); ++(i))
#define SQR(a) ((a) * (a))

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef long double dbl;
typedef pair<int, int> pii ;
typedef vector<int> vint;
typedef vector<LL> vLL;

const int nmax = 109;
struct bush {
	int h, i, j;
	bool operator < (const bush a) const {
		return h > a.h;
	}
};

int b[nmax][nmax];
int r[nmax];
int c[nmax];
bush a[nmax * nmax];

string solve() {
	int n, m;
	scanf("%d %d", &n, &m);
	
	MEM(r, -1);
	MEM(c, -1);
	REP(i, n) {
		REP(j, m) {
			scanf("%d", &b[i][j]);
			int k = i * m + j; 
			a[k].h = b[i][j];
			a[k].i = i;
			a[k].j = j;
		}
	}
	sort(a, a + n * m);
	REP(k, n * m) {
		if (r[a[k].i] > a[k].h && c[a[k].j] > a[k].h)
			return "NO";
		else
			r[a[k].i] = max(r[a[k].i], a[k].h), c[a[k].j] = max(c[a[k].j], a[k].h);
	}
	return "YES";
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	FOR(I, 1, T) {
		string ans = solve();
		printf("Case #%d: %s\n", I, ans.c_str());
	}

	return 0;
}

