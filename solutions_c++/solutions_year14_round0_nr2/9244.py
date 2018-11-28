// BEGIN CUT HERE
/*

*/
// END CUT HERE
#line 7 "AmebaDiv1.cpp"
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <set>
#include <functional>
#include <numeric>
#include <sstream>
#include <stack>
#include <map>
#include <queue>

#define CL(arr, val)    memset(arr, val, sizeof(arr))
#define REP(i, n)       for((i) = 0; (i) < (n); ++(i))
#define FOR(i, l, h)    for((i) = (l); (i) <= (h); ++(i))
#define FORD(i, h, l)   for((i) = (h); (i) >= (l); --(i))
#define L(x)    (x) << 1
#define R(x)    (x) << 1 | 1
#define MID(l, r)   (l + r) >> 1
#define Min(x, y)   (x) < (y) ? (x) : (y)
#define Max(x, y)   (x) < (y) ? (y) : (x)
#define E(x)        (1 << (x))
#define iabs(x)     (x) < 0 ? -(x) : (x)
#define OUT(x)  printf("%I64d\n", x)
#define Read()  freopen("data.in", "r", stdin)
#define Write() freopen("data.out", "w", stdout)
#define PB      push_back

#define CROL(value, bits, xx) ((value << bits) | (value >> (xx - bits)))

typedef long long LL;
const double eps = 1e-6;
const double PI = acos(-1.0);
const double INF = 1e11;
const int inf = 0x1F1F1F1F;
const int MOD = 1e9+7;

using namespace std;
const int N = 110;

int main() {
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int T, i, cas = 0;
    double c, f, x;
    double per, sec, tmp, ans;
    scanf("%d", &T);
    while(T--) {
        scanf("%lf%lf%lf\n", &c, &f, &x);
        per = 2;
        sec = 0;
        ans = x/per;
        for(i = 1; i <= int(x) + 1; ++i) {
            tmp = sec + c/per + x/(per + f);
            //printf("%lf %lf %lf\n", sec, per, tmp);
            ans = min(ans, tmp);
            sec += c/per;
            per += f;
        }
        printf("Case #%d: %.7f\n", ++cas, ans);
    }
    return 0;
}
