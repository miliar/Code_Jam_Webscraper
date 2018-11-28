#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int table[110][110];
int mark[110][110];

int main()
{
    int aa, nn, n, m, i, j, k;
    scanf("%d", &nn);
    for (aa = 1; aa <= nn; aa++) {
        scanf("%d %d",&n,&m);
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                scanf("%d", &table[i][j]);
            }
        }

        memset(mark, 0 , sizeof(mark));
        for (i = 0; i < n; i++) {
            for (j = 0, k = 0; j < m; j++) {
                k = (table[i][j] > k)? table[i][j] : k;
            }
            for (j = 0; k && j < m; j++) {
                if (table[i][j] == k) mark[i][j] |= 1;
            }
        }
        for (i = 0; i < m; i++) {
            for (j = 0, k = 0; j < n; j++) {
                k = (table[j][i] > k)? table[j][i] : k;
            }
            for (j = 0; k && j < n; j++) {
                if (table[j][i] == k) mark[j][i] |= 1;
            }
        }
        for (i = 0, k = 1; k && i < n; i++) {
            for (j = 0; k && j < m; j++) {
                k = mark[i][j];
            }
        }
        if (k) {
            printf("Case #%d: YES\n", aa);
        } else {
            printf("Case #%d: NO\n", aa);
        }
    }
    return 0;
}

