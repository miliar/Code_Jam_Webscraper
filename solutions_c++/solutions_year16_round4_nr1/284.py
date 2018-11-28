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

string winning_string[15][3];

void precalc() {
    winning_string[0][0] = 'P';
    winning_string[0][1] = 'R';
    winning_string[0][2] = 'S';
    int child[3][2] = {{0, 1}, {1, 2}, {2, 0}};
    for (int i = 1; i < 15; i++) {
        for (int j = 0; j < 3; j++) {
            winning_string[i][j] = min(winning_string[i - 1][child[j][0]] + winning_string[i - 1][child[j][1]], winning_string[i - 1][child[j][1]] + winning_string[i - 1][child[j][0]]);
        }
    }
}

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
    precalc();
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i);
    }
}


void solve(int test_number) {
    int n, p, r, s;
    cin >> n >> r >> p >> s;
    string ans = "Z";
    for (int winner = 0; winner < 3; winner++) {
        string cur = winning_string[n][winner];
        int P = count(cur.begin(), cur.end(), 'P');
        int R = count(cur.begin(), cur.end(), 'R');
        int S = count(cur.begin(), cur.end(), 'S');
        if (p != P || r != R || s != S) {
            continue;
        }
        ans = min(ans, cur);
    }
    cout << "Case #" << test_number + 1 << ": ";
    if (ans == "Z") {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << ans << endl;
    }
}
