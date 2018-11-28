#include <iostream>
#include <stdio.h>
#include <set>

using namespace std;

char result[8];

char best(char a, char b) {
    if (a == 'R') {
        if (b == 'P')
            return 'P';
        else
            return 'R';
    }
    if (a == 'P') {
        if (b == 'S')
            return 'S';
        else
            return 'P';
    }
    if (a == 'S') {
        if (b == 'R')
            return 'R';
        else
            return 'S';
    }
}

bool valid(int n) {
    char test[8];
    int cnt = (1 << n);
    for (int i = 0; i < cnt; ++i)
        test[i] = result[i];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; 2 * j < cnt; ++j) {
            if (test[2 * j] == test[2 * j + 1])
                return false;
            test[j] = best(test[2 * j], test[2 * j + 1]);
        }
        cnt >>= 1;
    }
    return true;
}

bool gen(int v, int n, int r, int p, int s) {
    if (v == (1 << n) && valid(n)) {
        result[v] = '\0';
        cout << result << endl;
        return true;
    }
    if (p > 0) {
        result[v] = 'P';
        if (gen(v + 1, n, r, p - 1, s)) {
            return true;
        }
    }
    if (r > 0) {
        result[v] = 'R';
        if (gen(v + 1, n, r - 1, p, s)) {
            return true;
        }
    }
    if (s > 0) {
        result[v] = 'S';
        if (gen(v + 1, n, r, p, s - 1)) {
            return true;
        }
    }
    return false;
}

void solve() {
    int n, p, r, s;
    cin >> n >> r >> p >> s;
    if (!gen(0, n, r, p, s)) {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int f = 1; f <= t; ++f) {
        cout << "CASE #" << f << ": ";
        solve();
    }
}
