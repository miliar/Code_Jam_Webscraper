#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main () {
    int T;
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    scanf ("%d", &T);
    for (int j = 1; j <= T; j++) {
        int n, headn = 0, headk = 0, tailn, tailk;
        int y = 0, z = 0;
        double naomi[15], ken[15];
        scanf ("%d", &n);
        tailn = n-1;
        tailk = tailn;
        for (int i = 0; i < n; i++)
            scanf ("%lf", &naomi[i]);
        for (int i = 0; i < n; i++)
            scanf ("%lf", &ken[i]);
        sort (naomi, naomi+n);
        sort (ken, ken+n);
        while (headn <= tailn) {
              if (naomi[headn] > ken[headk]) {
                 headn++;
                 headk++;
                 y++;
                 continue;
              }
              if (naomi[headn] <= ken[headk]) {
                 headn++;
                 tailk--;
                 continue;
              }
              if (naomi[tailn] > ken[tailk]) {
                 tailn--;
                 tailk--;
                 y++;
                 continue;
              }
              if (naomi[tailn] <= ken[tailk]) {
                 headn++;
                 tailk--;
                 continue;
              }
        }
        int rem = n-1;
        for (int i = 0; i < n; i++) {
            int k, flag = 0;
            if (naomi[i] > ken[rem])
               continue;
            for (k = 0; k <= rem; k++)
                if (ken[k] > naomi[i]) {
                   flag = 1;
                   break;
                }
            if (flag == 0)
               continue;
            z++;
            ken[k] = -1;
            if (k == rem) {
               for (int l = rem; l >= 0; l--)
                   if (ken[l] != -1) {
                      rem = l;
                      break;
                   }
            }
        }
        printf ("Case #%d: %d %d\n", j, y, n-z);
    }
    return 0;
}
