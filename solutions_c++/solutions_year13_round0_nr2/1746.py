#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 104;

int map[maxn][maxn], high[maxn][maxn][4];
int n, m;

void init() {
     memset(map, 0, sizeof(map));
     memset(high, 0, sizeof(high));
     scanf("%d%d",&n,&m);
     for (int i = 1; i <= n; i++ )
         for (int j = 1; j <= m; j++ )
             scanf("%d",&map[i][j]);
}

void work() {
     for (int i = 1; i <= n; i++ )
         for (int j = 1; j <= m; j++ ) {
             high[i][j][0] = max(map[i][j], high[i-1][j][0]);
             high[i][j][1] = max(map[i][j], high[i][j-1][1]);
         }
     for (int i = n; i >= 1; i-- )
         for (int j = m; j >= 1; j-- ) {
             high[i][j][2] = max(map[i][j], high[i+1][j][2]);
             high[i][j][3] = max(map[i][j], high[i][j+1][3]);
         }
     bool OK = true;
     for (int i = 1; i <= n; i++ )
         for (int j = 1; j <= m; j++ )
             if ((high[i-1][j][0] > map[i][j] || high[i+1][j][2] > map[i][j]) &&
                 (high[i][j-1][1] > map[i][j] || high[i][j+1][3] > map[i][j]))
                 OK = false;
     if (OK) printf("YES\n");
     else printf("NO\n");
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cas;
    scanf("%d",&cas);
    for (int run = 1; run <= cas; run++ ) {
        printf("Case #%d: ", run);
        init();
        work();
    }
    return 0;
}
