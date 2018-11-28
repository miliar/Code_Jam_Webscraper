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

int x[111];
int savea, saveb, savec;

int main() {
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        printf("Case #%d:\n", test);
        int R, N, M, K; scanf("%d%d%d%d", &R, &N, &M, &K);
        FOR(turn,1,R) {
            FOR(i,1,K) scanf("%d", &x[i]);

            savea = saveb = savec = 2;
            int cnt = 0;
            FOR(a,2,M) FOR(b,2,M) FOR(c,2,M) {
                set<int> s; s.clear();
                s.insert(1);
                s.insert(a); s.insert(b); s.insert(c);
                s.insert(a*b); s.insert(b*c); s.insert(c*a);
                s.insert(a*b*c);

                bool check = true;
                FOR(k,1,K)
                if (s.find(x[k]) == s.end()) {
                    check = false;
                    break;
                }

                if (check) {
                    ++cnt;
                    if (rand() % cnt == 0) {
                        savea = a;
                        saveb = b;
                        savec = c;
                    }
                }
            }
            cout << savea << saveb << savec << endl;
        }
    }
    return 0;
}
