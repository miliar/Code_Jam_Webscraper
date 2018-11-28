#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
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
#include <vector>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#define ALL(x) (x).begin(), (x).end()
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); itr++)  
#define FOR(i,b,e) for (int i=(int)(b); i<(int)(e); i++)
#define MP(x,y) make_pair(x,y)
#define REP(i,n) for(int i=0; i<(int)(n); i++)

int r, c;
string a[128];

int ddx[] = {1, -1, 0, 0};
int ddy[] = {0, 0, 1, -1};

int check(int x, int y) {
    int dx = 0;
    int dy = 0;

    if (a[x][y] == '^') dx = -1;
    if (a[x][y] == 'v') dx = 1;
    if (a[x][y] == '<') dy = -1;
    if (a[x][y] == '>') dy = 1;

    int xx = x;
    int yy = y;

    xx += dx;
    yy += dy;
    while (0 <= xx && xx < r && 0 <= yy && yy < c) {
        if (a[xx][yy] != '.')
            return 0;
        xx += dx;
        yy += dy;
    }

    REP (k, 4) {
        dx = ddx[k];
        dy = ddy[k];
        xx = x;
        yy = y;
        
        xx += dx;
        yy += dy;
        while (0 <= xx && xx < r && 0 <= yy && yy < c) {
            if (a[xx][yy] != '.')
                return 1;
            xx += dx;
            yy += dy;
        }
    }

    return -1;
}

void solve() {
    cin >> r >> c;
    REP (i, r)
        cin >> a[i];

    int ret = 0;

    REP (i, r) REP (j, c) {
        if (a[i][j] == '.') continue;
        int tmp = check(i, j);

        if (tmp == -1) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }

        ret += tmp;
    }

    cout << ret << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    REP (i, T) {
        cerr << "Case #" << i+1 << ": " << endl;
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
