#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

static int max_;
static int maxc_;

void slv(vector<string> &s, int m, int n, vector<int> &a) {
    vector<unordered_set<string>> t(n);
    for (int i = 0; i < m; ++i) {
        t[a[i]].insert("");
        for (int j = 0; j < s[i].length(); ++j) {
            t[a[i]].insert(s[i].substr(0, j + 1));
        }
    }
    int cur = 0;
    for (int i = 0; i < n; ++i) {
        cur += t[i].size();
    }
    if (cur > max_) {
        max_ = cur;
        maxc_ = 1;
    } else if (cur == max_) {
        ++maxc_;
    }
}

void bf(vector<string> &s, int m, int n, int i, vector<int> &a) {
    if (i == m) {
        slv(s, m, n, a);
    } else {
        for (int j = 0; j < n; ++j) {
            a[i] = j;
            bf(s, m, n, i + 1, a);
        }
    }
}

void solve(unsigned t) {
    cerr << "Test #" << t <<  endl;
    cout << "Case #" << t << ": ";

    int m, n;
    cin >> m >> n;
    vector<string> s(m);
    for (int i = 0; i < m; ++i) {
        cin >> s[i];
    }
    vector<int> a(m);
    max_ = 0;
    maxc_ = 0;
    bf(s, m, n, 0, a);
    cout << max_ << " " << maxc_;

    cout << endl;
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    unsigned t;
    cin >> t;
    for (unsigned i = 0; i < t; ++i) {
        solve(i + 1);
    }
    return 0;
}
