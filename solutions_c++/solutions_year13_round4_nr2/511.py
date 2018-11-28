/*
 * Author:  xioumu
 * Created Time:  2013/6/1 23:37:08
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
#define rep(i, n) for (lint i = 0; i < (n); ++i)
#define repf(i, a, b) for (lint i = (a); i <= (b); ++i)
#define repd(i, a, b) for (lint i = (a); i >= (b); --i)
#define clr(x) memset(x,0,sizeof(x))
#define clrs( x , y ) memset(x,y,sizeof(x))
#define out(x) printf(#x" %lld\n", x)
#define sqr(x) ((x) * (x))
typedef long long lint;

const lint maxlint = -1u>>1;
const double eps = 1e-8;

lint sgn(const double &x) {  return (x > eps) - (x < -eps); }

lint n, m;

lint two(lint w) {
    return 1LL << w;
}

lint gao1(lint n, lint m) {
    lint now = n, res = 1;
    repf (i, 1, n) {
        if (two(n) - two(n - i + 1) + 1 <= m)
            res = i;
        else break;
    }
    if (m == two(n))
        return two(n);
    return two(res) - 1;
}

lint gao2(lint n, lint m) {
    lint now = n, res = 0;
    repd (i, n, 1) {
        if (two(i) <= m) {
            res = i;
            break;
        }
    }
    //printf("%lld\n", res);
    lint h = two(n - res);
    return two(n) - h;
}

int main() {
    freopen("b.out", "w", stdout);
    lint T, ca = 1;
    scanf("%lld", &T);
    while (T--) {
        scanf("%lld%lld", &n, &m);
        lint ans1, ans2;
        ans1 = gao1(n, m) - 1;
        ans2 = gao2(n, m);
        printf("Case #%lld: ", ca++);
        printf("%lld %lld\n", ans1, ans2);
    }
    return 0;
}
