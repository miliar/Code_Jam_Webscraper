
#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
using namespace std;
typedef long long LL;
int ca;
#define N 52
int n , m , C;
bool f[N][N][N * N];
int pre[N][N][N * N];
int cnt[N * N];
int num[N];
char s[N][N];
char t[N][N];
int dx[] = {1 , 1 , 1 , 0 , 0 , -1 , -1 , -1 , 0};
int dy[] = {1 , 0 , -1 , 1 , -1 , -1 , 0 , 1 , 0};

void work()
{
    int i , j , k , l , x;
    cin >> n >> m >> C;
    printf("Case #%d:\n" , ++ ca);
    if (n == 1) {
        putchar('c');
        for (i = 0 ; i < m - 1 - C ; ++ i)
            putchar('.');
        for (i = 0 ; i < C ; ++ i)
            putchar('*');
        puts("");
        return;
    }
    if (m == 1) {
        puts("c");
        for (i = 0 ; i < n - 1 - C ; ++ i)
            puts(".");
        for (i = 0 ; i < C ; ++ i)
            puts("*");
        return;
    }
    if (C + 1 == n * m) {
        putchar('c');
        for (i = 1 ; i < m ; ++ i)
            putchar('*');
        puts("");
        for (i = 2 ; i <= n ; ++ i) {
            for (j = 1 ; j <= m ; ++ j)
                putchar('*');
            puts("");
        }
        return;
    }
    if (C == 0) {
        putchar('c');
        for (i = 1 ; i < m ; ++ i)
            putchar('.');
        puts("");
        for (i = 2 ; i <= n ; ++ i) {
            for (j = 1 ; j <= m ; ++ j)
                putchar('.');
            puts("");
        }
        return;
    }
    memset(f , 0 , sizeof(f));
    memset(cnt , -1 , sizeof(cnt));
    f[1][0][0] = 1;
    for (i = 1 ; i < m ; ++ i) {
        f[1][i][2 * i + 2] = 1;
        cnt[2 * i + 2] = 10000 + i;
    }
    f[1][m][2 * m] = 1;
    cnt[2 * m] = 10000 + m;
    for (i = 1 ; i < n ; ++ i) {
        for (j = 0 ; j <= m ; ++ j) {
            for (k = 0 ; k <= n * m ; ++ k) {
                if (!f[i][j][k]) continue;
                cnt[k] = i * 10000 + j;
                for (l = 0 ; l <= j ; ++ l) {
                    if (l == 0) {
                        f[i + 1][l][k] = 1;
                        pre[i + 1][l][k] = j * 10000 + k;
                    } else if (l == m) {
                        f[i + 1][l][k + m] = 1;
                        pre[i + 1][l][k + m] = j * 10000 + k;
                    } else {
                        f[i + 1][l][k + l + 1] = 1;
                        pre[i + 1][l][k + l + 1] = j * 10000 + k;
                    }
                }
            }
        }
    }
    C = n * m - C;
    if (!~cnt[C]) {
        puts("Impossible");
        return;
    }
    memset(num , 0 , sizeof(num));
    i = cnt[C] / 10000 , j = cnt[C] % 10000 , k = C;
    while (i > 0) {
        num[i] = j;
        x = pre[i][j][k];
        -- i , j = x / 10000 , k = x % 10000;
    }
    for (i = 1 ; i <= n ; ++ i)
        for (j = 1 ; j <= m ; ++ j)
            t[i][j] = '*';
    memset(s , 0 , sizeof(s));
    for (i = 1 ; i <= n ; ++ i)
        for (j = 1 ; j <= num[i] ; ++ j)
            s[i][j] = '.';
    for (i = 1 ; i <= n ; ++ i) {
        for (j = 1 ; j <= m ; ++ j) {
            for (k = 0 ; k < 9 ; ++ k)
                if (s[i + dx[k]][j + dy[k]] == '.')
                    t[i][j] = '.';
        }
    }
    t[1][1] = 'c';
    for (i = 1 ; i <= n ; ++ i) {
        for (j = 1 ; j <= m ; ++ j)
            putchar(t[i][j]);
        puts("");
    }
    //for (i = 1 ; i <= n * m ; ++ i)
    //    if (~cnt[i])
    //        printf("%d\n" , i);

}

int main (){
    freopen("1.txt" , "r" , stdin);
    freopen("2.txt" , "w" , stdout);

    int T;
    scanf("%d",&T);
    while (T --) {
        work();
    }
    return 0;
}
