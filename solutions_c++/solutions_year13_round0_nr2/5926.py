#define debug if(1)
// Grzegorz Guspiel
#include <algorithm>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
 
#define REP(i,n) for(int i=0;i<int(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<int(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=((int)(a))-1; i>=int(b); --i)
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second

// In g++, you can use the little known __uint128_t type.

const int maxn = 110;

PII t[maxn][maxn];
int n, m;

void align(vector<PII*> all) {
    int m = 0;
    FOREACH(i,all) m = max(m, (*i)->st);
    FOREACH(i,all) (*i)->nd = min((*i)->nd, m);
}

bool solved() {
    REP(i,n) REP(j,m) if(t[i][j].st != t[i][j].nd) return 0;
    return 1;
}

int main() {
	int z; scanf("%d", &z);
    int cid = 1;
	while(z--) {
        scanf("%d%d", &n, &m);
        REP(i,n) REP(j,m) scanf("%d", &t[i][j].st);
        REP(i,n) REP(j,m) t[i][j].nd = 100;
        REP(i,n) {
            vector<PII*> all;
            REP(j,m) all.pb(&t[i][j]);
            align(all);
        }
        REP(j,m) {
            vector<PII*> all;
            REP(i,n) all.pb(&t[i][j]);
            align(all);
        }
        printf("Case #%d: %s\n", cid++, solved() ? "YES" : "NO");
}
	return 0;
}
