#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

bool can0[16], can1[16];

int f0[4][4], f1[4][4];

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        int r;
        cin >> r;
        --r;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> f0[i][j];
            }
        }
        int c;
        cin >> c;
        --c;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> f1[i][j];
            }
        }
        memset(can0, 0, sizeof can0);
        memset(can1, 0, sizeof can1);
        for (int i = 0; i < 4; ++i) {
            can0[f0[r][i] - 1] = true;
        }
        for (int i = 0; i < 4; ++i) {
            can1[f1[c][i] - 1] = true;
        }
        int q = 0;
        int v = 0;
        for (int i = 0; i < 16; ++i) {
            if (can0[i] && can1[i]) {
                ++q;
                v = i + 1;
            }
        }
        if (q == 0) {
            printf("Volunteer cheated!\n");
        } else if (q == 1) {
            printf("%d\n", v);
        } else {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
