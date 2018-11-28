/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

int t, n, m, cell[8][8], ans;
set<deque<vector<int> > > sol;

inline bool check2(int x, int y) {
    int k = cell[x][y];
    if (k == 0) return true;
    int cnt[4] = {};
    if (x > 0) cnt[cell[x - 1][y]]++;
    if (x + 1 < n) cnt[cell[x + 1][y]]++;
    cnt[cell[x][(y > 0 ? y - 1 : m - 1)]]++;
    cnt[cell[x][(y == m - 1 ? 0 : y + 1)]]++;
    if (cnt[k] > k) return false;
    if (cnt[k] < k && cnt[0] == 0) return false;
    return true;
}

inline bool check(int x, int y) {
    bool f = check2(x, y);
    if (x > 0) f &= check2(x - 1, y);
    if (x + 1 < n) f &= check2(x + 1, y);
    f &= (y > 0 ? check2(x, y - 1) : check2(x, m - 1));
    f &= (y == m - 1 ? check2(x, 0) : check2(x, y + 1));
    return f;
}

void dfs(int x, int y) {
    if (x == n && y == 0) {
        deque<vector<int> > v(m);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                v[i].push_back(cell[j][i]);
            }
        }
        if (sol.find(v) != sol.end())
            return;
        for (int i = 0; i < m; ++i) {
            vector<int> vv = v.front();
            v.pop_front();
            v.push_back(vv);
            sol.insert(v);
        }
        ++ans;
        return;
    }
    for (int i = 1; i <= 3; ++i) {
        cell[x][y] = i;
        if (!check(x, y))
            continue;
        if (y == m - 1)
            dfs(x + 1, 0);
        else
            dfs(x, y + 1);
    }
    cell[x][y] = 0;
}

void solve() {
    scanf("%d%d", &n, &m);
    sol.clear();
    memset(cell, 0, sizeof(cell));
    ans = 0;
    dfs(0, 0);
    printf("Case #%d: %d\n", ++t, ans);
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
