#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

const int max_n = 1, inf = 1111111111;

long long t, k, c, s;

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        cin >> k >> c >> s;
        cout << "Case #" << test << ": ";
        if (c == 1) {
            if (s < k) {
                cout << "IMPOSSIBLE" << endl;
            } else {
                for (int i = 1; i <= k; ++i) {
                    cout << i << " ";
                }
                cout << endl;
            }
        } else if (2 * s < k) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            long long x = 1;
            for (int i = 1; i < c; ++i) {
                x *= k;
            }
            long long q = x / k;
            long long y = x;
            for (int i = 0; i < s; ++i) {
                cout << y << " ";
                y += x - q;
            }
            cout << endl;
        }
    }
    return 0;
}
