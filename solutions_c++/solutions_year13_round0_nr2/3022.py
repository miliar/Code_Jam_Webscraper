#include <stdio.h>
#include <string.h>

int t, m, n;
int hc[128][128];
int sc[128][128];
int hm[128], sm[128];

int main()
{
    int tmp;

    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d %d", &n, &m);
        memset(hc, 0, sizeof(hc));
        memset(sc, 0, sizeof(sc));
        memset(hm, 0, sizeof(hm));
        memset(sm, 0, sizeof(sm));
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < m; k++) {
                scanf("%d", &tmp);
                hc[j][tmp]++;
                sc[k][tmp]++;
                hm[j] = (hm[j] > tmp)? hm[j]: tmp;
                sm[k] = (sm[k] > tmp)? sm[k]: tmp;
            }
        }
        int remove = 0;
        for (int j = 0; j < n; j++) {
            remove += hc[j][hm[j]];
        }
        for (int k = 0; k < m; k++) {
            remove += sc[k][sm[k]];
        }
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < m; k++) {
                if (hm[j] == sm[k]) remove--;
            }
        }
        if (remove >= n * m) {
            printf("Case #%d: YES\n", i);
        }
        else {
            printf("Case #%d: NO\n", i);
        }
    }

    return 0;
}
