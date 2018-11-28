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

const int MAXN = 16;
int N, K;
double prob[MAXN];

void solve() {
	scanf("%d %d", &N, &K);
	REP(i, N) scanf("%lf", &prob[i]);
	double res = 0;
	REP(i, 1<<N) {
		int c = __builtin_popcount(i);
		if (c != K) {
			continue;
		}
		VI elems;
		double tempRes = 0;
		REP(j, N) if (i & (1 << j)) elems.PB(j);
		REP(j, 1 << K) {
			int d = __builtin_popcount(j);
			if (d != K / 2) {
				continue;
			}
			double pom = 1;
			REP(k, K) {
				if (j & (1 << k)) {
					pom *= prob[elems[k]];
				} else {
					pom *= (1 - prob[elems[k]]);
				}
			}
			tempRes += pom;
		}
		if (tempRes > res) res = tempRes;
	}
	printf("%.10lf\n", res);
}

int main() {
	int t;
	scanf("%d", &t);
	REP(q, t) {
		printf("Case #%d: ", q+1);
		solve();
	}
}