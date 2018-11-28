#include <algorithm>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <set>
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

char s[1010];
int a[1010];
int ans, num;
vector<string> vv[10];
vector<string> vs;

int sz;
int ch[88][26];

void Insert(string s) {
    int p = 0;
    for(int i=0; i<s.length(); i++) {
        int t = s[i] - 'A';
        if(!ch[p][t]) {
            ch[p][t] = sz ++;
        }
        p = ch[p][t];
    }
}

int solve(vector<string> & v) {
    clr(ch, 0);
    sz = 1;
    for(int i=0; i<v.size(); i++) {
        Insert(v[i]);
    }
    return sz;
}

void dfs(int x, int n, int m) {
    if(x == m) {
        set<int> s;
        for(int i=0; i<m; i++) {
            s.insert(a[i]);
        }
        if(s.size() < n) return;
        int tmp = 0;
        for(int i=0; i<n; i++) vv[i].clear();
        for(int i=0; i<m; i++) {
            vv[a[i]].push_back(vs[i]);
        }
        for(int i=0; i<n; i++) {
            tmp += solve(vv[i]);
        }
        if(ans < tmp) {
            ans = tmp;
            num = 1;
        } else if(ans == tmp) {
            ++ num;
        }
    } else for(int i=0; i<n; i++) {
        a[x] = i;
        dfs(x+1, n, m);
    }
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        int n, m;
        scanf("%d%d", &m, &n);
        vs.clear();
        for(int i=0; i<m; i++) {
            scanf("%s", s);
            vs.push_back(string(s));
        }
        ans = 0;
        num = 0;
//        if(n == 1) {
//            ans = solve(vs);
//        } else if(n == 2) {
//            int t = (1<<m);
//            for(int i=1; i<t; i++) {
//                vector<string> s0, s1;
//                for(int j=0; j<m; j++) {
//                    if(i&(1<<j)) {
//                        s1.push_back(vs[j]);
//                    } else {
//                        s0.push_back(vs[j]);
//                    }
//                }
//                int tmp = solve(s1) + solve(s0);
//                if(tmp > ans) {
//                    ans = tmp;
//                    num = 1;
//                } else if(tmp == ans) {
//                    ++ tmp;
//                }
//            }
//        } else {
            dfs(0, n, m);
//        }
        printf("Case #%d: %d %d\n", cas, ans, num);
    }
    return 0;
}
