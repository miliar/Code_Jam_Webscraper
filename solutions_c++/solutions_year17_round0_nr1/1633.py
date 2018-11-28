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
    int n = 1;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        solve(i);
    }
}

const int MAX_N = 100005; // TODO

string s;
int k;
int ans;

void read_input() {
    cin >> s >> k;
}

void init() {
    // memset(a, -1, sizeof(a));
    ans = 0;
}

void output(int test_number) {
    cout << "Case #" << test_number << ": ";
    if (ans < 0) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << ans << endl;
    }
}

void flip(int i) {
    for (int j = i; j < i + k; j++) {
        s[j] = (s[j] == '+')? '-': '+';
    }
}

void solve(int test_number) {
    read_input();
    init();
    for (int i = 0; i + k <= s.size(); i++) {
        if (s[i] == '-') {
            flip(i);
            ans++;
        }
    }
    if  (count(s.begin(), s.end(), '-')) {
        ans = -1;
    }
    output(test_number);
}
