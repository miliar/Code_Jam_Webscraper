#include <stdio.h>
#include <string.h>

int casN, n, cnt;
int a[2010], b[2010], ans[2010], vis[2010], add[2010][2010];
unsigned conn[2010][70];

inline bool isConnect(int x, int y) {
    if (add[x][y]) return true;
    if (x < y) {
        return a[y] <= a[x];
    } else if (x > y) {
        return b[y] <= b[x];
    }
    return false;
}

inline void set(int v, int i) {
    conn[v][i>>5] |= 1u<<(i&31);
}
inline bool get(int v, int i) {
    return (conn[v][i>>5] & (1u<<(i&31)) ) != 0;
}
inline void mergeTo(int to, int from) {
    for (int i=0; i<((n+31)>>5); i++) {
        conn[to][i] |= conn[from][i];
    }
}

void DFS(int v) {
    for (int i=0; i<n; i++) {
        if (isConnect(v, i)) {
            if (!vis[i]) {
                vis[i] = 1;
                DFS(i);
            }
            mergeTo(v, i);
        }
    }
}

void Fill(int v) {
    for (int i=0; i<n; i++) {
        if (i==v || ans[i] || !get(v, i)) continue;
        Fill(i);
    }
    ans[v] = ++cnt;
}

int main() {
    scanf("%d", &casN);
    for (int casI = 0; casI < casN; casI++) {
        scanf("%d", &n);
        for (int i=0; i<n; i++){
            scanf("%d", &a[i]);
        }
        for (int i=0; i<n; i++) {
            scanf("%d", &b[i]);
        }
        memset(conn, 0, sizeof(conn));
        memset(add, 0, sizeof(add));
        memset(vis, 0, sizeof(vis));
        for (int i=0; i<n; i++) {
            set(i, i);
        }
        for (int i=0; i<n; i++) {
            if (b[i] > 1) {
                for (int j=i+1; j<n; j++) {
                    if (b[j] == b[i]-1) {
                        add[i][j] = 1; 
                        break;
                    }
                }
            }
            if (a[i] > 1) {
                for (int j=i-1; j>=0; j--) {
                    if (b[j] == b[i]-1) {
                        add[i][j] = 1; 
                        break;
                    }
                }
            }
        }
        for (int i=0; i<n; i++) {
            if (!vis[i]) {
                vis[i] = 1;
                DFS(i);
            }
        }
        cnt = 0;
        memset(ans, 0, sizeof(ans));
        for (int i=0; i<n; i++) {
            if (!ans[i]) {
                Fill(i);
            }
        }
        printf("Case #%d:", casI+1);
        for (int i=0; i<n; i++) {
            printf(" %d", ans[i]);
        }
        puts("");
    }
    return 0;
}
