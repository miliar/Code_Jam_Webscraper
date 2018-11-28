#include <stdio.h>

int K, R, C;
int map[55][55];
int qx[9] = {-1, -1, -1, 0, 0, 1, 1, 1};
int qy[9] = {-1, 0, 1, -1, 1, -1, 0, 1};

void print(){
    
    int i, j;

    for (i = 1; i <= R; i++){
        for (j = 1; j <= C; j++){
            if (i + j == 2) printf("c");
            else if (map[i][j] == 0) printf("*");
            else printf(".");
        }
        printf("\n");
    }

}
int back(int x, int y, int cnt){

    if (cnt == R*C - K) {
        print();
        return 1;
    }
    if (cnt > R*C - K)
        return 0;
    int i, a = 0;
    for (i = 0; i < 8; i++){
        int tx = x + qx[i];
        int ty = y + qy[i];
        if ((tx < 1 || tx > R) || (ty < 1 || ty > C)) continue;
        if (map[tx][ty] == 0) {
            map[tx][ty] = cnt + 1;
            a++;
        }
    }
    
    for (i = 0; i < 8; i++){
        int tx = x + qx[i];
        int ty = y + qy[i];
        if ((tx < 1 || tx > R) || (ty < 1 || ty > C)) continue;
        if (map[tx][ty] != cnt + 1) continue;
        if (back(tx, ty, cnt + a) == 1) return 1;
    }
    for (i = 0; i < 8; i++){
        int tx = x + qx[i];
        int ty = y + qy[i];
        if ((tx < 1 || tx > R) || (ty < 1 || ty > C)) continue;
        if (map[tx][ty] == cnt + 1) map[tx][ty] = 0;
    }
    return 0;

}
int main(){

    int T;
    scanf("%d", &T);
    
    int i, j, k;
    for (i = 0; i < T; i++){
        
        for (j = 1; j <= 50; j++){
            for (k = 1; k <= 50; k++){
                map[j][k] = 0;
            }
        }
        
        scanf("%d %d %d", &R, &C, &K);
        
        printf("Case #%d:\n", i + 1);
        map[1][1] = 1;
        if (back(1, 1, 1) == 1) continue;
        printf("Impossible\n");

    }

}
