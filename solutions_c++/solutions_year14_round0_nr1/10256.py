#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    int a[4][4];
    int b[2][4];

    int t, c, n1, i, j, r, n;
    scanf("%d", &t);

    n = 1;
    while (t--) {
        scanf("%d", &n1);
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                scanf("%d", &a[i][j]);
                if ((i + 1) == n1) {
                    b[0][j] = a[i][j];
                }
            }
        }
        scanf("%d", &n1);
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                scanf("%d", &a[i][j]);
                if ((i + 1) == n1) {
                    b[1][j] = a[i][j];
                }
            }
        }

        c = 0;
        r = 0;
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                if (b[0][i] == b[1][j]) {
                    c++;
                    r = b[0][i];
                    break;
                }
            }
        }

        if (c == 1)
            printf("Case #%d: %d\n", n, r);
        else if (c == 0)
            printf("Case #%d: Volunteer cheated!\n", n);
        else
            printf("Case #%d: Bad magician!\n", n);
        n++;
    }

    return 0;
}
