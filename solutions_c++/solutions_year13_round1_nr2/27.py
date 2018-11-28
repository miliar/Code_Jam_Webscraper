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

const int MN = 10111;

int start[MN], last[MN];
pair<int,int> v[MN];
int E, R, n;

int main() {
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        scanf("%d%d%d", &E, &R, &n);
        FOR(i,1,n) {
            scanf("%d", &v[i].first);
            v[i].second = i;

            start[i] = E; last[i] = 0;
        }
        sort(v+1, v+n+1, greater< pair<int,int> > ());

        long long res = 0;
        FOR(turn,1,n) {
            int i = v[turn].second;
            res += (v[turn].first) * (long long) (start[i] - last[i]);

            int cur = last[i], u = i;
            while (cur + R < E && u < n) {
                ++u;
                cur += R;
                start[u] = min(start[u], cur);
            }

            cur = start[i]; u = i;
            while (cur - R > 0 && u > 1) {
                --u;
                cur -= R;
                last[u] = max(last[u], cur);
            }
        }
        printf("Case #%d: %lld\n", test, res);
    }
    return 0;
}
