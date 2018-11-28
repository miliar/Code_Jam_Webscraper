#include <cstdio>
#include <cstring>
using namespace std;

int n, m;
int a[110][110];

int good(int x, int y){
    int ax = 1, ay = 1;
    for (int i = 0; ax && i < n; i++)
        if (a[i][y] > a[x][y]) ax = 0;
    for (int i = 0; ay && i < m; i++)
        if (a[x][i] > a[x][y]) ay = 0;
    if (ax + ay >= 1) return 1;
    return 0;
}

int check(){
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (!good(i, j) ) return 0;
    return 1;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int cases; scanf("%d", &cases);
    
    for (int tc = 1; tc <= cases; tc++){
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &a[i][j]);
        printf("Case #%d: ", tc);
        if (check() ) puts("YES");
        else puts("NO");
    }
    return 0;   
}
