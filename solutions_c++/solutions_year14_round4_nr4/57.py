#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

const int N = 100;
char s[N][12];
int a[N], ck[10], l[N];
int ans, ways;

void solve(int n, int m) {
    memset(ck, 0, sizeof(ck));
    for (int i = 0; i < m; i++)
        ck[a[i]]++;
    for (int i = 0; i < n; i++)
        if (ck[i] == 0)
            return;
    int cur = 0;
    for (int i = 0; i < n; i++) {
        set<string> trie;
        for (int j = 0; j < m; j++)
            if (a[j] == i)
                for (int k = 1; k <= l[j]; k++)
                    trie.insert(string(s[j], k));
        cur += trie.size() + 1;
    }
    if (cur > ans) {
        ans = cur;
        ways = 0;
    }
    if (cur == ans)
        ways++;
}

void dfs(int k, int n, int m) {
    if (k == m) {
        solve(n, m);
    } else {
        for (int i = 0; i < n; i++) {
            a[k] = i;
            dfs(k + 1, n, m);
        }
    }
}

void run(int cas) {
    int m, n;
    scanf("%d%d", &m, &n);
    for (int i = 0; i < m; i++) {
        scanf("%s", s[i]);
        l[i] = strlen(s[i]);
    }
    ans = 0;
    ways = 0;
    dfs(0, n, m);
    printf("Case #%d: %d %d\n", cas, ans, ways);
}

int main() {
    int tt, cas;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas++)
        run(cas);
    return 0;
}

