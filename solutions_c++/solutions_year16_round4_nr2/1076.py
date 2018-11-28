#include <stdio.h>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

double f[210][210];
double p[210], p0[210];

double ans = 0;
void check(int n){
        memset(f, 0, sizeof(f));
        f[0][0] = 1.0;
        for (int i = 0; i < n; i ++){
                for (int j = 0; j <= i; j ++){
                        double p1 = f[i][j] * p[i];
                        double p2 = f[i][j] * (1.0 - p[i]);
                        f[i+1][j+1] += p1;
                        f[i+1][j] += p2;
                }
        }
        ans = max(ans, f[n][n/2]);
        return;
}

void dfs(int deep, int x, int n, int k){
        if (deep == k) {
                check(k);
                return;
        }
        if (n - x + deep < k) return;

        for (int i = x; i < n; i ++) {
                p[deep] = p0[i];
                dfs(deep + 1, i + 1, n, k);
        }
}

int main(){
        freopen("b.in", "r", stdin);
        freopen("b.out", "w", stdout);

        int tt, ca = 0;
        scanf("%d", &tt);
        while (tt--) {
                printf("Case #%d: ", ++ca);
                int n, k;
                scanf("%d%d", &n, &k);
                for (int i = 0; i < n; i ++) scanf("%lf", &p0[i]); 
                
                ans = 0;
                dfs(0, 0, n, k);

                printf("%lf\n", ans);
        }
}
