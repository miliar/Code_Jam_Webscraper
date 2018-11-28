/*
 * Author:  xioumu
 * Created Time:  2014/5/31 23:35:23
 * File Name: D.cpp
 * solve: D.cpp
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
const int maxn = 10;

int sgn(const double &x) {  return (x > eps) - (x < -eps); }

int jie[maxn], ans1, ans2;
vector<int> e[maxn];
vector<string> s;
int n, m;

void init() {
    s.clear();
    rep (i, m) {
        string tmp;
        cin >> tmp;
        s.push_back(tmp);
    }
    jie[0] = 1;
    repf (i, 1, m)
        jie[i] = jie[i - 1] * n;
}

int getDit(int w, int i) {
    int res = w % jie[i + 1];
    return res / jie[i]; 
} 

void getQue(int w) {
    rep (i, n) e[i].clear();
    rep (i, m) {
        int h = getDit(w, i);
        e[h].push_back(i); 
    }
}

set<string> st;

int getAns() {
    int res = 0;
    rep (i, n) {
        st.clear();
        if (sz(e[i]) == 0) return -1;
        rep (j, sz(e[i])) {
            int k = e[i][j];
            string ss;
            rep (r, sz(s[k])) {
                ss.push_back(s[k][r]);
                st.insert(ss);
            } 
        }
        res += sz(st) + 1;
    }
    return res;
}

void gao() {
    ans1 = -1, ans2 = 0;
    rep (i, jie[m]) {
        getQue(i);
        int res = getAns();
        if (res > ans1) {
            ans1 = res;
            ans2 = 1;
        }
        else if (res == ans1) {
            ans2++;
        }
    }
}

int main() {
    int T; 
    freopen("d.out", "w", stdout);
    scanf("%d", &T);
    repf (ca, 1, T) {
        scanf("%d %d", &m, &n);
        init();
        gao();
        printf("Case #%d: %d %d\n", ca, ans1, ans2);
    }
    return 0;
}
