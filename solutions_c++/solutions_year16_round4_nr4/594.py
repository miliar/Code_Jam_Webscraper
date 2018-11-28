#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <list>
#include <ctime>
#include <sstream>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
#define FOR(x, b, e) for(int x=(b); x<=(e); ++x)
#define FORD(x, b, e) for(int x=((int)(b))-1; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) ((int)((x).size()))
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define mp(x,y) make_pair(x,y)
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FOREACH(it, (x)) cerr <<*it <<", "; cout <<endl; }}
typedef short int sint;

const int MAXN = 4;
int N, mask;
bool mog[MAXN][MAXN];
bool can[1 << (MAXN * MAXN)];

bool zaj[MAXN];
VI um[MAXN];
int kol[MAXN];

bool proba(int kt) {
	if (kt == N) return true;
	bool moge = false;
	REP(i, SIZE(um[kol[kt]])) {
		int elem = um[kol[kt]][i];
		if (!zaj[elem]) {
			zaj[elem] = true;
			bool wynProb = proba(kt + 1);
			if (wynProb == false) {
				return false;
			} else {
				moge = true;
			}
			zaj[elem] = false;
		}
	}
	return moge;
}

bool czy(int c) {
	REP(i, N) {
		um[i].clear();
		REP(j, N) if (c & (1 << (i * N + j))) {
			um[i].PB(j);
		}
	}
	REP(i, N) kol[i] = i;
	bool ok = true;
	do {
		REP(i, N) zaj[i] = false;
		if (!proba(0)) {
			return false;
		}
	} while(next_permutation(kol, kol + N));
	return true;
}

void preq() {
	REP(i, 1 << (N * N)) {
		can[i] = czy(i);
		// if(can[i]) printf("can[%d] = %d\n", i, can[i]);
	}
}

void solve() {
	cin >> N;
	mask = 0;
	REP(i, N) {
		string x;
		cin >> x;
		REP(j, N) {
			mog[i][j] = x[j] - '0';
			if (mog[i][j]) {
				mask |= (1 << (i * N + j));
			}
		}
	}
	preq();
	// printf("mask: %d\n", mask);
	int res = N * N;
	REP(i, (1 << (N * N))) {
		if ((i & mask) == mask && can[i]) {
			// printf("can[%d] = true\n", i);
			res = min(res, __builtin_popcount(i) - __builtin_popcount(mask));
		}
		can[i] = false;
	}
	cout << res << endl;
}

int main() {
	int t;
	cin >> t;
	REP(q, t) {
		cout << "Case #" << q+1 << ": ";
		solve();
	}
}