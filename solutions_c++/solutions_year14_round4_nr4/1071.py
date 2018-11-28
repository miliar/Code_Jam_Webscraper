#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>

#define DEBUGLEVEL
#ifdef DEBUGLEVEL
#define printf_debug(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define printf_debug(fmt, args...)
#endif

typedef long long llong;

using namespace std;

const int MAXM = 8;
const int INF = 1234567890;

string s[MAXM];
int cur[MAXM];
int m, n, x, y;
int tree[100000][26];
int used[10];
int t_sz;

void add_s(int j) {
    int c = 0;
    for(int i = 0; i < (int)s[j].size(); ++i) {
        int e = s[j][i] - 'A';
        if(tree[c][e] == -1) {
            t_sz++;
            memset(tree[t_sz], -1, sizeof(tree[t_sz]));
            tree[c][e] = t_sz;
            c = t_sz;
        } else {
            c = tree[c][e];
        }
    }
}

int build_one(int j) {
    memset(tree[0], -1, sizeof(tree[0]));
    t_sz = 0;
    for(int i = 0; i < m; ++i) {
        if(cur[i] == j) {
            add_s(i);
        }
    }
    return t_sz + 1;
}

void build() {
    int ans_loc = 0;
    for(int i = 0; i < n; ++i) {
        ans_loc += build_one(i);
    }
    if(x < ans_loc) {
        x = ans_loc;
        y = 0;
    }
    if(x == ans_loc) {
        y++;
    }
}

void rec(int d) {
    if(d == m) {
        memset(used, 0, sizeof(used));
        for(int i = 0; i < m; ++i) {
            used[cur[i]] = 1;
        }
        int cnt = 0;
        for(int i = 0; i < n; ++i) {
            cnt += used[i];
        }
        if(cnt == n) {
            build();
        }
        return;
    }
    for(int i = 0; i < n; ++i) {
        cur[d] = i;
        rec(d + 1);
    }
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cin >> m >> n;
        for(int i = 0; i < m; ++i) {
            cin >> s[i];
        }
        x = -1, y = 0;
        rec(0);
        printf("Case #%d: %d %d\n", t, x, y);
    }    
    return 0;
}