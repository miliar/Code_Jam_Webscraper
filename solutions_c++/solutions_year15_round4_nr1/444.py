#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
using namespace std;

char buf[200][200];
int sum_a[200], sum_b[200];
int n, m;
int was[200][200];
pair<int, int> reswalk[40000];
int reswalk_mx = 0;
bool goodwalk;

char get_direction(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first) {
        if (a.second < b.second) {
            return '>';
        } else {
            return '<';
        }
    } else {
        if (a.first < b.first) {
            return 'v';
        } else {
            return '^';
        }
    }
}

void walk(int x, int y) {
    if (was[x][y]) {
        goodwalk = true;
        return;
    }
    was[x][y] = 1;
    reswalk[reswalk_mx++] = make_pair(x, y);
    if (buf[x][y] == '^') {
        x--;
        while (x >= 0 && buf[x][y] == '.') x--;
        if (x == -1) {
            return;
        }
        walk(x, y);
    } else if (buf[x][y] == 'v') {
        x++;
        while (x < n && buf[x][y] == '.') x++;
        if (x == n) {
            return;
        }
        walk(x, y);
    } else if (buf[x][y] == '<') {
        y--;
        while (y >= 0 && buf[x][y] == '.') y--;
        if (y == -1) {
            return;
        }
        walk(x, y);
    } else if (buf[x][y] == '>') {
        y++;
        while (y < m && buf[x][y] == '.') y++;
        if (y == m) {
            return;
        }
        walk(x, y);
    }
}

void solve() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> buf[i];
    }
    memset(sum_a, 0, sizeof(sum_a));
    memset(sum_b, 0, sizeof(sum_b));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            was[i][j] = 0;
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (buf[i][j] != '.') {
                sum_a[i]++;
                sum_b[j]++;
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (buf[i][j] != '.' && sum_a[i] == 1 && sum_b[j] == 1) {
                cout << "IMPOSSIBLE";
                return;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (buf[i][j] != '.' && was[i][j] == 0) {
                reswalk_mx = 0;
                goodwalk = false;
                walk(i, j);
                if (goodwalk) {
                    continue;
                }
                if (reswalk_mx != 1) {
                    pair<int, int> last = reswalk[reswalk_mx - 1];
                    pair<int, int> prelast = reswalk[reswalk_mx - 2];
                    buf[last.first][last.second] = get_direction(last, prelast);
                    ans++;
                } else {
                    ans++;
                    for (int k = 0; k < n; ++k) {
                        if (k != i && buf[k][j] != '.') {
                            buf[i][j] = get_direction(make_pair(i, j), make_pair(k, j));
                        }
                    }
                    for (int k = 0; k < m; ++k) {
                        if (k != j && buf[i][k] != '.') {
                            buf[i][j] = get_direction(make_pair(i, j), make_pair(i, k));
                        }
                    }
                }
            }
        }
    }
    cout << ans;
}

int main() {
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}
