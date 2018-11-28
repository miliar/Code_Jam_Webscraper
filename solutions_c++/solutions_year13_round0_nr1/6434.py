#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <memory.h>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <cassert>

#define oo 1000111000

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for(int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for(int i = (a), _b = (b); i >= _b; i--)
#define FOREACH(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

#define PB push_back
#define MP make_pair
#define SIZE(c) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define RESET(c,x) memset(c,x,sizeof(c))
#define F first
#define S second

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

template <class T> inline T MAX(T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN(T a, T b) { if (a < b) return a; return b; }
template <class T> inline T ABS(T x) { if (x < 0) return -x; return x; }

inline void OPEN(const string &s) {
	freopen((s + ".in").c_str(), "r", stdin);
	freopen((s + ".out").c_str(), "w", stdout);
}

// template by ptrrsn_1

bool isX(char c) {
	return c == 'X' || c == 'T';
}

bool isO(char c) {
	return c == 'O' || c == 'T';
}

int nTC;
char M[4][4];

int main() {
	scanf("%d", &nTC);
	
	FOR (tc, 1, nTC) {
		REP (i, 4) scanf("%s", M[i]);
		bool X = false, O = false, xtmp, otmp;
		// cek baris
		REP (i, 4) {
			xtmp = true;
			otmp = true;
			REP (j, 4) {
				if (!isX(M[i][j]))
					xtmp = false;
				if (!isO(M[i][j]))
					otmp = false;
			}
			if (xtmp) X = true;
			if (otmp) O = true;
		}
		// cek kolom
		REP (j, 4) {
			xtmp = true;
			otmp = true;
			REP (i, 4) {
				if (!isX(M[i][j]))
					xtmp = false;
				if (!isO(M[i][j]))
					otmp = false;
			}
			if (xtmp) X = true;
			if (otmp) O = true;
		}
		// cek diagonal
		xtmp = true;
		otmp = true;
		REP (i, 4) {
			if (!isX(M[i][i]))
				xtmp = false;
			if (!isO(M[i][i]))
				otmp = false;
		}
		if (xtmp) X = true;
		if (otmp) O = true;
		
		xtmp = true;
		otmp = true;
		REP (i, 4) {
			if (!isX(M[i][3 - i]))
				xtmp = false;
			if (!isO(M[i][3 - i]))
				otmp = false;
		}
		if (xtmp) X = true;
		if (otmp) O = true;
		
		printf("Case #%d: ", tc);
		
		bool full = true;
		REP (i, 4) REP (j, 4) if (M[i][j] == '.') {
			full = false;
			break;
		}
		
		if (X == O && full) printf("Draw");
		else if (X) printf("X won");
		else if (O) printf("O won");
		else printf("Game has not completed");
		
		printf("\n");
	}
	
	return 0;
}

