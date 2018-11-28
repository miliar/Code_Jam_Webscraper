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


int a[100010];

void solve() {
    int n, x;
    cin >> n >> x;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }
    sort(a + 1, a + n + 1);
    int ans = 0;
    for (int i = n, j = 1; i >= j; --i) {
        if (a[i] + a[j] <= x) {
            ++ j;
        }
        ++ ans;
    }
    cout << ans << endl;
}

int main() {
    int testcase;
    freopen("/Users/xhSong/Downloads/A-large.in", "r", stdin);
    freopen("/Users/xhSong/gcj/a.txt", "w", stdout);
    cin >> testcase;
    for (int i = 1; i <= testcase; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
