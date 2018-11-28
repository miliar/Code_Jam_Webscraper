#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int t, w, h, b;
int res;
vector <vector <bool> > river;
int changerow[4][4] = {{0,1,0,-1},{1,0,-1,0},{0,-1,0,1},{-1,0,1,0}};
int changecol[4][4] = {{-1,0,1,0},{0,1,0,-1},{1,0,-1,0},{0,-1,0,1}};
int changedir[4][4] = {{3,0,1,2},{0,1,2,3},{1,2,3,0},{2,3,0,1}};

int dfs(int row, int col, int dir) {
    river [row] [col] = false;
    if (row == h) {
        res ++;
        return 0;
    }

    for (int i = 0; i < 4; i++) {
        if (river [row + changerow [dir] [i]] [col + changecol [dir] [i]]) {
            if (dfs ( row + changerow [dir] [i], col + changecol [dir] [i], changedir [dir] [i]) == 0) return 0;
        }
    }


    return 1;
}



int main () {
    int lowlex, lowley, upprx, uppry;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases ++) {
        res = 0;
        scanf("%d %d %d", &w, &h, &b);
        river.resize(h + 2, vector <bool> (w + 2, true));
        for (int i = 0; i < b; i++) {
            scanf("%d %d %d %d", &lowley, &lowlex, &uppry, &upprx);
            lowley ++;
            lowlex ++;
            uppry ++;
            upprx ++;
            for (int j = lowlex; j <= upprx; j++) {
                for (int k = lowley; k <= uppry; k++) river [j] [k] = false;
            }
        }
        for (int i = 0; i < h + 2; i++) {
            river [i] [0] = false;
            river [i] [w + 1] = false;
        }
        for (int i = 0; i < w + 2; i++) {
            river [0] [i] = false;
            river [h + 1] [i] = false;
        }
        for (int i = 1; i <= w; i++) {
            if (river [1] [i]) dfs(1,i,0);
        }
        printf("Case #%d: %d\n", cases, res);



        river.clear();
    }
}
