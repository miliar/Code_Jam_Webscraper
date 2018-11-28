#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

void solve(int tc) {
    cerr << "Case #" << tc << ", " << clock() << " ms.\n";
    cout << "Case #" << tc << ": ";
    int n;
    int x;
    cin >> n >> x;
    vector<int> s(n);
    forn(i, n) cin >> s[i];
    int ans = 0;
    sort(all(s));
    int j = n - 1;
    for (int i = 0; i < n; i++) {
        if (s[i] == -1) continue;
        while (j > i && s[j] + s[i] > x) j--;
        ans++;
        if (j > i) {
            s[i] = -1;
            s[j] = -1;
            j--;
        }
    }
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
