#include <sstream>
#include <iomanip>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define FORN(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define DOWN(i,a,b) for(int i=a,_b=(b);i>=_b;i--)
#define SET(a,v) memset(a,v,sizeof(a))
#define sqr(x) ((x)*(x))
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair

#define DEBUG(x) cout << #x << " = "; cout << x << endl;
#define PR(a,n) cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl;
#define PR0(a,n) cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl;
using namespace std;

//Buffer reading
int INP,AM,REACHEOF;
#define BUFSIZE (1<<12)
char BUF[BUFSIZE+1], *inp=BUF;
#define GETCHAR(INP) { \
    if(!*inp) { \
        if (REACHEOF) return 0;\
        memset(BUF,0,sizeof BUF);\
        int inpzzz = fread(BUF,1,BUFSIZE,stdin);\
        if (inpzzz != BUFSIZE) REACHEOF = true;\
        inp=BUF; \
    } \
    INP=*inp++; \
}
#define DIG(a) (((a)>='0')&&((a)<='9'))
#define GN(j) { \
    AM=0;\
    GETCHAR(INP); while(!DIG(INP) && INP!='-') GETCHAR(INP);\
    if (INP=='-') {AM=1;GETCHAR(INP);} \
    j=INP-'0'; GETCHAR(INP); \
    while(DIG(INP)){j=10*j+(INP-'0');GETCHAR(INP);} \
    if (AM) j=-j;\
}
//End of buffer reading

const long double PI = acos((long double) -1.0);

#define TWO(x) (1<<(x))
#define CONTAIN(S,x) (S & TWO(x))
;

int f[TWO(20)], k, n;
int need[222];
vector<int> has[222];
bool done[222];

bool getKeys(vector<int> cur, int u, vector<int> &next) {
    next.clear();
    bool found = false;
    REP(i,cur.size()) {
        if (cur[i] == need[u] && found == false) {
            found = true;
        }
        else {
            next.push_back(cur[i]);
        }
    }
    if (!found) return false;

    REP(i,has[u].size()) {
        next.push_back(has[u][i]);
    }
    return true;
}

int get(int s, vector<int> keys) {
    if (f[s] >= 0) return f[s];

    if (s == TWO(n) - 1) return f[s] = 1;

    vector<int> next;
    REP(i,n)
    if (!CONTAIN(s, i)) {
        bool ok = getKeys(keys, i, next);
        if (!ok) continue;

        if (get(s + TWO(i), next)) {
            return f[s] = 1;
        }
    }
    return f[s] = 0;
}

int main() {
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        memset(f, -1, sizeof f);
        printf("Case #%d:", test);

        scanf("%d%d", &k, &n);
        vector<int> keys; keys.resize(k);
        REP(i,k) scanf("%d", &keys[i]);

        REP(i,n) {
            scanf("%d", &need[i]);
            int x; scanf("%d", &x);
            has[i].resize(x);
            REP(t,x) scanf("%d", &has[i][t]);
        }

        if (get(0, keys) == 0) puts(" IMPOSSIBLE");
        else {
            memset(done, false, sizeof done);
            int curS = 0;
            FOR(turn,1,n) {
                vector<int> next;
                REP(u,n) if (!done[u]) {
                    bool ok = getKeys(keys, u, next);
                    if (ok && get(curS + TWO(u), next) == 1) {
                        curS += TWO(u);
                        printf(" %d", u + 1);
                        done[u] = true;
                        keys = next;
                        break;
                    }
                }
            }
            puts("");
        }
    }
    return 0;
}

