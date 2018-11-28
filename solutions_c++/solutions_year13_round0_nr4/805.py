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

#define MAXKEY 40
#define MAXCONTAINERS 20

int nTC;

int nKeys, N;
int key[MAXKEY + 5];
int open[MAXCONTAINERS + 5];
vector <int> C[MAXCONTAINERS + 5];

inline void readTestData() {
	scanf("%d%d", &nKeys, &N);
	REP (i, nKeys) {
		scanf("%d", &key[i]);
		key[i]--;
	}
	
	REP (i, N) {
		scanf("%d", &open[i]);
		open[i]--;
		
		C[i].clear();
		int x;
		scanf("%d", &x);
		while (x--) {
			int y;
			scanf("%d", &y);
			y--;
			C[i].PB(y);
		}
	}
}

struct arr {
	int A[MAXKEY];
	arr() {
		REP (i, MAXKEY) A[i] = 0;
	}
};

queue <pair <int, arr> > Q;
int parent[1 << MAXCONTAINERS];

int main() {
	scanf("%d", &nTC);
	FOR (tc, 1, nTC) {
		readTestData();
		arr cnt, c2;
		REP (i, nKeys) cnt.A[key[i]]++;
		Q.push(MP(0, cnt));
		
		RESET(parent, -1);
		
		bool ret = false;
		while (!Q.empty()) {
			int bm = Q.front().F;
			cnt = Q.front().S;
			
			if (bm == (1 << N) - 1) ret = true;
			
			Q.pop();
			
			REP (i, N) {
				if (!(bm & (1 << i)) && parent[bm | (1 << i)] == -1) {
					if (cnt.A[open[i]]) {
						c2 = cnt;
						c2.A[open[i]]--;
						REP (k, SIZE(C[i])) {
							c2.A[C[i][k]]++;
						}
						Q.push(MP(bm | (1 << i), c2));
						parent[bm | (1 << i)] = i;
					}
				}
			}
		}
		printf("Case #%d:", tc);
		if (ret) {
			vector <int> ans;
			int bm = (1 << N) - 1;
			while (bm) {
				ans.PB(parent[bm] + 1);
				bm -= (1 << parent[bm]);
			}
			reverse(ALL(ans));
			REP (i, SIZE(ans)) printf(" %d", ans[i]);
		}
		else printf(" IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}

