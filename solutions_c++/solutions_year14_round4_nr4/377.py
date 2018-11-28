// Rain Dreamer MODEL
// Create @ 22:48 05-31 2014
// Comment - 

#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <map>
#include <set>

using namespace std;

// Self Template Code BGEIN

#define sz(x) ((int)((x).size()))
#define out(x) printf(#x" %d\n", x)
#define all(x) (x).begin(), (x).end()
#define RD(x) freopen (x, "r", stdin)
#define WT(x) freopen (x, "w", stdout)
#define clz(x) memset (x, 0, sizeof(x))
#define cln(x) memset (x, -1, sizeof(x))
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define repf(i,a,b) for (int i = (a); i <= (b); ++i)
#define repd(i,a,b) for (int i = (a); i >= (b); --i)
#define repcase int t, Case = 1; for (scanf ("%d", &t); t; --t)
#define repeach(i,x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)

typedef long long int64;
typedef pair<int, int> pii;

int sgn(double x) { return (x > 1e-8) - (x < -1e-8); }
int count_bit(int x) { return x == 0? 0 : count_bit(x >> 1) + (x & 1); }

template<class T> inline void ckmin(T &a, const T b) { if (b < a) a = b; }
template<class T> inline void ckmax(T &a, const T b) { if (b > a) a = b; }

// Self Template Code END

int calc_lcp(string s1, string s2) {
    int res = 0;
    for (; res < sz(s1) && res < sz(s2); ++res) {
        if (s1[res] != s2[res]) {
            break;
        }
    }
    return res;
}

int calc_trie_nodes(vector<string> v) {
    sort (all(v));
    int res = 1;
    rep (i, sz(v) - 1) {
        res += sz(v[i]);
        res -= calc_lcp(v[i], v[i + 1]);
    }
    res += sz(v[sz(v) - 1]);
    return res;
}

string s[10];
int n, m, ans, ans_num, g[10];

void calc_ans() {
    vector<string> vs[4];
    rep (i, n) {
        vs[g[i]].push_back(s[i]);
    }
    int res = 0;
    rep (i, m) {
        if (sz(vs[i]) == 0) {
            return;
        }
        res += calc_trie_nodes(vs[i]);
    }
    if (res == ans) {
        ans_num += 1;
    } else if (res > ans) {
        ans = res;
        ans_num = 1;
    }
}

void dfs(int x) {
    if (x == n) {
        calc_ans();
        return ;
    }
    rep (i, m) {
        g[x] = i;
        dfs (x + 1);
    }
}

int main() {
    WT ("D.out");
    
    repcase {
        scanf ("%d%d", &n, &m);
        rep (i, n) {
            char buf[12];
            scanf ("%s", buf);
            s[i] = string(buf);
        }
        ans = -1;
        dfs (0);
        printf ("Case #%d: %d %d\n", Case++, ans, ans_num);
    }
    return 0;
}

