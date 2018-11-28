#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <vector>
#include <string>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
#define bitAt(x, k) (((x) >> (k)) & 1)
typedef long long LL;
typedef long double LD;
const int MOD = 1000000000 + 7;
const int INF = 1000000000;
const double EPS = 1e-9;
const double PI = acos(-1.0);

int trie[10000][26], a[1005], c[10000], n, m;
char s[1005][200];

int calc() {
    int ret = 0;
    for (int i = 1; i <= n; ++i) {
        int tot = 0;
        memset(trie[0], 0, sizeof(trie[0]));
        int tmp = 0;
        for (int j = 1; j <= m; ++j) {
            if (a[j] == i) {
                ++tmp;
                for (int k = 0, o = 0; k < strlen(s[j]); ++k) {
                    char ch = s[j][k] - 'A';
                    if (!trie[o][ch]) {
                        trie[o][ch] = ++tot;
                        memset(trie[tot], 0, sizeof(trie[tot]));
                    }
                    o = trie[o][ch];
                }
            }
        }
        ret += tot + 1;
        if (tmp == 0) {
            return -1;
        }
    }
    return ret;
}

void dfs(int i) {
    if (i > m) {
        int xx = calc();
        if (xx != -1) {
            ++c[xx];
        }
        return;
    }
    for (int j = 1; j <= n; ++j) {
        a[i] = j;
        dfs(i + 1);
    }
}

void solve() {
    memset(c, 0, sizeof(c));
    scanf("%d%d", &m, &n);
    for (int i = 1; i <= m; ++i) {
        scanf("%s", s[i]);
    }
    dfs(1);
    for (int i = 5000; i >= 1; --i) {
        if (c[i] > 0) {
            printf("%d %d\n", i, c[i]);
            break;
        }
    }
}

int main() {
    //freopen("D.in", "r", stdin);
    int test;
    scanf("%d", &test);
    for (int kase = 1; kase <= test; ++kase) {
        printf("Case #%d: ", kase);
        solve();
    }
    return 0;
}
