#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

typedef long long ll;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

using namespace std;

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    string s;
    int k;
    cin >> s >> k;
    int n = (int)s.size();
    int ans = 0;
    for (int i = 0; i + k <= n; i++) {
        if (s[i] == '-') {
            ans++;
            for (int j = i; j < i + k; j++) {
                if (s[j] == '-') s[j] = '+'; else s[j] = '-';
            }
        }
    }
    for (int i = n - k + 1; i < n; i++) {
        if (s[i] == '-') {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
