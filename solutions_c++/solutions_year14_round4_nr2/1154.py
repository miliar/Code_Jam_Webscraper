#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

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
}

void print(vector<int> &v) {
    for (int i = 0; i < v.size(); ++i) {
        cerr << v[i] << " " ;
    }
    cerr << endl;
}

bool test(vector<int> &a, int n) {
    int max_ = a[0];
    int ind = 0;
    for (int i = 0; i < n; ++i) {
        if (a[i] > max_) {
            max_ = a[i];
            ind = i;
        }
    }
    for (int i = 0; i < ind; ++i) {
        if (a[i] > a[i + 1]) {
            return false;
        }
    }
    for (int i = ind + 1; i < n; ++i) {
        if (a[i - 1] < a[i]) {
            return false;
        }
    }
    return true;
}

int swp(vector<int> &a, int n) {
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (a[i] < a[j]) {
                ++ans;
                swap(a[i], a[j]);
            }
        }
    }
    return ans;
}

void solve(unsigned t) {
    cerr << "Test #" << t <<  endl;
    cout << "Case #" << t << ": ";

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    vector<vector<int>> p = iv(n);
    int max_ = 1111111111;
    for (int _ = 0; _ < p.size(); ++_) {
        vector<int> &cur = p[_];
        vector<int> b;
        for (int i = 0; i < n; ++i) {
            b.push_back(a[cur[i]]);
        }
        if (!test(b, n)) {
            continue;
        }
        int cur_ = swp(cur, n);
        if (cur_ < max_) {
            max_ = cur_;
        }
    }
    cout << max_;

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
