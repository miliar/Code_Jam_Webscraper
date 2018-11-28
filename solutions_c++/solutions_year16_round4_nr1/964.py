#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

const int N = (int)1e5 + 4;
const int inf = (int)1e9 + 7;

string answer;

void change(const string &s, int l, int r) {
    if (l == r) {
        answer += s[l];
        return;
    }
    int m = (l + r) / 2;
    string a, b;
    for (int j = l; j <= m; ++j) {
        a += s[j];
    }
    for (int j = m + 1; j <= r; ++j) {
        b += s[j];
    }
    if (a < b) {
        change(s, l, m);
        change(s, m + 1, r);
    } else {
        change(s, m + 1, r);
        change(s, l, m);
    }
}

void solve(int T) {
    int n, X[3];
    cin >> n >> X[0] >> X[2] >> X[1];
    char A[3] = {'R', 'S', 'P'};
    map<char, int> w;
    answer = "";
    w['R'] = 0, w['S'] = 1, w['P'] = 2;
    cout << "Case #" << T << ": ";
    for (int i = 0; i < 3; ++i) {
        string s;
        s += A[i];
        for (int j = 1; j <= n; ++j) {
            string p;
            for (int t = 0; t < (int)s.size(); ++t) {
                char a = s[t], b = A[(w[s[t]] + 1) % 3];
                if (a < b) {
                    p += a, p += b;
                } else {
                    p += b, p += a;
                }
            }
            s = p;
        }
        int D[3] = {0, 0, 0};
        for (int j = 0; j < (1 << n); ++j) {
            ++D[w[s[j]]];
        }
        bool f = true;  
        for (int j = 0; j < 3; ++j) {
            if (D[j] != X[j]) {
                f = false;
            }
        }
        if (f) {
            change(s, 0, (1 << n) - 1);
            cout << answer << endl;
            return;
        }
    }
    cout << "IMPOSSIBLE" << endl;
}


int main() {
    freopen("A-small-attempt4.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        solve(t);
    }
    return 0;
}