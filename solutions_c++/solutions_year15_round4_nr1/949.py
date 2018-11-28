#include <bits/stdc++.h>

using namespace std;

map<char, pair<int, int>> mp;
vector<pair<int, int>> move_;

void Solve (int test_num) {
    int n, m;
    scanf("%d%d", &n, &m);
    vector<vector<pair<int, int>>> grid(n);
    for (int i = 0; i < n; ++i) {
        grid[i].resize(m);
        for (int j = 0; j < m; ++j) {
            char c;
            scanf("\n%c", &c);
            grid[i][j] = mp[c];
        }
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == make_pair(0, 0)) continue;
            bool possible = false, to_change = true;
            for (auto p : move_) {
                int x = i + p.first, y = j + p.second;
                bool is_arrow = false;
                while (x < n && y < m && x >= 0 && y >= 0 && !is_arrow) {
                    if (grid[x][y] != make_pair(0, 0)) {
                        is_arrow = true;
                    }
                    x += p.first;
                    y += p.second;
                }
                if (is_arrow) possible = true;
                if (is_arrow && p == grid[i][j]) to_change = false;
            }
            if (!possible) {
                printf("Case #%d: IMPOSSIBLE\n", test_num);
                return;
            }
            if (to_change) ++ans;
        }
    }
    printf("Case #%d: %d\n", test_num, ans);
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    mp['.'] = {0, 0};
    mp['^'] = {-1, 0};
    mp['>'] = {0, 1};
    mp['<'] = {0, -1};
    mp['v'] = {1, 0};
    move_ = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; ++i) {
        Solve(i + 1);
    }
}
