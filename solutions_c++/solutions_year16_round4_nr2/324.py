#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxn = 200 + 10;

double p[maxn];
int n, k;

double f[maxn][maxn];
double a[maxn];

void solve() {
    double ans = 0;
    for(int sta = 0; sta <= k; sta++) {
        int lft = k - sta;
        int now = 0;
        for(int i = 0; i < sta; i++) {
            now++;
            a[now] = p[i];
        }
        for(int i = 0; i < lft; i++) {
            now++;
            a[now] = p[n - 1 - i];
        }
        memset(f, 0, sizeof(f));
            f[0][0] = 1;
            for(int i = 1; i <= k; i++) {
                f[i][0] = f[i - 1][0] * (1 - a[i]);
                for(int j = 1; j <= i; j++) {
                    f[i][j] = f[i - 1][j] * (1 - a[i]) + f[i - 1][j - 1] * a[i];
                }
            }
            /*for(int i = 1; i <= k; i++) {
                for(int j = 0; j <= k; j++) {
                    printf("%d  %d  %.3f\n", i, j, f[i][j]);
                }
            }*/
            ans = max(ans, f[k][k / 2]);
    }
    /*int key = (1 << n);
    for(int sta = 0; sta < key; sta ++) {
        int cnt = 0;
        for(int i = 0; i < n; i++) {
            if((1 << i) & sta) {
                cnt++;
            }
        }
        if(cnt == k) {
            int now = 0;
            for(int i = 0; i < n; i++) {
                if((1 << i) & sta) {
                    now++;
                    a[now] = p[i];

                }
            }
            memset(f, 0, sizeof(f));
            f[0][0] = 1;
            for(int i = 1; i <= k; i++) {
                f[i][0] = f[i - 1][0] * (1 - a[i]);
                for(int j = 1; j <= i; j++) {
                    f[i][j] = f[i - 1][j] * (1 - a[i]) + f[i - 1][j - 1] * a[i];
                }
            }
            /*for(int i = 1; i <= k; i++) {
                for(int j = 0; j <= k; j++) {
                    printf("%d  %d  %.3f\n", i, j, f[i][j]);
                }
            }
            ans = max(ans, f[k][k / 2]);
        }
    }*/
    printf("%.10f\n", ans);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("Bout.txt", "w", stdout);
    int ncase;
    scanf("%d", &ncase);
    for(int i = 1; i <= ncase; i++) {
        scanf("%d%d", &n, &k);
        for(int j = 0; j < n; j++) {
            scanf("%lf", &p[j]);
        }
        sort(p, p + n);
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
