#include <bits/stdc++.h>
using namespace std;

int Ans, ways, n, m;

struct Trie {
    int ne[26];
};
Trie tr[1000010];

char s[1000][1000];

int Cnt, from[100];

int newNode(int &Cnt) {
    memset(tr[Cnt].ne, -1, sizeof(tr[Cnt].ne));
    int ans = Cnt;
    Cnt++;
    return ans;
}

void dfs(int ss, int e, int n) {
    if (ss == e) {
        bool sol = true;
        int tot = 0;
        for (int i = 0; i < n; i++) {
            Cnt = 0;
            int root = newNode(Cnt);
            int x = 0;
            for (int j = 0; j < m; j++) {
                if (from[j] != i) continue;
                x++;
                int now = root;
                for (int k = 0; s[j][k]; k++) {
                    if (tr[now].ne[s[j][k] - 'A'] == -1) {
                        tr[now].ne[s[j][k] - 'A'] = newNode(Cnt);
                    }
                    now = tr[now].ne[s[j][k] - 'A'];
                }
            }
            if (x == 0) sol = false;
            //printf("%d ", Cnt);
            tot += Cnt;
        }
        if (sol == false) return;
        //puts("");
        if (Ans < tot) {
            Ans = tot;
            ways = 1;
        } else if (Ans == tot) {
            ways++;
        }
    } else {
        for (int i = 0; i < n; i++) {
            from[ss] = i;
            dfs(ss + 1, e, n);
        }
    }
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &m, &n);
        for (int i = 0; i < m; i++) {
            scanf("%s", s[i]);
        }
        for (int i = 0; i < m; i++) {
            from[i] = 0;
        }
        Ans = -1;
        dfs(0, m, n);
        printf("Case #%d: %d %d\n", cas, Ans, ways);
    }
    return 0;
}
