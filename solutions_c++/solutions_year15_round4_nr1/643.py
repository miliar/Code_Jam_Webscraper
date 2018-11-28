#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long LL;
const int N = 105;
char mp[N][N];
int n, m;

bool in(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

int ind[N * N], outd[N * N];
int col[N], row[N];
int main() {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int ca = 1; ca <= T; ++ca) {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; ++i) scanf("%s", mp[i]);
        memset(ind, 0, sizeof(ind));
        memset(outd, 0, sizeof(outd));
        memset(row, 0, sizeof(row));
        memset(col, 0, sizeof(col));
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                if(mp[i][j] == '.') continue;
                ++row[i];
                ++col[j];
                int dx = 0, dy = 0;
                if(mp[i][j] == '^') dx = -1;
                if(mp[i][j] == 'v') dx = 1;
                if(mp[i][j] == '<') dy = -1;
                if(mp[i][j] == '>') dy = 1;
                int x = i, y = j;
                while(1) {
                    x += dx; y += dy;
                    if(!in(x, y)) break;
                    if(mp[x][y] == '.') continue;
                    ++ind[x * m + y];
                    ++outd[i * m + j];
                    break;
                }
            }
        }
        int flag = 0;
        int ans = 0;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                if(mp[i][j] == '.') continue;
                if(row[i] == 1 && col[j] == 1) flag = 1;
                if(outd[i * m + j] == 0) ++ans;
            }
        }
        printf("Case #%d: ", ca);
        if(flag) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}
