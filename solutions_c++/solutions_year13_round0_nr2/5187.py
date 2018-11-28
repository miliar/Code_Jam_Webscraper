#include <cstdio>

#define N 100
int t, n, m;
int field[N + 2][N + 2];
int maxcol[N + 2], maxrow[N + 2];

int max(int a, int b){
    if(a >= b)
        return a;
    return b;
}
int min(int a, int b){
    if(a <= b)
        return a;
    return b;
}

int main(){
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &t);
    for(int c = 1; c <= t; c++){
        scanf("%d%d", &n, &m);
        for(int i = 0; i < N + 2; i ++){
            maxcol[i] = 0;
            maxrow[i] = 0;
        }
        for(int i = 0; i < n; i ++)
            for(int j = 0; j < m; j ++){
                scanf("%d", &field[i][j]);
                maxrow[i] = max(maxrow[i], field[i][j]);
                maxcol[j] = max(maxcol[j], field[i][j]);
            }
        bool ans = true;
        for(int i = 0; i < n; i ++)
            for(int j = 0; j < m; j ++)
                if(field[i][j] < min(maxrow[i], maxcol[j])){
                    ans = false;
                    break;
                }
        printf("Case #%d: %s\n", c, ans ? "YES" : "NO");
    }
    fflush(stdout);
    return 0;
}
