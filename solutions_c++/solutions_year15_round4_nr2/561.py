#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const int N = 110;

double r[N], c[N];

bool equal(double x, double y) {
    return fabs(x - y) <= 1e-8;
}

bool less_than(double x, double y) {
    return x < y && !equal(x, y);
}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
//    ios::sync_with_stdio(false);
//    cin.tie(nullptr);
    int tn;
    cin >> tn;
    for (int ti = 1; ti <= tn; ++ti) {
        int n;
        double v, x;
        cin >> n >> v >> x;
        for (int i = 0; i < n; ++i) {
            cin >> r[i] >> c[i];
        }
        bool possible = false;
        double answer = 1e9;
        for (int i = 0; i < n; ++i) {
            if (equal(c[i], x)) {
                answer = min(answer, v / r[i]);
                possible = true;
            }
        }
        if (n == 2 && equal(c[0], x) && equal(c[1], x)) {
            answer = min(answer, v / (r[0] + r[1]));
            possible = true;
        }
        if (n == 2) {
            if (c[0] > c[1]) {
                swap(c[0], c[1]);
                swap(r[0], r[1]);
            }
            if (less_than(c[0], x) && less_than(x, c[1])) {
                double v1 = v * (x - c[0]) / (c[1] - c[0]);
                double v0 = v - v1;
                answer = min(answer, max(v0 / r[0], v1 / r[1]));
                possible = true;
            }
        }
        cout << "Case #" << ti << ": ";
        if (possible) {
            cout << fixed << setprecision(10) << answer << '\n';
        } else {
            cout << "IMPOSSIBLE" << '\n';
        }
    }    
}

