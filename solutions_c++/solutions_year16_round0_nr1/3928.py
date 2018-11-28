# include <iostream>
# include <cmath>
# include <algorithm>
# include <map>
# include <unordered_set>
# include <memory.h>
# include <vector>
using namespace std;
 
 
const int MD = 1000000000 + 7;
const int MAX_E = 500333;
const int MAX_N = 1047;

#define time ez_contest
#define rank ez_timus

bool used[10];

void mark(long long x) {
    if (x == 0) {
        used[0] = true;
        return;
    }
    while (x > 0) {
        used[x % 10] = true;
        x /= 10;
    }
}

void solve(int tc) {
    cout << "Case #" << tc << ": ";
    long long n;
    cin >> n;
    long long a = n;
    for (int i = 0; i < 10; i++) {
        used[i] = false;
    }
    for (int iter = 0; iter <= 10000000; iter++) {
        mark(n);
        bool ok = true;
        for (int i = 0; i < 10; i++) {
            if (used[i] == false) {
                ok = false;
            }
        }
        if (ok) {
            cout << n << "\n";
            return;
        }
        n += a;
    }
    cout << "INSOMNIA\n";
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve(t);
    }
    return 0;
}

