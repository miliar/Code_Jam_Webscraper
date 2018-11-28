#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <bitset>
#include <queue>
using namespace std;

#define rep(i, s, t) for (int i = (s); i <= (t); ++i)
#define REP(i, n) rep(i, 1, n)

int nxt[5][88][27];
int tot[5];
int N, M;
int anstot, ans;
int bg[11];
char st[11][11];

void solve(int x){
    if (x > M){
        REP(i, N) memset(nxt[i][0], 0, sizeof nxt[i][0]);
        memset(tot, 0, sizeof tot);
        REP(i, M){
            int o = bg[i], x = 0;
            int l = strlen(st[i] + 1);
            REP(j, l){
                int c = st[i][j] - 'A';
                if (nxt[o][x][c] == 0){
                    nxt[o][x][c] = ++tot[o];
                    memset(nxt[o][tot[o]], 0, sizeof nxt[o][tot[o]]);
                }
                x = nxt[o][x][c];
            }
        }
        int res = 0;
        REP(i, N) if (tot[i] == 0) return;
        else res += tot[i] + 1;
        if (res > ans)
            ans = res, anstot = 0;
        if (res == ans) anstot++;
        return;
    }
    for (int i = 1; i <= N; ++i){
        bg[x] = i;
        solve(x + 1);
    }
}

void Fate(int ca){
    anstot = 0;
    ans = 0;
    scanf("%d%d", &M, &N);
    REP(i, M) scanf("%s", st[i] + 1);
    solve(1);
    printf("Case #%d: ", ca);
    printf("%d %d\n", ans, anstot);
}

int main(){
    freopen("D-small.in", "r", stdin);
    freopen("D-small.out", "w", stdout);
    int Ti;
    scanf("%d", &Ti);
    REP(x, Ti){
        Fate(x);
    }
    //system("pause");
}
