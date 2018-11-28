#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;


int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    int T;
    cin >> T;    
    for (int test = 1; test <= T; ++test) {        
        int n, m;
        cin >> n >> m;
        int cnt = 2 * (n + m);

        vector<int> a(cnt);
        for (int i = 0; i < cnt; ++i) {
            cin >> a[i];
        }
        vector< vector<char> > ans(n, vector<char>(m));
       
        bool fail = false;
        for (int msk = 0; msk < (1 << (n * m)); ++msk) {
            const int UP = 0;
            const int DOWN = 1;
            const int LEFT = 2;
            const int RIGHT = 3;
            const int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};
            vector< vector< vector<int> > > vid(n, vector<vector<int>>(m, vector<int>(4, 0)));
            int vc = 0;
            vector<int> px;
            vector<int> py;

            int cmsk = msk;
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < m; ++j) {
                    int type = cmsk & 1;
                    cmsk >>= 1;
                    if (type == 0) {
                        ans[i][j] = '/';
                        vid[i][j][UP] = vid[i][j][LEFT] = vc++;
                        px.push_back(i);
                        py.push_back(j);

                        vid[i][j][DOWN] = vid[i][j][RIGHT] = vc++;
                        px.push_back(i);
                        py.push_back(j);
                    } else {
                        ans[i][j] = '\\';
                        vid[i][j][UP] = vid[i][j][RIGHT] = vc++;
                        px.push_back(i);
                        py.push_back(j);
                        vid[i][j][DOWN] = vid[i][j][LEFT] = vc++;
                        px.push_back(i);
                        py.push_back(j);
                    }
                }

            fail = false;
            for (int i = 0; i < cnt; i += 2) {
                int x = a[i];
                int y = a[i + 1];
                int start, finish;

                if (x >= 1 && x <= m) {
                    start = vid[0][x - 1][UP];
                } else
                if (x >= m + 1 && x <= n + m) {
                    start = vid[x - m - 1][m - 1][RIGHT];
                } else
                if (x >= n + m + 1 && x <= n + m + m) {
                    start = vid[n - 1][m - (x - n - m - 1) - 1][DOWN];
                } else {
                    start = vid[n - (x - n - m - m - 1) - 1][0][LEFT];
                }


                if (y >= 1 && y <= m) {
                    finish = vid[0][y - 1][UP];
                } else
                if (y >= m + 1 && y <= n + m) {
                    finish = vid[y - m - 1][m - 1][RIGHT];
                } else
                if (y >= n + m + 1 && y <= n + m + m) {
                    finish = vid[n - 1][m - (y - n - m - 1) - 1][DOWN];
                } else {
                    finish = vid[n - (y - n - m - m - 1) - 1][0][LEFT];
                }

                queue<int> q;
                vector<int> pred(px.size(), -1);
                vector<int> forbid(px.size(), 0);
                q.push(start);

                bool found = false;
                while (!q.empty() && !found) {
                    int v = q.front(); q.pop();

                            if (v == finish) {
                                found = 1;
                                break;
                            }

                    int x = px[v];
                    int y = py[v];
                    for (int d = 0; d < 4; ++d) {
                        if (vid[x][y][d] == v) {
                            int nx = x + dx[d];
                            int ny = y + dy[d];
                            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                                continue;
                            }
                            int to = vid[nx][ny][d ^ 1];
                            if (pred[to] != -1 || forbid[to]) {
                                continue;
                            }

                            pred[to] = v;
                            if (to == finish) {
                                found = 1;
                                break;
                            }
                            q.push(to);
                        }
                    }
                }

                if (!found) {
                    fail = true;
                    break;
                }

                int vv = finish;
                while (vv != start) {
                    forbid[vv] = true;
                    vv = pred[vv];
                }
            }            
            if (!fail) {
                break;
            }
        }
    
        cout << "Case #" << test << ":\n";
        if (!fail) {
            for (int i =0 ; i < n; ++i) {
                for (int j = 0; j < m; ++j)
                    cout << ans[i][j];
                cout << endl;
            }
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }

    return 0;
}
