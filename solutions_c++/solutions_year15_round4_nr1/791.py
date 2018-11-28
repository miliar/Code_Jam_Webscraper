#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

void precalc() {

}

bool checkLeft(const vector<string>& p, int i, int j) {
    for (--j; j >= 0; --j) {
        if (p[i][j] != '.') return true;
    }
    return false;
}

bool checkRight(const vector<string>& p, int i, int j) {
    for (++j; j < p[i].size(); ++j) {
        if (p[i][j] != '.') return true;
    }
    return false;
}

bool checkUp(const vector<string>& p, int i, int j) {
    for (--i; i >= 0; --i) {
        if (p[i][j] != '.') return true;
    }
    return false;
}

bool checkDown(const vector<string>& p, int i, int j) {
    for (++i; i < p.size(); ++i) {
        if (p[i][j] != '.') return true;
    }
    return false;
}

char getNew(const vector<string>& p, int i, int j) {
    if (p[i][j] == '<' && checkLeft(p, i, j)) {
        return p[i][j];
    }
    if (p[i][j] == '^' && checkUp(p, i, j)) {
        return p[i][j];
    }
    if (p[i][j] == '>' && checkRight(p, i, j)) {
        return p[i][j];
    }
    if (p[i][j] == 'v' && checkDown(p, i, j)) {
        return p[i][j];
    }

    if (checkLeft(p, i, j)) {
        return '<';
    }
    if (checkUp(p, i, j)) {
        return '^';
    }
    if (checkRight(p, i, j)) {
        return '>';
    }
    if (checkDown(p, i, j)) {
        return 'v';
    }
    return '-';
}

void solve() {
    int n, m;
    cin >> n >> m;
    vector<string> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
    }

    int res = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (p[i][j] != '.') {
                char next = getNew(p, i, j);
                if (next == '-') {
                    cout << "IMPOSSIBLE" << endl;
                    return;
                }
                if (next != p[i][j]) {
                    ++res;
                }
            }
        }
    }
    cout << res << endl;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    precalc();

    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        cerr << test << endl;
        solve();
    }
    return 0;
}
