#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int N;
string S;
int M[10][10];
int r[10];
int c[10], q[1010];
int ans;
bool vis[1010];

bool check() {
    if (N == 1) {
        if (M[0][0] == 1) {
            return true;
        } else {
            return false;
        }
    }
    int hd = 0, tl = 1;
    memset(vis, 0, sizeof vis);
    for (int i = 0; i < N; ++i) if (!vis[i]) {
        hd = 0, tl = 1;
        vis[q[1] = i] = true;
        int cnt_edge = 0, cl = 0, cr = 0;
        while (hd < tl){
            int x = q[++hd];
            if (x < N) {
                ++cl;
                for (int y = 0; y < N; ++y) if (M[x][y] == 1){
                    cnt_edge++;
                    if (!vis[y + N]){
                        vis[q[++tl] = y + N] = true;
                    }
                }
            } else {
                ++cr;
                for (int y = 0; y < N; ++y) if (M[y][x - N] == 1){
                    if (!vis[y]){
                        vis[q[++tl] = y] = true;
                    }
                }
            }
        }
        if (cnt_edge != cl * cr || cl != cr) return false ;
    }
    return true;
}

void dfs(int num, int cost) {
    if (num == N * N) {
        if (check()) {
            if (cost < ans) {
                ans = cost;
            }
        }
        return ;
    }

    int x = num / N;
    int y = num % N;

    if (M[x][y] == 0) {
        M[x][y] = 1;
        dfs(num + 1, cost + 1);
        M[x][y] = 0;
    }

    dfs(num + 1, cost);
}

int main()
{
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);

    int T;
    cin >> T;
    for (int Cas = 1; Cas <= T; ++Cas) {
        cin >> N;
        for (int i = 0; i < N; ++i) {
            cin >> S;
            for (int j = 0; j < N; ++j) {
                M[i][j] = (int)S[j] - (int)('0');
            }
        }

        ans = 10101;
        dfs(0, 0);

        printf("Case #%d: %d\n", Cas, ans);
    }
    return 0;
}
