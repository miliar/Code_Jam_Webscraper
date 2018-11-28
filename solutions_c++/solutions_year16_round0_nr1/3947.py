# include <iostream>
# include <cmath>
# include <algorithm>
# include <map>
# include <vector>
using namespace std;
 
  bool used[10];

void rec(long long x) {
    if (x == 0) {
        used[0] = true;
    }
    else {
        while (x > 0) {
            used[x % 10] = true;
            x /= 10;
        }
    }
}

void solve(int test) {
    cout << "Case #" << test << ": ";
    long long n,x;
    cin >> n;
    x = n;
    for (int i = 0; i < 10; i++) {
        used[i] = false;
    }
    for (int iter = 0; iter <= 10000000; iter++) {
        rec(n);
        bool ok = true;
        for (int i = 0; i < 10; i++) {
            if (!used[i]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << n << "\n";
            return;
        }
        n += x;
    }
    cout << "INSOMNIA\n";
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        solve(t);
    }
    return 0;
}

