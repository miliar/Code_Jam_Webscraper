#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;
/*
vector<vector<int>> iv(int n) {
    vector<vector<int>> ans;
    vector<int> tmp, cur;
    for (int i = 0; i < n; ++i) {
        tmp.push_back(i);
        cur.push_back(i);
    }
    ans.push_back(tmp);
    next_permutation(cur.begin(), cur.end());
    while (cur != tmp) {
        ans.push_back(cur);
        next_permutation(cur.begin(), cur.end());
    }
    return move(ans);
}*/

void solve(unsigned t) {
    cout << "Case #" << t << ": ";

    int x, n;
    cin >> n >> x;
    vector<int> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }
    sort(s.begin(), s.end());

    vector<bool> used(n);
    for (int i = 0; i < n; ++i) {
        used[i] = false;
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (!used[i]) {
            used[i] = true;
            ++ans;
            for (int j = n - 1; j >= 0; --j) {
                if (used[j]) {
                    continue;
                }
                if (s[j] + s[i] > x) {
                    continue;
                }
                used[j] = true;
                break;
            }
        }
    }

    cout << ans;
/*
    ans = n;
    vector<vector<int>> p = iv(n);
    for (int i = 0; i < p.size(); ++i) {
        vector<int> &cur = p[i];
        int cc = 0;
        int cnt = 0;
        int cw = 0;
        for (int j = 0; j < cur.size(); ++j) {
            int w = s[cur[j]];
            if (cnt == 0) {
                ++cnt;
                ++cc;
                cw = w;
            } else if (cnt == 2) {
                ++cc;
                cnt = 1;
                cw = w;
            } else {
                if (w + cw <= x) {
                    ++cnt;
                    cw += w;
                } else {
                    cnt = 1;
                    cw = w;
                    ++cc;
                }
            }
        }
        if (cc < ans) {
            ans = cc;
        }
    }

    cout << " " << ans;*/

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
