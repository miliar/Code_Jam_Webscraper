#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;


char m[5][5];

bool usdw[5];
bool usdm[5];

int N;

bool find() {
    for (int i = 0; i < N; ++i) {
        if (usdw[i])
            continue;
        bool g = false;
        for (int j = 0; j < N; ++j) {
            if (!usdm[j] && m[i][j] == '1') {
                g = true;
                usdw[i] = true;
                usdm[j] = true;
                bool res = find();
                usdw[i] = false;
                usdm[j] = false;
                if (!res)
                    return false;
            }
        }
        if (!g)
            return false;
    }
    return true;
}

bool add(int cnt, int x, int y) {
    if (cnt == 0)
        return find();
    if (y >= N)
        return false;
    int nx = x + 1;
    int ny = y;
    if (nx == N) {
        ++ny;
        nx = 0;
    }
    if (m[x][y] == '0') {
        m[x][y] = '1';
        bool res = add(cnt - 1, nx, ny);
        m[x][y] = '0';
        if (res)
            return true;
    }
    return add(cnt, nx, ny);
}

void solve() {
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        scanf("%s", m[i]);
        usdw[i] = false;
        usdm[i] = false;
    }
    for (int i = 0; ; ++i) {
        if (add(i, 0, 0)) {
            printf("%d\n", i);
            return;
        }
    }
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}