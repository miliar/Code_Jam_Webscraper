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

typedef vector<int> row;
typedef vector< vector<int> > matr;

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};

set<matr> ans;

int n, m;
matr a;

void addAnswer() {
    matr b(m, row(n, 0));
    forn(j, m) forn(i, n) b[j][i] = a[i][j];
    matr mn = b;
    forn(it, 5) {
        rotate(b.begin(), b.begin() + 1, b.end());
        if (mn > b) mn = b;
    }
    ans.insert(mn);
}

bool checkRow(int r) {
    forn(j, m) {
        int s = 0;
        forn(d, 4) {
            int x = r + dx[d];
            int y = (m + j + dy[d]) % m;
            if (x < 0 || x >= n) continue;
            if (a[x][y] == a[r][j]) s++;
        }
        if (s != a[r][j]) return false;
    }
    return true;
}

void rec(int i, int j) {
    if (j == m) {
        if (i > 0 && !checkRow(i - 1)) return;
        i++;
        j = 0;
    }
    if (i == n) {
        if (checkRow(i - 1)) addAnswer();
        return;
    }
    for (int k = 1; k <= 4; k++) {
        int f = 0, s = 0;
        forn(d, 4) {
            int x = i + dx[d];
            int y = (j + m + dy[d]) % m;
            if (x >= n || x < 0) continue;
            if (a[x][y] == 0) {
                f++;
            } else if (a[x][y] == k) s++;
        }
        if (s > k) continue;
        if (s + f < k) continue;
        a[i][j] = k;
        rec(i, j + 1);
        a[i][j] = 0;
    }
}

void solveCase(int tc) {
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    cin >> n >> m;
    a = matr(n, row(m, 0));
    ans.clear();
    rec(0, 0);
    /*
    for (auto x : ans) {
        forn(i, n) {
            forn(j, m) cout << x[j][i];
            cout << endl;
        }
        cout << endl;
    }*/
    printf("%d\n", ans.size());
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
