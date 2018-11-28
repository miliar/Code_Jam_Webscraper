#include <bits/stdc++.h>
using namespace std;
const int N = 205;
int n , K;
double p[N];
double f[2][N];
void work() {
    scanf("%d%d" , &n , &K);
    for (int i = 0 ; i < n ; ++ i) {
        scanf("%lf" , p + i);
    }
    sort(p , p + n);
    double res = 0;
    for (int i = 0 ; i + n - K - 1 < n ; ++ i) {
        int cur = 0 , nxt = 1;
        memset(f , 0 , sizeof(f));
        f[0][0] = 1;
        for (int j = 0 ; j < n ; ++ j) {
            if (j < i || j > i + n - K - 1) {
                memset(f[nxt] , 0 , sizeof(f[nxt]));
                for (int k = 0 ; k <= n ; ++ k) {
                    f[nxt][k] += f[cur][k] * (1 - p[j]);
                    if (k < n) {
                        f[nxt][k + 1] += f[cur][k] * p[j];
                    }
                }
                swap(nxt , cur);
            }
        }
        //printf("%d : %f\n" , i , f[cur][K / 2]);
        res = max(res , f[cur][K / 2]);
    }
    printf("%.12f\n" , res);
}

int main() {
    int ca = 0 , T;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}
