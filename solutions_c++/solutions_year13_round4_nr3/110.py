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
const int MN = 2011;

int a[MN], b[MN], orig[MN], cura[MN], curb[MN];
int n;
int bminleft[MN], aminright[MN];

void solve() {
    memset(orig, 0, sizeof orig);

    FOR(turn,1,n) { // Find position of turn
        memset(cura, 0, sizeof cura);
        memset(curb, 0, sizeof curb);

        memset(bminleft, 0, sizeof bminleft);
        memset(aminright, 0, sizeof aminright);
        bminleft[0] = 1000111;
        aminright[n+1] = 1000111;

        FOR(i,1,n) {
            cura[i] = max(1, cura[i-1]);
            bminleft[i] = bminleft[i-1];

            if (orig[i]) cura[i] = max(cura[i], a[i] + 1);
            else bminleft[i] = min(bminleft[i-1], b[i]);
        }

        FORD(i,n,1) {
            curb[i] = max(1, curb[i+1]);
            aminright[i] = aminright[i+1];

            if (orig[i]) curb[i] = max(curb[i], b[i] + 1);
            else aminright[i] = min(aminright[i+1], a[i]);
        }

        // PR(cura, n);
        // PR(curb, n);
        // PR(bminleft, n);
        // PR(aminright, n);

        FOR(i,1,n)
        if (!orig[i] && cura[i] == a[i] && curb[i] == b[i])
            if (bminleft[i-1] >= b[i] + 1 && aminright[i+1] >= a[i] + 1) {
                orig[i] = turn;
                break;
            }
    }
    FOR(i,1,n) printf(" %d", orig[i]); puts("");

    FOR(i,1,n) {
        cura[i] = 1;
        FOR(j,1,i-1)
            if (orig[j] < orig[i])
                cura[i] = max(cura[i], cura[j] + 1);
    }
    FORD(i,n,1) {
        curb[i] = 1;
        FORD(j,n,i+1)
            if (orig[j] < orig[i])
                curb[i] = max(curb[i], curb[j] + 1);
    }

    FOR(i,1,n) {
        if (orig[i] < 1 || orig[i] > n) puts(":-O");
        if (cura[i] != a[i]) puts(":(");
        if (curb[i] != b[i]) puts(":)");
    }
}

int main() {
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        printf("Case #%d:", test);
        scanf("%d", &n);
        FOR(i,1,n) scanf("%d", &a[i]);
        FOR(i,1,n) scanf("%d", &b[i]);

        solve();
    }
    return 0;
}
