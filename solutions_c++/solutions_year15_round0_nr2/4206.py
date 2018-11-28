/*
 * Author:  xioumu
 * Created Time:  2015/4/11 14:56:34
 * File Name: b.cpp
 * solve: b.cpp
 */
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<iostream>
#include<vector>
#include<queue>

using namespace std;
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clr(x) memset(x,0,sizeof(x))
#define clrs( x , y ) memset(x,y,sizeof(x))
#define out(x) printf(#x" %d\n", x)
#define sqr(x) ((x) * (x))
typedef long long lint;

const int maxint = -1u>>1;
const double eps = 1e-8;
const int maxn = 1000 + 10;

int sgn(const double &x) {  return (x > eps) - (x < -eps); }

int n;
int d[maxn];
multiset<int> st;

int gao(int lim) {
    int res = 0;
    rep (i, n) {
        res += d[i] / lim + (d[i] % lim != 0) - 1;
    }
    return res;
}

int main() {
    int T, ca = 1;
    //freopen("b.out", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        int l = 1, r = 0, ans = 0;
        scanf("%d", &n);
        rep (i, n) {
           scanf("%d", &d[i]); 
           r = max(r, d[i]);
        }
        ans = r;
        repf (i, 1, r) {
            int val = gao(i);
            ans = min(val + i, ans);
            //printf ("%d %d\n", i, val);
        }
        printf("Case #%d: %d\n", ca++, ans);
    }
    return 0;
}
