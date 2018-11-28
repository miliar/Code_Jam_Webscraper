#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

const int maxn = 128;
const int maxt = 1024;

int f[maxn][maxt][2];
int hp[maxn], g[maxn];

int solve() {
    memset(f, 180, sizeof(f));

    int n, P, Q;
    scanf("%d%d%d", &P, &Q, &n);
    for (int i = 0; i < n; ++i)
        scanf("%d%d", hp + i, g + i);

    f[0][0][0] = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < maxt; ++j)
            for (int k = 0; k < 2; ++k)
                if (f[i][j][k] >= 0) {
                    int val = f[i][j][k];
                    int current_hp = hp[i];
                    for (int hit = 0; current_hp >= 0; ++hit, current_hp -= P) {
                        int can = 0;
                        int cost;
                        if (current_hp > 0) {
                            int remain = current_hp % Q;
                            if (remain == 0) remain = Q;
                            if (remain > P) continue;
                            can = current_hp / Q + (k == 0) + j;
                            if (remain == Q) --can;
                            cost = hit + 1;
                        } else {
                            can = j;
                            cost = hit;
                        }
                        if (can >= cost) {
                            f[i+1][can-cost][1] = max(f[i+1][can-cost][1], val + g[i]);
                        }
                    }
                    int get = (hp[i] - 1) / Q + (k == 0);
                    f[i+1][j+get][0] = max(f[i+1][j+get][0], val);
                }
    }

  /*  for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= 5; ++j) {
            printf("%d,%d  ", f[i][j][0],f[i][j][1]);
        } printf("\n");
    }*/

    int ans = 0;
    for (int j = 0; j< maxt; ++j)
        for (int k = 0; k < 2; ++k)
            ans = max(ans, f[n][j][k]);
    return ans;
}

int main()
{
    freopen("D:\\work\\gcj14\\r4\\cppinput.txt", "r", stdin);
   freopen("D:\\work\\gcj14\\r4\\cppoutput.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: %d\n", i,  solve());
    }
    fprintf(stderr, "done\n");
    return 0;
}


