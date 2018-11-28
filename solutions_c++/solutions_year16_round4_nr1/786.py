#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <utility>
#include <sstream>

typedef long long ll;

using namespace std;

template<typename T>
T next() { T tmp; cin >> tmp; return tmp; }


string build(int start, int n) {
    if (n == 0) {
        if (start == 0) return "P";
        if (start == 1) return "R";
        if (start == 2) return "S";
        exit(1);
    }
    string a = build(start, n - 1);
    string b = build((start + 1) % 3, n - 1);
    return a < b ? a + b : b + a;
}

void solve() {
    int n = next< int >();
    int req[] = {0, 0, 0};
    req[1] = next< int >();
    req[0] = next< int >();
    req[2] = next< int >();
    
    string best = "";
    for (int start = 0; start < 3; ++start) {
        int a[] = {0, 0, 0};
        a[start] = 1;
        for (int i = 0; i < n; ++i) {
            int b[] = {0, 0, 0};
            for (int j = 0; j < 3; ++j) {
                b[j] += a[j];
                b[(j + 1) % 3] += a[j];
            }
            for (int j = 0; j < 3; ++j) {
                a[j] = b[j];
            }
        }
        if (a[0] == req[0] && a[1] == req[1] && a[2] == req[2]) {
            string cand = build(start, n);
            if (best == "" || cand < best) {
                best = cand;
            }
        }
    }
    if (best == "") {
        best = "IMPOSSIBLE";
    }
    cout << best << endl;
}

int main() {
    int n = next< int >();
    for (int i = 1; i <= n; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
