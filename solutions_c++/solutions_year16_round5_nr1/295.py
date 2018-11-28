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

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;
                   
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()
#define pb push_back


void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    string s;
    cin >> s;
    int ans = 0;
    while (s.size() >= 2) {
        bool f = false;
        forn(i, s.size() - 1) {
            if (s[i] == s[i + 1]) {
                s.erase(i, 2);
                f = true;
                ans += 10;
                break;
            }
        }
        if (!f) break;
    }
    ans += s.size() / 2 * 5;
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
