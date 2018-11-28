#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int n, m;
double p[300], a[300], f[500][500];
double ans;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++ cas){
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++ i)
            scanf("%lf", &p[i]);
        sort(p, p + n);
        for (int i = 0; i < m; ++ i){
            a[i + 1] = p[i];
        }
        ans = 0;
        int cnt = 0;
        while (true){
            memset(f, 0, sizeof(f));
            f[0][0] = 1;
            for (int i = 1; i <= m; ++ i)
                for (int j = 0; j <= i; ++ j){
                    if (j > 0)
                    f[i][j] += f[i - 1][j - 1] * a[i];
                    f[i][j] += f[i - 1][j] * (1 - a[i]);
                }
            if (f[m][m / 2] < ans) break;
            ans = f[m][m / 2];
            cnt ++;
            if (m - cnt + 1 < 1) break;
            a[m - cnt + 1] = p[n - cnt];
        }
        printf("Case #%d: %.10lf\n", cas, ans);
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
