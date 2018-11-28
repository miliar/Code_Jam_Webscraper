#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int bitCount(int n) {
    return __builtin_popcount(n);
}

bool calc(int i, int n, const vector<int>& p, const vector<vector<int> >& a, vector<bool>& used) {
    if (i == n) return true;
    int j = p[i];
    bool f = false;
    for (int k = 0; k < n; ++k) {
        if (used[k]) continue;
        if (a[j][k]) {
            used[k] = true;
            if (!calc(i + 1, n, p, a, used)) return false;
            used[k] = false;
            f = true;
        }
    }
    return f;
}

bool works(int n, const vector<vector<int> >& a) {
    vector<int> p(n);
    for (int i = 0; i < n; ++i) p[i] = i;
    do {
        vector<bool> used(n);
        if (!calc(0, n, p, a, used)) return false;
    } while (next_permutation(p.begin(), p.end()));
    return true;
}

int solve(int n, const vector<vector<int> >& a) {
    int ans = n * n;
    int m = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (a[i][j] == 1) {
                m |= 1 << (i * n + j);
            }
        }
    }
    for (int mask = 0; mask < (1 << n * n); ++mask) {
        if (m & mask) continue;
        vector<vector<int> > b(a);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mask & (1 << (i * n + j))) {
                    b[i][j] = 1;
                }
            }
        }
        if (works(n, b)) ans = min(ans, bitCount(mask));
    }
    return ans;
}

int main() {
    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; ++t) {
        cerr << t << endl;
        int n; cin >> n;
        vector<vector<int> > a(n);
        for (int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            for (int j = 0; j < n; ++j) a[i].push_back(s[j] - '0');
        }
        cout << "Case #" << t << ": " << solve(n, a) << endl;
    }
    return 0;
}
