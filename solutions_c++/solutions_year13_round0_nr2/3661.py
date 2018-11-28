#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int v[110][110];
int lin, col;
int pd[3][110][110];
int func (int t, int cara, int val) {
    if (pd[t][cara][val] != -1) return pd[t][cara][val];
    if (t == 0) {
        //linha cara
        for (int c = 1; c <= col; c++) {
            if (v[cara][c] > val) {
                return pd[t][cara][val] = 0;
            }
        }
        pd[t][cara][val] = 1;
        for (int c = 1; c <= col; c++) {
            if (v[cara][c] < val) {
                pd[t][cara][val] = pd[t][cara][val]&func(1, c, v[cara][c]);
            }
        }
        return pd[t][cara][val];
    }
    else {
        //coluna cara
        for (int c = 1; c <= lin; c++) {
            if (v[c][cara] > val) return pd[t][cara][val] = 0;
        }
        pd[t][cara][val] = 1;
        for (int c = 1; c <= lin; c++) {
            if (v[c][cara] < val) {
                pd[t][cara][val] = pd[t][cara][val]&func(0, c, v[c][cara]);
            }
        }
        return pd[t][cara][val];
    }
    return -1;
}
int main () {
    int t;
    scanf("%d", &t);
    for (int lo = 1; lo <= t; lo++) {
        printf("Case #%d: ", lo);
        scanf("%d %d", &lin, &col);
        for (int c = 1; c <= lin; c++) {
            for (int g = 1; g <= col; g++) {
                scanf("%d", &v[c][g]);
            }
        }
        for (int t = 0; t < 2; t++) {
            for (int c = 1; c <= max(lin, col); c++) {
                for (int g = 1; g <= 100; g++) {
                    pd[t][c][g] = -1;
                }
            }
        }
        bool res = true;
        for (int c = 1; c <= lin; c++) {
            for (int g = 1; g <= col; g++) {
                if (!func(0, c, v[c][g]) && !func(1, g, v[c][g])) res = false;
            }
        }
        if (res) printf("YES");
        else printf("NO");
        printf("\n");
    }
    return 0;
}
