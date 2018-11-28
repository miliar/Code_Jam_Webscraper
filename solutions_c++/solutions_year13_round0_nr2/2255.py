#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <string>

using namespace std;

#include <queue>
typedef pair<int, int> PII;
#define mp make_pair
const int maxn = 128;
int g[maxn][maxn], n, m;

bool check1(int x, int y) {
    for (int ty = 0; ty < m; ++ty) {
        if (g[x][ty] > g[x][y]) return false;
    }
    for (int ty = 0; ty < m; ++ty) {
        g[x][ty] = -1;
    }
    return true;
}

bool check2(int x, int y) {
    for (int tx = 0; tx < n; ++tx) {
        if (g[tx][y] > g[x][y]) return false;
    }
    for (int tx = 0; tx < n; ++tx) {
        g[tx][y] = -1;
    }
    return true;
}

void solved(int nT) {
    scanf("%d %d", &n, &m);
    priority_queue<PII, vector<PII>, greater<PII> > q;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            scanf("%d", &g[i][j]);
            q.push(mp(g[i][j], i * m + j));
        }
    }
    printf("Case #%d: ", nT);
    bool flag = true;
    while (!q.empty() && flag) {
        PII tmp = q.top(); q.pop();
        if (g[tmp.second / m][tmp.second % m] == -1) continue;
        int cnt = 0;
        if (check1(tmp.second / m, tmp.second % m)) ++cnt;
        if (check2(tmp.second / m, tmp.second % m)) ++cnt;
        if (cnt == 0) flag = false;
    }
    puts(flag ? "YES" : "NO");
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T = 1;
    scanf("%d", &T);
    for (int nT = 1; nT <= T; ++nT) {
        solved(nT);
    }
    return 0;
}