#include <algorithm>
#include <bitset>
#include <cctype>
#include <cfloat>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
#include <utility>
#include <vector>

using namespace std;
typedef long long ll;

void print_case(int tc) { printf("Case #%d: ", tc); }
#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }

void solve_case() {
    int i, j, d;
    int grid[4][4], can[16], two = 0, ans = 0;
    d = getint();
    for (i = 0; i < 16; i++) can[i] = 0;
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) {
        grid[i][j] = getint();
    }
    for (i = 0; i < 4; i++) can[grid[d - 1][i] - 1]++;
    d = getint();
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) {
        grid[i][j] = getint();
    }
    for (i = 0; i < 4; i++) can[grid[d - 1][i] - 1]++;
    for (i = 0; i < 16; i++) if (can[i] == 2) two++, ans = i + 1;
    if (two == 1) {
        printf("%d\n", ans);
    } else if (two == 0) {
        printf("Volunteer cheated!\n");
    } else {
        printf("Bad magician!\n");
    }
}

int main () {
    int tcc, tc = getint();
    for (tcc = 1; tcc <= tc; tcc++) {
        print_case(tcc);
        solve_case();
    }
    return 0;
}
