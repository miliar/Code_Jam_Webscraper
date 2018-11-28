// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; ++i)
/*
#define cin fin
*/
#define cout fout

//ifstream fin(".in");
ofstream fout("res.out");

const int N = 40, M = 13, mod = 0;

map<pair<int, int>, int> address;
int match[N], per[N], n, m, dir[N];
pair<int, int> p[N];
int dx[] = {1, 0, -1, 0};
int dy[] = {0, -1, 0, 1};
int mat[N][N];
bool out(int i, int j) { return (i < 0 || j < 0 || i >= n || j >= m); }
int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int tc;
    cin >> tc;
    rep(ntc, tc) {
        address.clear();
        cout << "Case #" << ntc + 1 << ":\n";
        // Clear Start
        
        // Clear End
        // Start
        cin >> n >> m;
        for (int i = 0; i < 2 * (n + m); ++i) {
            cin >> per[i];
            per[i]--;
        }
        for (int i = 0; i < 2 * (n + m); ++i)
            match[per[i]] = per[i ^ 1];
        for (int i = 0, y = 0; y < m; ++i, ++y)
            p[i] = make_pair(-1, y), dir[i] = 0;
        for (int i = m, x = 0; x < n; ++i, ++x)
            p[i] = make_pair(x, m), dir[i] = 1;
        for (int i = n + m, y = m - 1; y >= 0; --y, ++i)
            p[i] = make_pair(n, y), dir[i] = 2;
        for (int i = n + m + m, x = n - 1; x >= 0; --x, ++i)
            p[i] = make_pair(x, -1), dir[i] = 3;
        for (int i = 0; i < 2 * (n + m); ++i)
            address[p[i]] = i;
        bool flag = 0;
        for (int mask = 0; mask < (1 << (n * m)); ++mask) {
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < m; ++j) {
                    int id = i * m + j;
                    mat[i][j] = mask >> id & 1;
                }
            bool ok = 1;
            for (int i = 0; i < 2 * (n + m); ++i) {
                int x = p[i].first, y = p[i].second, d = dir[i];
                while (true) {
                    int nx = x + dx[d], ny = y + dy[d];
                    if (out(nx, ny) && address[make_pair(nx, ny)] != match[i]) {
                        ok = 0;
                        break;
                    }
                    if (out(nx, ny))
                        break;
                    if (mat[nx][ny] == 0)
                        d ^= 3;
                    else
                        d ^= 1;
                    x = nx;
                    y = ny;
                }
            }
            if (ok) {
                for (int i = 0; i < n; ++i) {
                    for (int j = 0; j < m; ++j)
                        cout << (mat[i][j] == 1? '/': char(92));
                    cout << '\n';
                }
                flag = 1;
                break;
            }
        }
        if (!flag)
            cout << "IMPOSSIBLE\n";
        // End
    }
}













