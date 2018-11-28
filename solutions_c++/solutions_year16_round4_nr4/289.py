#include <bits/stdc++.h>
using namespace std;

const int N = 4;
bool f[1 << N];
int a[N], n;

bool check() {
    for (int i = 0; i < n; ++i) {
        memset(f, 0, sizeof f);
        f[0] = true;
        for (int j = 0; j < n; ++j) if (i != j) {
            for (int mask = (1 << n) - 1; mask >= 0; --mask) if (f[mask]) {
                for (int k = 0; k < n; ++k) if ((a[j] & 1 << k) != 0) f[mask | 1 << k] = true;
            }
        }
        if (f[a[i]]) return false;
    }
    return true;
}

bool backtrack(int x, int y, int total) {
    if (total < 0) return false;
    if (y == n) return backtrack(x + 1, 0, total);
    //if (n * n - (n * x + y) < total) return false;
    if (x == n) return check(); 
    if ((a[x] & 1 << y) != 0) return backtrack(x, y + 1, total - 1);
    else {
        if (backtrack(x, y + 1, total)) return true;
        a[x] |= 1 << y;
        bool tmp = backtrack(x, y + 1, total - 1);
        a[x] &= ~(1 << y);
        if (tmp) return tmp;
    }
    return false;
}

bool possible(int total) {
    return backtrack(0, 0, total);
}

int runTest() {
    cin >> n;
    int now = 0;
    for (int i = 0; i < n; ++i) {
        a[i] = 0;
        for (int j = 0; j < n; ++j) {
            char c; cin >> c;
            a[i] |= (c - '0') << j;
        }
        now += __builtin_popcount(a[i]);
    }
    int low = now, high = n * n;
    while (low < high) {
        int mid = (low + high) / 2;
        if (possible(mid)) high = mid;
        else low = mid + 1;
    }
    return low - now;
}

int main() {
    int nt; cin >> nt;
    for (int tc = 1; tc <= nt; ++tc) cout << "Case #" << tc << ": " << runTest() << endl;
    return 0;
}
