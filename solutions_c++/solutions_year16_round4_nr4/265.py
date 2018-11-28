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

bool used[10];
int n, mask;
int perm[10];

bool rec(int w) {
    if (w == n) {
        return true;
    }
    int worker  = perm[w];
    int cnt = 0;
    for (int machine = 0; machine < n; machine++) {
        if (!(mask & (1 << (worker * n + machine))) || used[machine]) {
            continue;
        }
        used[machine] = true;
        if (!rec(w + 1)) {
            return false;
        }
        used[machine] = false;
        cnt++;
    }
    return (cnt > 0);
}

bool good() {
    for (int i = 0; i < n; i++) {
        perm[i] = i;
    }
    do {
        memset(used, false, sizeof(used));
        if (!rec(0)) {
            return false;
        }
    } while (next_permutation(perm, perm + n));
    return true;
}

void solve(int test_number) {
    cin >> n;
    string s;
    for (int i = 0; i < n; i++) {
        string tmp;
        cin >> tmp;
        s += tmp;
    }
    int m1 = 0;
    for (int i = 0; i < n * n; i++) {
        if (s[i] == '1') {
            m1 |= (1 << i);
        }
    }
    int ans = 10000;
    for (mask = 0; mask < (1 << (n * n)); mask++) {
        if (m1 & (~mask)) {
            continue;
        }
        if (good()) {
            ans = min(ans, __builtin_popcount(m1 ^ mask));
        }
    }
    cout << "Case #" << test_number + 1 << ": ";
    cout << ans << endl;
}
