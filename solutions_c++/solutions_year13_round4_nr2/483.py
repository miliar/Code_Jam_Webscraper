#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;


bool calc1(int64 i, int64 n, int64 p) {
    int64 deg = 2;
    int64 result = 0;
    int64 step = 0;
    while (i >= deg - 1) {
       ++step;
       result += (1LL << (n - step));
       deg *= 2;
    }
    return result <= p - 1;
}

bool calc2(int64 i, int64 n, int64 p) {
    int64 deg = 2;
    int64 result = (1LL << n);
    while ((i + deg - 1) < (1LL << n)) {
       result /= 2;
       deg *= 2;
    }
    return result <= p;
}

void solve() {
    int64 n, p;
    cin >> n >> p;
    
    int64 left = 0;
    int64 right = (1LL << n) - 1;
    while (right - left > 10) {
        int64 m = (left + right) / 2;
        if (calc1(m, n, p))
             left = m;
        else
             right = m;
    }
    for (int64 i = right; i >= left; --i)
        if (calc1(i, n, p)) {
            cout << i << " ";
            break;
        }
    left = 0;
    right = (1LL << n) - 1;
    while (right - left > 10) {
        int64 m = (left + right) / 2;
        if (calc2(m, n, p))
             left = m;
        else
             right = m;
    }
    for (int64 i = right; i >= left; --i)
        if (calc2(i, n, p)) {
            cout << i << endl;
            break;
        }
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
