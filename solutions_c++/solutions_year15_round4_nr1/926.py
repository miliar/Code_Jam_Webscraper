#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <vector>
#include <valarray>
#include <array>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <complex>
#include <random>
#include <bitset>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

const int MN = 110;
// >^<v
// x, y
const int d4[4][2] = {
    {1, 0},
    {0, 1},
    {-1, 0},
    {0, -1}
};

int r, c;
int g[MN][MN];


bool bc(int x, int y) {
    return (0 <= x && x < c && 0 <= y && y < r);
}

bool blank(int x, int y, int d) {
    if (!bc(x, y)) return true;
    if (g[y][x] != -1) return false;
    return blank(x+d4[d][0], y+d4[d][1], d);
}


void solve(int T) {
    cin >> r >> c;
    for (int i = 0; i < r; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < c; j++) {
            if (s[j] == '.') g[i][j] = -1;
            else if (s[j] == '>') g[i][j] = 0;
            else if (s[j] == 'v') g[i][j] = 1;
            else if (s[j] == '<') g[i][j] = 2;
            else if (s[j] == '^') g[i][j] = 3;
        }
    }

    bool can = true;
    int sm = 0;
    for (int y = 0; y < r; y++) {
        for (int x = 0; x < c; x++) {
            if (g[y][x] == -1) continue;
            bool f = false;
            for (int i = 0; i < 4; i++) {
                if (!blank(x+d4[i][0], y+d4[i][1], i)) {
                    f = true;
                    break;
                }
            }
            if (!f) can = false;
            if (blank(x+d4[g[y][x]][0], y+d4[g[y][x]][1], g[y][x])) sm++;
        }
    }
    if (!can) {
        printf("Case #%d: IMPOSSIBLE\n", T);
    } else {
        printf("Case #%d: %d\n", T, sm);
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
