#include <set>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cassert>
using namespace std;

const int C = 26;
const int maxm = 1024;
const int maxn = 128;

const int maxT = maxm * maxn;

struct TrieNode {
    TrieNode* ch[C];
    int size;
    int cnt;
    void init() {
        memset(ch, 0, sizeof(ch));
        size = 0;
        cnt = 0;
    }

    int node_cnt() {
        int sum = 1;
        for (int i = 0; i < C; ++i) if (ch[i]) sum += ch[i]->node_cnt();
        return sum;                                                   
    }
};

TrieNode trienodes[maxT];
int next_node;

char buf[maxm][1000];

int ans;
int cnt;

void insert_trie(TrieNode* n, const char* str) {
    int ch;
    while ((ch = *str) != 0) {
        ch -= 'A';
        assert(ch < 26 && ch >= 0);
        if (n->ch[ch] == NULL) {
            n->ch[ch] = &trienodes[next_node];
            trienodes[next_node].init();
            next_node ++;
        }
        n = n->ch[ch];
        ++str;
    }
    ++n->cnt;
}

TrieNode* root = trienodes;
void trie_init() {
    next_node = 1;
    root->init();
}

int n, m;
int s[maxm];

void dfs(int c) {
    if (c == m) {
        int nans = 0;
        for (int sid = 0; sid < n; ++sid) {
            trie_init();
            for (int j = 0; j < m; ++j)
                if (s[j] == sid) {
                    insert_trie(root, buf[j]);
                }
            if (next_node > 1)
                nans += next_node;
        }
        if (nans > ans) {
            ans = nans;
            cnt = 1;
        } else if (nans == ans) ++cnt;
    } else {
        for ( s[c] = 0; s[c] < n; ++s[c])
            dfs(c + 1);
    }
}

void solve() {

    scanf("%d%d", &m, &n);
    for (int i = 0; i < m; ++i) {
        scanf("%s", buf[i]);
    }

    ans = 0;
    cnt = 0;
    dfs(0);
}

int main() {
    freopen("D.txt", "r", stdin);
    int T;
    scanf("%d", &T);
    for (int i  = 1; i <= T; ++i)  {
        solve();
        printf("Case #%d: %d %d\n", i, ans, cnt);
    }
    return 0;
}
