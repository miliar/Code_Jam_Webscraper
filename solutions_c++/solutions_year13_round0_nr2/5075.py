#include <cstdio>
#include <cstring>

int field[105][105];
bool yes[105][105];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    int tc, nc;
    int r, c;
    int row, col;
    int min;
    int rm, cm;
    bool full;
    scanf("%d", &tc);
    for (nc=1;nc<=tc;nc++) {
        scanf("%d%d", &row, &col);
        for (r=0;r<row;r++) {
            for (c=0;c<col;c++) {
                scanf("%d", &field[r][c]);
                //printf("%d ", field[r][c]);
            }
            //printf("\n");
        }
        full = false;
        memset(yes, false, sizeof(yes));
        while (!full) {
            min = 1000;
            for (r=0;r<row;r++) {
                for (c=0;c<col;c++) {
                    if (min>field[r][c] && !yes[r][c]) {
                        min = field[r][c];
                        rm = r;
                        cm = c;
                    }
                }
            }
            //if (yes[1][3]) printf("y "); else printf("n ");
            //printf("%d %d ", rm, cm);
            if (min==1000) {
                full = true;
                continue;
            }
            for (r=0;r<row;r++) {
                if (field[r][cm]!=field[rm][cm] && !yes[r][cm])
                    break;
            }
            if (r==row) {
                for (r=0;r<row;r++) {
                    yes[r][cm] = true;
                }
                //printf("col\n");
                continue;
            }
            for (c=0;c<col;c++) {
                if (field[rm][c]!=field[rm][cm] && !yes[rm][c])
                    break;
            }
            if (c==col) {
                for (c=0;c<col;c++) {
                    yes[rm][c] = true;
                }
                //printf("row\n");
            }
            if (r!=row && c!=col) {
                break;
            }
        }
        printf("Case #%d: ", nc);
        if (full) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
}
