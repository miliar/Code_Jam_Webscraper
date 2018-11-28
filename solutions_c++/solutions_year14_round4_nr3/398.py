#include <cstdio>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cassert>

using namespace std;

int w, h;
int map[501][102];
int b;
int paths;

int dr[8] = {1, 1, 1, 0, -1, -1, -1, 0};
int dc[8] = {1, 0, -1, -1, -1, 0, 1, 1};

bool inMap(int r, int c) {
    if (r < 0 || r >= h)
        return 0;
    if (c < 0 || c >= w+1)
        return 0;
    return 1;
}

bool valid(int r, int c) {
    if (r < 0 || r >= h)
        return 0;
    if (c < 0 || c >= w+1)
        return 0;
    if (map[r][c] == paths+2)
        return 0;
    if (map[r][c] == 0)
        return 0;
    return 1;
}

void fill(int r, int c) {
    if (r >= 500)
        printf("Rrrrr %d\n", r);
    map[r][c] = paths + 2;
    int i;
    for (i = 0; i < 8; i++)
        if (valid(r+dr[i], c+dc[i]))
            fill(r+dr[i], c+dc[i]);    
}

void printMap() {
    int i, j;
    for (i = 0; i < h; i++) {
        for (j = 0; j < w+1; j++)
             printf("%d ", map[i][j]); 
         printf("\n");
    }
}

void expand() {
    int i, j, k;
    for (i = 0; i < h; i++) {
        for (j = 0; j < w+1; j++) {
            if (map[i][j] != 0)
                continue;
            for (k = 0; k < 8; k++)
                if (inMap(i+dr[k], j+dc[k]) && map[i+dr[k]][j+dc[k]] == paths+2)
                    map[i][j] = paths+1;
        }
    }        
}

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        scanf("%d %d %d", &w, &h, &b);
        int i, j, k;
        int r1, c1, r2, c2;
        for (i = 0; i < h; i++) {
            map[i][0] = 1;
            for (j = 0; j < w; j++)
                map[i][j+1] = 0;
        }
        for (i = 0; i < b; i++) {
            scanf("%d %d %d %d", &c1, &r1, &c2, &r2);
            for (j = r1; j <= r2; j++)
                for (k = c1; k <= c2; k++)
                    map[j][k+1] = 1;
        }
        paths = 0;
        while (true) {
            //printf("filling\n");
            //printMap();
            fill(0, 0);
            //printf("filled\n");
            for (i = 0; i < h; i++)
                if (map[i][w] == paths+2)
                    break;
            if (i != h)
                break;
            //printf("expanding\n");
            expand();
            //printf("expanded\n");
            paths++;
        }
        printf("%d\n", paths);
    }
}