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

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int ans = 0;
    int tot = 0;
    for (int i = 0; i <= n; i++) {
        if (s[i] != '0' && tot < i) {
            ans += i - tot;
            tot = i;
        }
        tot += s[i] - '0';
    }
    cout << ans << "\n";
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
