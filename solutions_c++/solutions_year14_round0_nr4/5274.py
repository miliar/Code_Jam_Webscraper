#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
    double nm[1001];
    double ken[1001];
    int test, n;
    int w;
    int dw;
    int i, j, k, l;

    scanf("%d", &test);

    for (l = 1; l <= test; l++) {
        scanf("%d", &n);
        for(i = 0; i < n; i++) {
            scanf("%lf", &nm[i]);
        }
        for(i = 0; i < n; i++) {
            scanf("%lf", &ken[i]);
        }
        sort(nm, nm + n);
        sort(ken, ken + n);

        w = 0;
        dw = 0;
        k = 0;
        // for war
        for (i = n-1, j = n-1; i >= 0; i--) {
            if (nm[i] > ken[j] && j >= k) {
                w++;
                k++;
            } else {
                j--;
            }
        }

        for (i = n-1, j = n-1; i >= 0; i--) {
            if (nm[i] < ken[0]) {
                break;
            }
            if (j < 0) {
                break;
            }
            if (nm[i] > ken[j]) {
                dw++;
                j--;
            } else {
                while (ken[j] > nm[i] && j >= 0) {
                    j--;
                }
                if (j >= 0) {
                    dw++;
                    j--;
                }
            }
        }

        printf("Case #%d: %d %d\n", l, dw, w);
    }
    return 0;
}
