#include <algorithm>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>

#define clr(a,b) memset(a,b,sizeof(a))
#define cpy(a,b) memcpy(a,b,sizeof(a))
#define rep(i,n) for(int i=0; i<n; i++)

using namespace std;

inline int LL(int x) { return x<<1; }
inline int RR(int x) { return x<<1|1; }

#define lson l, m, LL(rt)
#define rson m+1, r, RR(rt)

const double eps = 1e-8;
const double pi = acos(-1.0);
const double inf = 1e20;

inline bool eq(double x, double y) {
    return fabs(x - y) < eps;
}

const int INF = 0x3f3f3f3f;

const int N = 10100;

int s[N];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, cas(0);
    scanf("%d", &T);
    while(T--) {
        int n, X;
        scanf("%d%d", &n, &X);
        for(int i=0; i<n; i++) {
            scanf("%d", &s[i]);
        }
        sort(s, s+n);
        int l = 0, r = n-1, ans(0);
        while(r > l) {
            if(s[r]+s[l] > X) {
                ++ ans;
                -- r;
            } else {
                ++ ans;
                ++ l;
                -- r;
            }
        }
        if(r == l) ++ ans;
        printf("Case #%d: %d\n", ++cas, ans);
    }

    return 0;
}
