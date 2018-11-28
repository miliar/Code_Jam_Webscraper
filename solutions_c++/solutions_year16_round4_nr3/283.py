#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int t, kejs, i, n, j, k, m;

char a[18][18];
int v[320];
int R, C;
int dr[4] = {1, 0, -1, 0};// DLUR
int dc[4] = {0, -1, 0, 1};

int go(int f) {
        int i, r, c, d;
        if (f <= C) { r = 0; c = f; d = 0;}
        else if (f <= C+R) { r = f - C; c = C+1; d=1;}
        else if (f <= C+R+C) { r = R+1; c = C - (f - C - R) + 1; d=2;}
  else {r = R - (f-C-R-C)+1; c = 0; d=3;}
        for(;;) {
                r += dr[d]; c += dc[d];
                if (r == 0 || c == 0 || r == R+1 || c == C+1) break;
                if (a[r][c] == '/') {
                        if (d == 0) d = 1;
                        else if (d == 1) d = 0;
                        else if (d == 2) d = 3;
                        else d = 2;
                } else {
                        if (d == 0) d = 3;
                        else if (d == 1) d = 2;
                        else if (d == 2) d = 1;
                        else d = 0;
                }
        }
        if (r == 0) return c;
        if (c == C+1) return C + r;
        if (r == R+1) return C + R + C - c + 1;
        return C + R + C + R - r + 1;
}

int main() {
        scanf("%d", &t);

        for (kejs = 1; kejs <= t; kejs++) {
                                                                printf("Case #%d:\n", kejs);
                scanf("%d%d",&R, &C);
                                                                n = 2*(R+C);
                                                                for (i = 0; i < n; i++) scanf("%d",&v[i]);
                                                                for (m = 0; m < (1<<(R*C)); m++) {
                                                                        k = 0;
                                                                        for (i = 1; i <= R; i++) for (j = 1; j <= C; j++) {
                                                                                if (m & (1<<k)) a[i][j] = '\\'; else a[i][j] = '/';
                                                                                k++;
                                                                        }
                                                                        for (i = 0; i < n; i+=2) {
                                                                                if (go(v[i]) != v[i+1]) break;
                                                                        }
                                                                        if (i >= n) {
                                                                                for (i = 1; i <= R; i++) {
                                                                                        for (j = 1; j <= C; j++) {
                                                                                                printf("%c", a[i][j]);
                                                                                        }
                                                                                        printf("\n");
                                                                                }
                                                                                break;
                                                                        }
                                                                }
                                                                if (m >= (1<<(R*C))) printf("IMPOSSIBLE\n");
        }
        return 0;
}
