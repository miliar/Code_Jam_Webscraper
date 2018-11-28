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
#define fore(i, l, r) for (int i = (int)(l); i < (int)(r); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};
const string ds = "^>v<";

void solveCase(int tc) {
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    forn(i, n) cin >> a[i];
    int ans = 0;
    forn(i, n) {
        forn(j, m) {
            if (a[i][j] == '.') continue;
            int d = ds.find(a[i][j]);
            int x = i + dx[d];
            int y = j + dy[d];
            while (x >= 0 && x < n && y >= 0 && y < m && a[x][y] == '.') {
                x += dx[d];
                y += dy[d];
            }
            if (x < 0 || x >= n || y < 0 || y >= m) {
                bool f = false;
                forn(k, 4) {
                    int xx = i + dx[k];
                    int yy = j + dy[k];
                    while (xx >= 0 && xx < n && yy >= 0 && yy < m && a[xx][yy] == '.') {
                        xx += dx[k];
                        yy += dy[k];
                    }
                    if (xx >= 0 && xx < n && yy >= 0 && yy < m) {
                        f = true;
                        break;
                    }
                }
                if (!f) {
                    cout << "IMPOSSIBLE" << endl;
                    return;
                }
                ans++;
            }
        }
    }
    cout << ans << endl;
}

int main() {
#ifdef NEREVAR_PROJECT
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
