#include <bits/stdc++.h>
using namespace std;



typedef double DB;
typedef long long LL;

const int N = 1e5 + 7;

vector<int> e[105];
int v[105], npt, R, C;
int x[105], y[105];
void addedge(int x, int y) {
    e[x].push_back(y);
    e[y].push_back(x);
}

void dfs(int x, int len) {
    v[x] = 1;
    for (int i = 0; i < e[x].size(); i++) {
        int y = e[x][i];
        if (v[y]) continue;
        dfs(y, len + 1);
    }
}

bool check(int x, int y) {
    x += npt, y += npt;
    memset(v, 0, sizeof(v));
    dfs(x, 0);
    return v[y];
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int CAS;
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%d%d", &R, &C);
        int n = R + C;
        npt = R * C * 4;
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &x[i], &y[i]);
            x[i]--, y[i]--;
        }
        printf("Case #%d:\n", cas);
        for (int i = 0; i < (1 << R * C); i++) {
            for (int j = 0; j < npt + n + n; j++)
                e[j].clear();
            for (int j = 0; j < C; j++) {
                addedge(npt + j, j * 4);
            }
            for (int j = 0; j < R; j++) {
                addedge(npt + C + j, j * 4 * C + (C - 1) * 4 + 1);
            }
            for (int j = 0; j < C; j++) {
                addedge(npt + C + R + j, (R - 1) * C * 4 + (C - 1 - j) * 4 + 2);
            }
            for (int j = 0; j < R; j++) {
                addedge(npt + C + R + C + j, (R - 1 - j) * C * 4 + 3);
            }
            for (int j = 0; j < R * C; j++) {
                int r = j / C, c = j % C;
                if (r) addedge(r * C * 4 + c * 4, (r - 1) * C * 4 + c * 4 + 2);
                if (c) addedge(r * C * 4 + c * 4 + 3, r * C * 4 + c * 4 - 4 + 1);
                if (i >> j & 1) {
                    addedge(r * C * 4 + c * 4, r * C * 4 + c * 4 + 1);
                    addedge(r * C * 4 + c * 4 + 2, r * C * 4 + c * 4 + 3);
                } else{
                    addedge(r * C * 4 + c * 4, r * C * 4 + c * 4 + 3);
                    addedge(r * C * 4 + c * 4 + 1, r * C * 4 + c * 4 + 2);
                }
            }
            int flag = 0;
            for (int j = 0; j < n; j++)
            if (!check(x[j], y[j])) flag = 1;

            if (!flag) {
                for (int j = 0; j < R * C; j++) {
                    if (i >> j & 1) printf("\\"); else printf("/");
                    if (j % C == C - 1) puts("");
                }
                break;
            } else if (i == (1 << R * C) - 1) puts("IMPOSSIBLE");
        }

    }
}
