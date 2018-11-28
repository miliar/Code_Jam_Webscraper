#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define TASKNAME ""

void solve(int test_number);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(3);
#ifdef LOCAL
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#else
#endif
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i);
    }
}

const int MAX_N = 20005;

void solve(int test_number) {
    string s;
    cin >> s;
    int c1 = count(s.begin(), s.end(), 'C');
    int c2 = s.size() - c1;
    int ans = 0;
    while (s.size() > 1) {
        int ind = -1;
        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] == s[i + 1]) {
                ind = i;
                break;
            }
        }
        if (ind < 0) {
            break;
        }
        s.erase(s.begin() + ind);
        s.erase(s.begin() + ind);
        ans += 10;
    }
    ans += 5 * (s.size() / 2);
    cout << "Case #" << test_number + 1 << ": " << ans << endl;
}
