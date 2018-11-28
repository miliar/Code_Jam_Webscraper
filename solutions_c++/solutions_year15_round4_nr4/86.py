#include <cstdio>
#include <set>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;

set< vector<int> > st;

void read() {
    scanf("%d%d", &n, &m);
}

int a[128][128];
int ans;

int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};

int check(int x, int y) {
    int q, w;

    if (a[x][y] == -1) return 1;

    int maybe = 0, ok = 0;

    for (int i = 0; i < 4; i++) {
        q = x + dx[i];
        w = (y + dy[i] + m) % m;

        if (q >= 0 && q < n) {
            if (a[q][w] == -1) maybe ++;
            if (a[q][w] == a[x][y]) ok ++;
        }
    }

    if (ok <= a[x][y] && a[x][y] <= ok + maybe) return 1;
    return 0;
}

void rec(int x, int y) {
    if (x == n) {
        rec(0, y + 1);
        return ;
    }
    if (y == m) {
        for (int i = 0; i < n; i++) {
            if (!check(i, 0) || !check(i, m - 1)) {
                return ;
            }
        }

        // all good
        for (int j = 0; j < m; j++) {
            vector<int> sol;

            for (int k = 0; k < m; k++) {
                for (int i = 0; i < n; i++) {
                    sol.push_back(a[i][(j + k) % m]);
                }
            }

            if (j == 0 && st.count(sol)) return ;
            st.insert(sol);
        }

        ++ ans;

        return ;
    }

    for (int i = 1; i <= 3; i++) {
        a[x][y] = i;

        if (y >= 2 && !check(x, y - 1)) {
            continue;
        }

        rec(x + 1, y);
    }
}

void solve() {
    st.clear();
    ans = 0;
    memset(a, -1, sizeof a);
    rec(0, 0);

    printf ("%d\n", ans);
}

int main() {
    int cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
