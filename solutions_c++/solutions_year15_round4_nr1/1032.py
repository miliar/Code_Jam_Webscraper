#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;

int r, c;
vector<string> rows;
vector<vector<char>> states;
vector<vector<pair<int, int>>> pre;

const char GOOD = 1;
const char LEADS_TO_BAD = 2;
const char BAD = 3;

const int dirs[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

pair<int, int> get_dir(char c) {
    switch (c) {
    case '^': return make_pair(-1, 0);
    case '>': return make_pair(0, 1);
    case '<': return make_pair(0, -1);
    case 'v': return make_pair(1, 0);
    default: throw exception();
    }
}

void dfs(int row, int col) {
    set<pair<int, int>> was;
    was.insert(make_pair(row, col));

    pair<int, int> last(row, col);
    pair<int, int> dir = get_dir(rows[row][col]);
    while (true) {
        row += dir.first, col += dir.second;
        if (row < 0 || row >= r || col < 0 || col >= c) {
            for (auto& entry : was)
                states[entry.first][entry.second] = LEADS_TO_BAD;
            states[last.first][last.second] = BAD;
            return;
        }
        if (rows[row][col] == '.')
            continue;
        pre[row][col] = last;
        if (states[row][col] == BAD || states[row][col] == LEADS_TO_BAD) {
            for (auto& entry : was)
                states[entry.first][entry.second] = LEADS_TO_BAD;
            return;
        }
        if (was.count(make_pair(row, col)) || states[row][col] == GOOD) {
            for (auto& entry : was)
                states[entry.first][entry.second] = GOOD;
            return;
        }
        last = make_pair(row, col);
        was.insert(last);
        dir = get_dir(rows[row][col]);
    }
}

void rewind(int row, int col/*, queue<pair<int, int>>& q*/) {
    // q.push(make_pair(row, col));
    states[row][col] = GOOD;
    while (true) {
        pair<int, int> pr = pre[row][col];
        if (pr.first == -1)
            break;
        row = pr.first, col = pr.second;

        if (rows[row][col] == '.' || states[row][col] != LEADS_TO_BAD)
            throw exception();
        states[row][col] = GOOD;
        //q.push(make_pair(row, col));
    }
}

void solve() {
    cin >> r >> c;
    rows.resize(r);
    for (int i = 0; i < r; ++i)
        cin >> rows[i];
    states.assign(r, vector<char>(c));
    pre.assign(r, vector<pair<int, int>>(c, make_pair(-1, -1)));

    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            if (rows[i][j] != '.' && states[i][j] == 0)
                dfs(i, j);

    int ans = 0;
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            if (states[i][j] == BAD) {
                if (pre[i][j].first != -1) {
                    rewind(i, j);
                }
                ++ans;
            }

    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            if (states[i][j] == BAD) {
                bool good = false;
                for (int d = 0; !good && d < 4; ++d) {
                    int x = i, y = j;
                    while (true) {
                        x += dirs[d][0], y += dirs[d][1];
                        if (x < 0 || y < 0 || x >= r || y >= c)
                            break;
                        if (rows[x][y] != '.') {
                            good = true;
                            break;
                        }
                    }
                }
                if (!good) {
                    cout << "IMPOSSIBLE" << endl;
                    return;
                }
            }

    cout << ans << endl;
}

int main() {
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; ++t) {
        cerr << "test: " << t << endl;
        cout << "Case #" << t << ": ";
        solve();
    }

    return 0;
}

