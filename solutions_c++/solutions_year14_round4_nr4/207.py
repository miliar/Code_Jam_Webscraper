#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

#define MAXN 128
#define MAXC 26
#define MOD 1000000007
#define IDX(x) ((x) - 'A')

using namespace std;

struct Trie {
    int nxt[MAXN][MAXC], tag[MAXN], sz;

    void clear() {
        memset(nxt, 0, sizeof(nxt));
        memset(tag, 0, sizeof(tag));
        sz = 1;
    }

    void insert(const char *str, int key) {
        int cur = 0;
        for ( ; *str; ++str) {
            if (!nxt[cur][IDX(*str)]) nxt[cur][IDX(*str)] = sz++;
            cur = nxt[cur][IDX(*str)];
        }
        tag[cur] = key;
    }

    int size() const { return sz; }
} trie[8];

string dic[16];
int st[16], sum[16];

inline void add(int &a, int b) {
    if ((a += b) >= MOD) a -= MOD;
}

void dfs(int m, int n, int k, int &ans, int &cnt) {
    int i, cur;

    if (k == m) {
        memset(sum, 0, sizeof(sum));
        for (i = 0; i < m; ++i) ++sum[st[i]];
        for (i = 0; i < n; ++i) {
            if (!sum[i]) return;
        }

        for (i = 0; i < n; ++i) trie[i].clear();
        for (i = 0; i < m; ++i) {
            trie[st[i]].insert(dic[i].c_str(), i + 1);
        }
        for (cur = i = 0; i < n; ++i) cur += trie[i].size();

        if (ans < cur) {
            ans = cur; cnt = 1;
        } else if (ans == cur) {
            add(cnt, 1);
        }
        return;
    }
    for (i = 0; i < n; ++i) {
        st[k] = i;
        dfs(m, n, k + 1, ans, cnt);
    }
}

int main() {
    int t, ct = 0, m, n, ans, cnt, i;

    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &m, &n);
        for (i = 0; i < m; ++i) cin >> dic[i];
        dfs(m, n, 0, ans = 0, cnt = 0);
        printf("Case #%d: %d %d\n", ++ct, ans, cnt);
    }

    return 0;
}
