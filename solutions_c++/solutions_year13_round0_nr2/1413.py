#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <ctime>
#include <cmath>
#include <cassert>
#include <numeric>
#include <algorithm>
using namespace std;

#define N 105
#define M 5200
#define ll long long
#define inf 0x7fffffff
#define lson (id<<1)
#define rson (id<<1|1)

#define eps 1e-6
#define pii pair<int,int>
#define pdd pair<double,int>
#define MP(i,j) make_pair(i,j)
#define It map<int,int>::iterator
#define X first
#define Y second

int n, m, a[N][N], h[N], w[N], b[N][N], c[N *N];

bool judge() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] != b[i][j])
                return false;
        }
    }
    return true;
}

void show() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << b[i][j] << " ";
        }
        cout << endl;
    }
}
void setRow(int r, int x) {
    for (int j = 0; j < m; j++)
        b[r][j] = min(b[r][j], x);
}

void setColumn(int r, int x) {
    for (int i = 0; i < n; i++)
        b[i][r] = min(b[i][r], x);
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int cas, pcas = 1;
    scanf("%d", &cas);
    while (cas--) {
        scanf("%d%d", &n, &m);
        memset(h, 0, sizeof(h)), memset(w, 0, sizeof(w));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%d", &a[i][j]);
                h[i] = max(h[i], a[i][j]);
                w[j] = max(w[j], a[i][j]);
                c[i * m + j] = a[i][j];
                b[i][j] = 100;
            }
        }
        sort(c, c + (n * m));
        int p = unique(c, c + (n * m)) - c;
        for (int i = p - 1; i >= 0; i--) {
            for (int j = 0; j < n; j++) {
                if (h[j] <= c[i])
                    setRow(j, c[i]);
            }
            for (int j = 0; j < m; j++) {
                if (w[j] <= c[i])
                    setColumn(j, c[i]);
            }
        }
        printf("Case #%d: %s\n", pcas++, judge() ? "YES" : "NO");
    }
    return 0;
}
