#include <iostream>
#include <vector>

using namespace std;

int dr[9] = {0, 0, 0, -1, -1, -1, 1, 1, 1};
int dc[9] = {0, -1, 1, 0, -1, 1, 0, -1, 1};

vector<vector<bool> > toGrid(const int R, const int C, const int b) {
    vector<vector<bool> > grid(R, vector<bool>(C, false));
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            const int index = C * i + j;
            if ((1<<index) & b) grid[i][j] = true;
        }
    }
    return grid;
}

void dfs(const vector<vector<bool> > &neigh, vector<vector<bool> > &vis, vector<vector<bool> > &lvis, int r, int c) {
    vis[r][c] = true;
    for (int d = 0; d < 9; ++d) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr >= 0 && nr < vis.size() && nc >= 0 && nc < vis[0].size()) {
            lvis[nr][nc] = true;
            if (!vis[nr][nc] && !neigh[nr][nc])
                dfs(neigh, vis, lvis, nr, nc);
        }
    }
}

bool valid(vector<vector<bool> > grid) {
    vector<vector<bool> > vis(grid.size(), vector<bool>(grid[0].size(), false));
    vector<vector<bool> > lvis(grid.size(), vector<bool>(grid[0].size(), false));
    vector<vector<bool> > neigh(grid.size(), vector<bool>(grid[0].size(), false));
    for (int i = 0; i < grid.size(); ++i) {
        for (int j = 0; j < grid[0].size(); ++j) {
            if (grid[i][j]) {
                for (int d = 0; d < 9; ++d) {
                    int nr = i + dr[d];
                    int nc = j + dc[d];
                    if (nr >= 0 && nr < grid.size() && nc >= 0 && nc < grid[0].size()) {
                        neigh[nr][nc] = true;
                    }
                }
            }
        }
    }
    int nc = 0;
    for (int i = 0; i < neigh.size(); ++i) {
        for (int j = 0; j < neigh[0].size(); ++j) {
            if (neigh[i][j] == 0) {
                if (!vis[i][j]) {
                    ++nc;
                    dfs(neigh, vis, lvis, i, j);
                }
            }
        }
    }
    bool ok = true;
    int cnt = 0;
    for (int i = 0; i < neigh.size(); ++i) {
        for (int j = 0; j < neigh[0].size(); ++j) {
            if (!grid[i][j] && !lvis[i][j]) ok = false;
            if (!grid[i][j]) ++cnt;
        }
    }

    // bloody edge case :<
    if (cnt == 1) {
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (!grid[i][j]) {
                    cout << 'c';
                } else {
                    cout << (grid[i][j] ? '*' : '.');
                }
            }
            cout << endl;
        }
        return true;
    }

    if (nc == 1 && ok) {
        bool first = false;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (!first && !neigh[i][j]) {
                    cout << 'c';
                    first = true;
                } else {
                    cout << (grid[i][j] ? '*' : '.');
                }
            }
            cout << endl;
        }
        return true;
    }
    return false;
}

void solve() {
    int R, C, M;
    cin >> R >> C >> M;

    for (int b = 0; b < (1 << (R*C)); ++b) {
        if (__builtin_popcount(b) != M) continue;
        vector<vector<bool> > grid = toGrid(R, C, b);
        if (valid(grid)) {
            return;
        }
    }
    cout << "Impossible" << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ":" << endl;
        solve();
    }
}
