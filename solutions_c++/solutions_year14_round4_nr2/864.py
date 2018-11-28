#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

template <typename T>
T gcd(T a, T b) {
    return b? gcd(b, a % b): a;
}

using namespace std;

const int maxn = 1002;

struct Number {
    int x, id, rk;
}a[maxn];

bool byX(const Number &a, const Number &b) {
    return a.x < b.x;
}

bool byID(const Number &a, const Number &b) {
    return a.id < b.id;
}

int b[maxn], c[maxn], f[maxn][maxn];

void solve() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i].x;
        a[i].id = i;
    }
    for (int i = 1; i <= n; ++i) {
        b[i] = 0;
        c[i] = 0;
        for (int j = 1; j < i; ++j) {
            if (a[j].x > a[i].x) {
                ++ b[i];
            }
        }
        for (int j = i + 1; j <= n; ++j) {
            if (a[j].x > a[i].x) {
                ++ c[i];
            }
        }
    }
    
    sort(a + 1, a + n + 1, byX);
    
    memset(f, 0x7, sizeof(f));
    f[0][0] = 0;
    for (int i = 0; i < n; ++i) {
        int idx = a[i + 1].id;
        for (int j = 0; j <= i; ++j) {
            f[i + 1][j] = min(f[i + 1][j], f[i][j] + b[idx]);
            f[i + 1][i] = min(f[i + 1][i], f[j][i] + b[idx]);
            f[i][i + 1] = min(f[i][i + 1], f[i][j] + c[idx]);
            f[j][i + 1] = min(f[j][i + 1], f[j][i] + c[idx]);
        }
    }
    int ans = 0x07070707;
    for (int i = 0; i < n; ++i) {
        ans = min(ans, f[n][i]);
        ans = min(ans, f[i][n]);
    }
    cout << ans << endl;
    /*
    for (int i = 1; i <= n; ++i) {
        cout << a[i].rk << " ";
    }
    cout << endl;
     */

}

int main() {
    int testcase;
    freopen("/Users/xhSong/Downloads/B-large.in", "r", stdin);
    freopen("/Users/xhSong/gcj/b.txt", "w", stdout);
    cin >> testcase;
    for (int i = 1; i <= testcase; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
