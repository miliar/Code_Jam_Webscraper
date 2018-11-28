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

int n;
long long p;

long long get1(long long better, long long cost) {
    if (better == 0) return 0;
    return get1((better - 1) / 2, cost / 2) + cost;
}

long long solve1() {
    long long left = 1, right = 1LL << n, res = 0;
    while (left <= right) {
        long long mid = (left + right) / 2;
        if (get1(mid - 1, 1LL << (n-1)) < p) {
            res = mid;
            left = mid + 1;
        }
        else right = mid - 1;
    }
    return res - 1;
}

long long get2(long long worse, long long nTeam) {
    if (worse == 0) return nTeam;
    return get2((worse - 1) / 2, nTeam / 2);
}

long long solve2() {
    long long left = 1, right = 1LL << n, res = 0;
    long long nTeam = right;
    while (left <= right) {
        long long mid = (left + right) / 2;
        if (get2(nTeam - mid, nTeam) <= p) {
            res = mid;
            left = mid + 1;
        }
        else right = mid - 1;
    }
    return res - 1;
}

int main() {
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        cin >> n >> p;
        long long res1 = solve1(), res2 = solve2();
        cout << "Case #" << test << ": " << res1 << ' ' << res2 << endl;
    }
    return 0;
}
