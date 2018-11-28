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

const int MAXN = 5001;
int N;
int t[3];
	VI cur;

char znak(int x) {
	if (x == 0) return 'R';
	if (x == 1) return 'P';
	return 'S';
}

void minimuj(int p, int q) {
	if (p + 1 == q) return;
	int sr = (p + q) / 2;
	int dl = (q - p) / 2;
	// printf("printfuj: %d %d\n",p,q);
	minimuj(p, sr);
	minimuj(sr, q);
	bool swapuj = false;
	REP(i, dl) {
		if (znak(cur[p + i]) > znak(cur[sr + i])) {
			swapuj = true;
			break;
		} else if (znak(cur[p + i]) < znak(cur[sr + i])) {
			swapuj = false;
			break;
		}
	}
	if (swapuj) {
		REP(i, dl) {
			swap(cur[p+i], cur[sr+i]);
		}
	}
}

// 0 - R, 1 - P, 2 - S
bool proba(int x) {
	cur.clear();
	cur.PB(x);
	REP(i, N) {
		VI pom;
		REP(j, SIZE(cur)) {
			if (cur[j] == 0) {
				pom.PB(0);
				pom.PB(2);
			} else if (cur[j] == 1) {
				pom.PB(1);
				pom.PB(0);
			} else {
				pom.PB(1);
				pom.PB(2);
			}
		}
		cur = pom;
	}
	int cnts[3];
	REP(i, 3) cnts[i] = 0;
	REP(i, SIZE(cur)) cnts[cur[i]]++;
	REP(i, 3) if (cnts[i] != t[i]) return false;
	minimuj(0, SIZE(cur));
	REP(i, SIZE(cur)) {
		printf("%c", znak(cur[i]));
	}
	printf("\n");
	return true;
}

void solve() {
	scanf("%d", &N);
	REP(i, 3) {
		scanf("%d", &t[i]);
	}
	REP(i, 3) {
		if (proba(i)) {
			return;
		}
	}
	printf("IMPOSSIBLE\n");
}

int main() {
	int t;
	scanf("%d", &t);
	REP(q, t) {
		printf("Case #%d: ", q+1);
		solve();
	}
}