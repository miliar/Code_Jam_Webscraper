#include <bits/stdc++.h>
using namespace std;
const int N = 105;

int n , m , ca;
char str[N][N];
int id[N][N];
int final[N * N];
void work() {
    int i , j ,  k , x , y;
    scanf("%d%d" , &n ,&m);
    for (i = 1 ; i <= n ; ++ i) {
        scanf("%s" , str[i] + 1);
    }
    int cnt = 0;
    for (i = 1 ; i <= n ; ++ i)
        for (j = 1 ; j <= m ; ++ j)
            id[i][j] = ++ cnt;
    memset(final , 0 , sizeof(final));
    int res = 0;    
    for (i = 1 ; i <= n ; ++ i)
        for (j = 1 ; j <= m ; ++ j) {
            x = i , y = j;
            if (str[i][j] == '^') {
                -- x;
                while (x > 0 && (str[x][y] == '.')) {
                    -- x;
                }
                if (x <= 0)
                    final[id[i][j]] |= 1;              
            }
            if (str[i][j] == '<') {
                -- y;
                while (y > 0 && (str[x][y] == '.')) {
                    -- y;
                }
                if (y <= 0)
                    final[id[i][j]] |= 1;                
            }
            if (str[i][j] == 'v') {
                ++ x;
                while (x <= n && (str[x][y] == '.')) {
                    ++ x;
                }
                if (x > n)
                    final[id[i][j]] |= 1;              
            }
            if (str[i][j] == '>') {
                ++ y;
                while (y <= m && (str[x][y] == '.')) {
                    ++ y;
                }
                if (y > m)
                    final[id[i][j]] |= 1;                
            }

            if (final[id[i][j]]) {
                ++ res;
                x = i , y = j;
                if (str[i][j] != '^') {
                    -- x;
                    while (x > 0 && (str[x][y] == '.')) {
                        -- x;
                    }
                    if (x > 0)
                        continue;
                }
                x = i , y = j;
                if (str[i][j] != '<') {
                    -- y;
                    while (y > 0 && (str[x][y] == '.')) {
                        -- y;
                    }
                    if (y > 0)
                        continue;         
                }
                x = i , y = j;
                if (str[i][j] != 'v') {
                    ++ x;
                    while (x <= n && (str[x][y] == '.')) {
                        ++ x;
                    }
                    if (x <= n)
                        continue;              
                }
                x = i , y = j;
                if (str[i][j] != '>') {
                    ++ y;
                    while (y <= m && (str[x][y] == '.')) {
                        ++ y;
                    }
                    if (y <= m)
                        continue;                
                }  
                printf("Case #%d: IMPOSSIBLE\n" , ++ ca);
                return;
            }
            
        }
    printf("Case #%d: %d\n" , ++ ca ,  res);    
}

int main() {
    freopen("1" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    while (T --)        
        work();
    return 0;
}
