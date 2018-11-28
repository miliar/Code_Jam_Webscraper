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
const int MN = 1011;
const long long MOD = 1000002013LL;

map<int,int> enters, exits;
int n, m, o[MN], e[MN], p[MN];

long long get(long long from, long long to) {
    if (from == to) return 0;
    long long l = to - from;

    long long res = l * n % MOD;
    res = (res - ((l * (l-1)) / 2) % MOD + MOD) % MOD;
    return res;
}

int main() {
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        scanf("%d%d", &n, &m);

        enters.clear(); exits.clear();
        long long should = 0;

        FOR(i,1,m) {
            scanf("%d%d%d", &o[i], &e[i], &p[i]);
            enters[o[i]] += p[i];
            exits[e[i]] += p[i];

            should = (should + get(o[i], e[i]) * p[i]) % MOD;
        }

        // PR(o, m);
        // PR(e, m);
        // PR(p, m);
        // DEBUG(should);

        long long res = 0;
        for(map<int,int> :: reverse_iterator it = enters.rbegin(); it != enters.rend(); ++it) {
            long long need = it->second;
            long long start = it->first;

            vector< pair<int,int> > to; to.clear();

            for(map<int,int> :: iterator it = exits.begin(); it != exits.end(); ++it) {
                long long target = it->first;
                long long can = it->second;

                if (target < start) continue;

                can = min(can, need);
                to.push_back(make_pair(it->first, can));
                need -= can;
                if (need == 0) break;
            }

            REP(i,to.size()) {
                // cout << start << ' ' << to[i].first << ' ' << to[i].second << endl;
                exits[to[i].first] -= to[i].second;

                res += to[i].second * get(start, to[i].first) % MOD;
                res %= MOD;
            }
        }
        // DEBUG(res);
        cout << "Case #" << test << ": " << (should - res + MOD) % MOD << endl;
    }
    return 0;
}
