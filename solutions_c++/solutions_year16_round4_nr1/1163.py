#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iomanip>
#include <queue>
#include <utility>
#include <cmath>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, char> pci;

string Solve(int p, int r, int s, char c, int n) {
    if (c == 'S' && s == 0 || c == 'R' && r == 0 || c == 'P' && p == 0) {
        return string(10000, 'Z');
    }
    if (c == 'S') {
        --s;
    } else if (c == 'P') {
        --p;
    } else {
        --r;
    }
    string res;
    res.push_back(c);
    int index = 0;
    while (p || r || s) {
        char ch = res[index++];
        if (ch == 'R') {
            res.push_back('S');
            res.push_back('R');
            --s;
        } else if (ch == 'S') {
            res.push_back('S');
            res.push_back('P');
            --p;
        } else if (ch == 'P') {
            res.push_back('R');
            res.push_back('P');
            --r;
        } else {
            cerr << "!!!\n";
        }
        if (p < 0 || s < 0 || r < 0) {
            return string(10000, 'Z');
        }
    }
    // cerr << "::: = " << res << "\n";
    reverse(res.begin(), res.end());
    return res.substr(0, 1 << n);
}

template <typename T>
void Swap(T first0, T last0, T first1, T last1) {
    while (first0 != last0) {
        swap(*first0, *first1);
        ++first0; ++first1;
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        string res0 = Solve(p, r, s, 'R', n);
        // cerr << "res0: " << res0 << "\n";
        string res1 = Solve(p, r, s, 'P', n);
        // cerr << "res1: " << res1 << "\n";
        string res2 = Solve(p, r, s, 'S', n);
        // cerr << "res2: " << res2 << "\n";
        string res = min(res0, res1);
        res = min(res, res2);
        if (res[0] == 'Z') {
            cout << "Case #" << test_index + 1 << ": IMPOSSIBLE\n";
            continue;
        }
        for (int i = 0; i < n; ++i) {
            int len = 1 << i;
            int cnt = (1 << n) / len;
            for (int j = 0; j < cnt / 2; ++j) {
                if (res.substr(2 * j * len, len) > res.substr((2 * j + 1) * len, len)) {
                    Swap(res.begin() + 2 * j * len, res.begin() + 2 * j * len + len,
                         res.begin() + (2 * j + 1) * len, res.begin() + (2 * j + 1) * len + len);

                }
            }
        }
        cout << "Case #" << test_index + 1 << ": " << res << "\n";
    }
    return 0;
}
