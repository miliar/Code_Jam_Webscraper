#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <cmath>
#include <iomanip>
#include <cassert>
#include <ctime>
#include <bitset>

using namespace std;

int a[1100];

void solve() {
    int n;
    cin >> n;
    for (int i = 0; i <= 1000; i++)
        a[i] = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        a[x]++;
    }
    int ans = 1000;
    for (int i = 1; i <= 1000; i++) {
        int tot = 0;
        for (int j = 1; j <= 1000; j++) {
            tot += (j - 1) / i * a[j];
        }
        ans = min(ans, i + tot);
    }
    cout << ans << endl;
}

int main() {
    freopen("G:/1.in", "r", stdin);
    freopen("G:/1.out", "w", stdout);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
