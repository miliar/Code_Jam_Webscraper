#include <bits/stdc++.h>
using namespace std;
const int N = 6;
bool f[N][N][N];
void init(){
    int i, j;
    for(i = 1; i <= 4; i++){
        for(j = 1; j <= 4; j++){
            f[1][i][j] = true;
            if((i*j) & 1)   continue;
            f[2][i][j] = true;
        }
    }
    f[3][2][3] = true;  f[3][3][3] = f[3][3][4] = true;
    f[4][3][4] = true;  f[4][4][4] = true;


}
int main(){
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);
    init();
    int tc, TC, n, r, c;
    scanf("%d", &TC);
    for(tc = 1; tc <= TC; tc++){
        scanf("%d%d%d", &n, &r, &c);
        if(r > c)   swap(r,c);
        printf("Case #%d: %s\n", tc, f[n][r][c] ? "GABRIEL":"RICHARD");
    }
    return 0;
}
