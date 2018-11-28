#include<algorithm>
#include<cstdio>

using namespace std;

void solve(int testNr) {
    int h, w, y, x, r, c;
    scanf("%d%d", &h, &w);
    int M[100][100];
    for (y = 0; y < h; y++) {
        for (x = 0; x < w; x++) {
            scanf("%d", &M[y][x]);
        }
    }

    int rowMax[100], colMax[100];
    for (r = 0; r < h; r++) {
        rowMax[r] = M[r][0];
        for (c = 0; c < w; c++) {
            rowMax[r] = max(rowMax[r], M[r][c]);
        }
    }

    for (c = 0; c < w; c++) {
        colMax[c] = M[0][c];
        for (r = 0; r < h; r++) {
            colMax[c] = max(colMax[c], M[r][c]);
        }
    }

    for (c = 0; c < w; c++) {
        for (r = 0; r < h; r++) {
            if(M[r][c] < rowMax[r] && M[r][c] < colMax[c]) {
                printf("Case #%d: NO\n", testNr);
                return;
            }
        }
    }

    printf("Case #%d: YES\n", testNr);
}

int main() {
    int n;
    scanf("%d", &n);
    for(int t=1; t<=n; t++)
        solve(t);
    return 0;
}
