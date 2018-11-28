#include <stdio.h>
#define FOR(i,n) for(int i = 0; i < (n); i++)

int numR, numC;
int grid[200][200];

bool isOk(int r, int c) {
    bool isBiggest = true;
    FOR(cr, numR) {
        if(grid[cr][c] > grid[r][c]) { isBiggest = false; break; }
    }
    if(isBiggest) return true;
    FOR(cc, numC) {
        if(grid[r][cc] > grid[r][c]) return false;
    }
    return true;
}

int main() {
    freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    int numT; scanf("%d", &numT);
    for(int cno = 1; cno <= numT; cno++) {
        scanf("%d %d", &numR, &numC);
        FOR(r, numR) FOR(c, numC) {
            scanf("%d", &grid[r][c]);
        }

        bool ok = true;
        FOR(r, numR) FOR(c, numC) {
            if(!isOk(r, c)) { ok = false; break; }
        }

        printf("Case #%d: ", cno);
        if(ok) printf("YES\n");
        else printf("NO\n");

    }
    return 0;
}

