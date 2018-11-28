#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>
#include <memory.h>

#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>

#define NAME "test-large"

#define EPS (1e-9)
#define INF ((int)(1e+9))
#define LINF ((long long)(1e+18))

#define ve vector<int>
#define pb push_back

#define pii pair<int, int>
#define mp make_pair
#define fi first
#define se second
#define fs first
#define sc second

using namespace std;

typedef long long li;
typedef long long ll;
typedef long long lint;

void solve(int test_number);

int main() {
#ifdef _GEANY
    freopen(NAME ".in", "r", stdin);
    freopen(NAME ".out", "w", stdout);
#else
#endif
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(3);
    int n = 1;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i + 1);
    }
    return 0;
}

const int MAXN = 110;

int n, m;
string a[MAXN];
int ddx[4] = { 0, 0, 1, -1 };
int ddy[4] = { 1, -1, 0, 0 };

void solve(int test_number) {
    cin >> n >> m;
    string x;
    for (int i = 0; i <= m + 2; i++)
        x += "0";
    a[0] = a[n + 1] = x;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        a[i] = "0" + a[i] + "0";
    }

    cout << "Case #" << test_number << ": ";

    int res = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i][j] == '.')
                continue;
            int dx, dy;
            if (a[i][j] == '^')
                dx = -1, dy = 0;
            else if (a[i][j] == '<')
                dx = 0, dy = -1;
            else if (a[i][j] == '>')
                dx = 0, dy = 1;
            else
                dx = 1, dy = 0;
            int x = i, y = j;
            bool flag = false;
            while (true) {
                x += dx, y += dy;
                if (a[x][y] == '0') {
                    flag = true;
                    res++;
                    break;
                } else if (a[x][y] != '.')
                    break;
            }
            if (flag) {
                int cnt = 4;
                for (int d = 0; d < 4; d++) {
                    int x = i, y = j;
                    int dx = ddx[d], dy = ddy[d];
                    while (true) {
                        x += dx, y += dy;
                        if (a[x][y] == '0') {
                            flag = true;
                            cnt--;
                            break;
                        } else if (a[x][y] != '.')
                            break;
                    }
                }
                if (cnt == 0) {
                    cout << "IMPOSSIBLE" << endl;
                    return;
                }
            }
        }
    }
    cout << res << endl;
}

