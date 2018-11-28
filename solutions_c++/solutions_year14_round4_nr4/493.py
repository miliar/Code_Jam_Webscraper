#include <iostream>
using namespace std;

const int N = 10;
const int M = 1111;
const int KIND = 26;
pair<int, int> ans;
char str[M][111];
int choose[M];
int n, m;

struct Trie {
    int root, alloc;
    struct Node {
        int child[KIND];
        void init() { memset(child, 0, sizeof(child)); }
    } node[111111];
    void clear() {
        root = alloc = 0;
        node[root].init();
    }
    void insert(char *str) {
        int p = root;
        while (*str) {
            int idx = *str - 'A';
            if (!node[p].child[idx]) {
                node[++alloc].init();
                node[p].child[idx] = alloc;
            }
            p = node[p].child[idx];
            str++;
        }
    }
} trie[N];

void update(pair<int, int> &ans, int a) {
    if (ans.first < a) {
        ans = pair<int, int>(a, 1);
    } else if (ans.first == a) {
        ans.second++;
    }
}

void dfs(int id) {
    if (id == m) {
        for (int i = 0; i < n; i++) trie[i].clear();
        for (int i = 0; i < m; i++) {
            trie[choose[i]].insert(str[i]);
        }
        int t = 0;
        for (int i = 0; i < n; i++) {
            t += trie[i].alloc + (trie[i].alloc > 0);
        }
        update(ans, t);
        return;
    }
    for (int i = 0; i < n; i++) {
        choose[id] = i;
        dfs(id + 1);
    }
}

int main() {
    freopen("d-small.in", "r", stdin);
    freopen("d-small.out", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> m >> n;
        for (int i = 0; i < m; i++) {
            cin >> str[i];
        }
        ans = pair<int, int>(0, 0);
        dfs(0);
        cout << "Case #" << Case++ << ": " << ans.first << " " << ans.second << endl;
    }
    return 0;
}
