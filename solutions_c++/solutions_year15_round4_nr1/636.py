#include <bits/stdc++.h>
using namespace std;

void runTest(int test) {
    int m; cin >> m;
    int n; cin >> n;
    vector<string> s (m);
    int result = 0;
    for (int i = 0; i < m; ++i) cin >> s[i];
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) if (s[i][j] != '.') {
            bool hasUp = false;
            for (int ii = i - 1; ii >= 0; --ii) hasUp |= s[ii][j] != '.';
            bool hasDown = false;
            for (int ii = i + 1; ii < m; ++ii) hasDown |= s[ii][j] != '.';
            bool hasLeft = false;
            for (int jj = j - 1; jj >= 0; --jj) hasLeft |= s[i][jj] != '.';
            bool hasRight = false;
            for (int jj = j + 1; jj < n; ++jj) hasRight |= s[i][jj] != '.';
            if (!(hasUp || hasDown || hasLeft || hasRight)) {
                cout << "Case #" << test + 1 << ": " << "IMPOSSIBLE" << '\n';
                return;
            }
            if (s[i][j] == '<' && !hasLeft) ++result;
            else if (s[i][j] == '>' && !hasRight) ++result;
            else if (s[i][j] == '^' && !hasUp) ++result;
            else if (s[i][j] == 'v' && !hasDown) ++result;
        }
    }
    cout << "Case #" << test + 1 << ": " << result << '\n';
}

int main() {
    assert(freopen("A-large.in", "r", stdin));
    assert(freopen("A-large.out", "w", stdout));
    ios::sync_with_stdio(false);
    int numTests; cin >> numTests;
    for (int test = 0; test < numTests; ++test) {
        runTest(test);
    }
    return 0;
}
