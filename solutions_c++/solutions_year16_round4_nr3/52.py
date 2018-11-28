#include <bits/stdc++.h>
using namespace std;
const int N = 505;
int n , m , a[N];
int id[N][N];
int f[N];
int getf(int x) {
    return f[x] == x ? x : f[x] = getf(f[x]);
}
void merge(int x , int y) {
    f[getf(x)] = getf(y);
}

void work() {
    scanf("%d%d" , &n , &m);
    int sum = 2 * (n + m);
    for (int i = 0 ; i < sum ; ++ i) {
        scanf("%d" , &a[i]);
        -- a[i];
    }
    int num = 0;
    for (int i = 0 ; i < n ; ++ i) {
        for (int j = 0 ; j < m ; ++ j) {
            id[i][j] = num ++;
        }
    }
    for (int mask = 0 ; mask < 1 << num ; ++ mask) {
        for (int i = 0 ; i < num * 4 + sum ; ++ i) {
            f[i] = i;
        }
        int tmp = 0;
        for (int i = 0 ; i < m ; ++ i) {
            merge(id[0][i] << 2 | 0 , (num << 2) + tmp ++);
        }
        for (int i = 0 ; i < n ; ++ i) {
            merge(id[i][m - 1] << 2 | 1 , (num << 2) + tmp ++);
        }
        for (int i = m - 1 ; i >= 0 ; -- i) {
            merge(id[n - 1][i] << 2 | 2 , (num << 2) + tmp ++);
        }
        for (int i = n - 1 ; i >= 0 ; -- i) {
            merge(id[i][0] << 2 | 3 , (num << 2) + tmp ++);
        }

        num = 0;
        for (int i = 0 ; i < n ; ++ i) {
            for (int j = 0 ; j < m ; ++ j) {
                if (i > 0) {
                    merge(id[i][j] << 2 | 0 , id[i - 1][j] << 2 | 2);
                }
                if (j > 0) {
                    merge(id[i][j] << 2 | 3 , id[i][j - 1] << 2 | 1);
                }
                if (mask >> num & 1) {
                    merge(num << 2 | 0 , num << 2 | 3);
                    merge(num << 2 | 1 , num << 2 | 2);
                } else {
                    merge(num << 2 | 0 , num << 2 | 1);
                    merge(num << 2 | 3 , num << 2 | 2);
                }
                num ++;
            }
        }
        bool flag = 1;
        for (int i = 0 ; i < n + m && flag; ++ i) {
            if (getf((num << 2) + a[i << 1]) != getf((num << 2) + a[i << 1 | 1])) {
                flag = 0;
            }
        }
        if (flag) {
            for (int i = 0 ; i < num ; ++ i) {
                putchar("\\/"[mask >> i & 1]);
                if (i % m + 1 == m) {
                    puts("");
                }
            }
            return;
        }
    }
    puts("IMPOSSIBLE");
}

int main() {
    int ca = 0 , T;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d:\n" , ++ ca);
        work();
    }
    return 0;
}
