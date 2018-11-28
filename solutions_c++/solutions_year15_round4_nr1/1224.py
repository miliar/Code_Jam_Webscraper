#include <bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define INF (0x3f3f3f3f)

#define SZ(x) ((int)((x).size()))
#define PB(x) push_back(x)
#define MEMSET(x,v) memset(x,v,sizeof(x))
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))

typedef long long LL;
typedef pair<int, int> PII; typedef pair<PII, int> PII2;

#define MAXN (105)

int R, C;
string board[MAXN];

int group[MAXN][MAXN];
bool can_go_off[MAXN*MAXN];
int group_sz[MAXN];
int gg;

int cx[] = {0, 1, 0, -1};
int cy[] = {1, 0, -1, 0};
map<char, int> dir;

void dfs(int ii, int jj) {
    group[ii][jj] = gg;
    group_sz[gg]++;
    int cur_d = dir[board[ii][jj]];
    bool out = false;
    for (int i = 1; ; i++) {
        int iii = ii + cx[cur_d] * i;
        int jjj = jj + cy[cur_d] * i;
        if (iii < 0 || iii >= R || jjj < 0 || jjj >= C) {
            out = true;
            break;
        } else {
            if (board[iii][jjj] != '.') {
                out = false;
                if (group[iii][jjj] == 0) {
                    dfs(iii, jjj);
                }
                break;
            }
        }
    }
    REP(k, 4) {
        for (int i = 1; ; i++) {
            int iii = ii + cx[k] * i;
            int jjj = jj + cy[k] * i;
            if (iii < 0 || iii >= R || jjj < 0 || jjj >= C) {
                break;
            } else {
                if (board[iii][jjj] != '.') {
                    int dd = dir[board[iii][jjj]];
                    if ((dd + 2) % 4 == k) {
                        if (group[iii][jjj] == 0) {
                            dfs(iii, jjj);
                        }
                    }
                    break;
                }
            }
        }
    }
    can_go_off[gg] |= out;
}

bool mark[MAXN*MAXN];

void solve() {
    cin >> R >> C;
    REP(i, R) cin >> board[i];
    MEMSET(group, 0);
    MEMSET(can_go_off, 0);
    MEMSET(group_sz, 0);
    gg = 0;
    int ans = 0;
    REP(i, R) {
        REP(j, C) {
            if (board[i][j] != '.' && group[i][j] == 0) {
                gg++;
                dfs(i, j);
            }
        }
    }
    MEMSET(mark, 0);

    REP(i, R) {
        REP(j, C) {
            int g = group[i][j];
            if (g && !mark[g]) {
                mark[g] = true;
                if (!can_go_off[g]) continue;
                if (group_sz[g] == 1) {
                    bool good = false;
                    REP(cur_d, 4) {
                        for (int k = 1; ; k++) {
                            int iii = i + cx[cur_d] * k;
                            int jjj = j + cy[cur_d] * k;
                            if (iii < 0 || iii >= R || jjj < 0 || jjj >= C) {
                                break;
                            } else {
                                if (board[iii][jjj] != '.') {
                                    good = true;
                                    break;
                                }
                            }
                        }
                    }
                    if (!good) {
                        printf("IMPOSSIBLE\n");
                        return ;
                    } else {
                        ans++;
                    }
                } else {
                    ans++;
                }
            }
        }
    }
    cout << ans << endl;
}

int main() {
    dir['>'] = 0;
    dir['v'] = 1;
    dir['<'] = 2;
    dir['^'] = 3;
    int T;
    cin >> T;
    REP(t, T) {
        printf("Case #%d: ", t + 1);
        solve();
    }

    return 0;
}
