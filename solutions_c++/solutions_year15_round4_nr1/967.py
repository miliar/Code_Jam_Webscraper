#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

typedef pair<int, int> PP;
typedef long long LL;
#define pb push_back
#define fr first
#define sc second

char s[200][200];
int n, m, d[200][200];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0,  0, -1, 1};

bool check(int x, int y, int r) {
    for (int i = x + dx[r], j = y + dy[r]; i >= 0 && i < n && j >= 0 && j < m; i += dx[r], j += dy[r])
        if (s[i][j] != '.') return true;
    return false;
}
void solve() {
    cin >> n >> m;
    for (int i = 0; i < n; i ++) cin >> s[i];
    memset(d, -1, sizeof(d));
    int res = 0;
    for (int i = 0; i < n; i ++) 
        for (int j = 0; j < m; j ++) if (s[i][j] != '.') {
            int t = -1;
            if (s[i][j] == '^') t = 0;
            else if (s[i][j] == 'v') t = 1;
            else if (s[i][j] == '<') t = 2;
            else t = 3;
            if (check(i, j, t)) continue;
            int flag = 0;
            for (int k = 0; k < 4; k ++) 
                if (check(i, j, k)) flag = 1;
            if (flag) res ++;
            else {
                cout << "IMPOSSIBLE" << endl;
                return;
            }
        }
    cout << res << endl;
}
int main() {
    #ifdef _TEST_
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i ++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    return 0;
}
