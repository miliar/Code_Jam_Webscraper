/*
 * Author:  xioumu
 * Created Time:  2013/6/1 22:29:17
 * File Name: a.cpp
 * solve: a.cpp
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

struct node {
    lint x, t;
    bool operator < (const node &b) const  {
        if (x != b.x) return x < b.x;
        else return t < b.t;
    }
    node (lint _x = 0, lint _t = 0) : x(_x), t(_t){
    }
};

vector<node> a;
lint need, ans, n, m;
priority_queue<int> que;

lint cost(lint a, lint b) {
    if (a == b) return 0;
    if (b - a == 1) return n;
    lint len = b - a;
    return (n + n - len + 1) * len / 2;
}
int main() {
    freopen("a.out", "w", stdout);
    lint T, ca = 1;
    scanf("%lld", &T);
    while (T--) {
        scanf("%lld%lld", &n, &m);
        need = 0;
        ans = 0;
        a.clear();
        rep (i, m) {
            lint s, e, p, len;
            scanf("%lld%lld%lld", &s, &e, &p);
            need += cost(s, e) * p;
            //printf("%lld\n", cost(s, e));
            rep (i, p) {
                a.push_back(node(s, 0));
                a.push_back(node(e, 1));
            }
        }
        sort(a.begin(), a.end());
        lint j = 0;
        repf (i, 1, n) {
            while (j < sz(a) && a[j].x == i) {
                if (a[j].t == 0)
                    que.push(a[j].x);
                else {
                    lint h = que.top();
                    ans += cost(h, i);
                    que.pop(); 
                }
                j++;
            }
        }
        //printf("%lld %lld\n", need, ans);
        printf("Case #%lld: ", ca++);
        printf("%lld\n", need - ans);
    }
    return 0;
}
