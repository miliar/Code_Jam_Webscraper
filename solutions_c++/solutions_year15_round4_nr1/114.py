#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
#include <queue>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};

bool bad(int d, const vs & v, int i, int j) {
    while (1) {
        i += dx[d];
        j += dy[d];
        if (i >= 0 && j >= 0 && i < v.size() && j < v[i].size()) {
            if (v[i][j] != '.') return false;
        } else break;
    }
    return true;
}

bool allbad(const vs & v, int i, int j) {
    for (int d = 0; d < 4; ++d) if (!bad(d, v, i, j))
        return false;
    return true;
}

int main() {
    int T;
    cin >> T;
    map<char, int> dir;
    dir['>'] = 0;
    dir['^'] = 1;
    dir['<'] = 2;
    dir['v'] = 3;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        int n,m;
        cin >> n >> m;
        vs v(n);
        for (int i = 0; i < n; ++i) cin >> v[i];
        int cnt = 0;
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) if (v[i][j] != '.') {
            int d = dir[v[i][j]];
            if (bad(d, v, i, j)) ++cnt;
            if (allbad(v, i, j)) cnt = 1e9;
        }
        if (cnt <= n * m) {
            cout << cnt << endl;
        } else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
