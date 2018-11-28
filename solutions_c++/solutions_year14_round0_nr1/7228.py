#include <stdio.h>

using namespace std;

int main() {
    freopen ("fin.in", "r", stdin);
    freopen ("fout.out", "w", stdout);
    int N, i, j, ok[17], x, row, count, val;
    scanf ("%d", &N);
    for (int caz = 1; caz <= N; ++caz) {
        for (i = 1; i <= 16; ++i) ok[i] = 0;
        scanf ("%d", &row);
        for (i = 1; i <= 4; ++i)
            for (j = 1; j <= 4; ++j) {
                scanf ("%d", &x);
                if (i == row) ok[x] = 1;
            }
        scanf ("%d", &row);
        for (i = 1; i <= 4; ++i)
            for (j = 1; j <= 4; ++j) {
                scanf ("%d", &x);
                if (i == row) ++ok[x];
            }
        count = 0;
        for (i = 1; i <= 16; ++i)
            if (ok[i] == 2) ++count, val = i;
        if (!count) printf ("Case #%d: Volunteer cheated!\n", caz);
        if (count == 1) printf ("Case #%d: %d\n", caz, val);
        if (count > 1) printf ("Case #%d: Bad magician!\n", caz);
    }
    return 0;
}
