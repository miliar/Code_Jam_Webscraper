#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int maxn = 1024;

string s[maxn];
vector<int> sets[maxn];
int lcp[maxn][maxn];
int ans, cnt;

void dfs(int d, int m, int nodes) {
    if (d == -1) {
        bool flag = true;
        for (int i = 0; i < m; ++i) {
            if (sets[i].size() == 0) {
                flag = false;
                break;
            }
        }
        if (flag) {
            if (nodes > ans) {
                ans = nodes;
                cnt = 1;
            } else if (nodes == ans) {
                cnt++;
            }
        }
        return;
    }
    for (int i = 0; i < m; ++i) {
        sets[i].push_back(d);
        int _nodes = nodes + s[d].size();
        if (sets[i].size() > 1) {
            _nodes -= lcp[sets[i][sets[i].size() - 2]][d];
        }
        dfs(d - 1, m, _nodes);
        sets[i].pop_back();
    }
}

void solve() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }
    sort(s, s + n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int &res = lcp[i][j];
            for (res = 0; res < s[i].size() && res < s[j].size(); res++) {
                if (s[i][res] != s[j][res]) {
                    break;
                }
            }
        }
    }
    ans = 0;
    cnt = 0;
    dfs(n - 1, m, 0);
    cout << ans + m << ' ' << cnt << endl;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int caseId = 1; caseId <= T; ++caseId) {
        printf("Case #%d: ", caseId);
        solve();
    }
}
