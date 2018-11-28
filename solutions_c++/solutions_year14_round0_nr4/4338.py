#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 1111;
double a[MAXN], b[MAXN];
bool used[MAXN], used2[MAXN];
int main() {
    int cases;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &a[i]);
        }
        for (int i = 0; i < n; i++) {
            scanf("%lf", &b[i]);
        }
        sort(a, a + n);
        sort(b, b + n);
        printf("Case #%d: ", T);
        memset(used, 0, sizeof(used));
        int war = 0;
        for (int i = 0; i < n; i++) {
            //int p = upper_bound(b, b + n, a[i]) - b;
            int p = -1;
            for (int j = 0; j < n; j++) {
                if (b[j] > a[i] && !used[j]) {
                    p = j;
                    break;
                }
            }
            if (p == -1) {
                war++;
            } else {
                used[p] = true;
            }
        }

        memset(used, 0, sizeof(used));
        memset(used2, 0, sizeof(used2));
        int deceitfulWar = 0;
        //int nn = n;
        int j = 0;
        for (int i = 0; i < n; i++) {
            //if (a[i] >= b[0]) break;
            if (a[i] < b[j]) {
                //used2[--nn] = true;
                //used[i] = true;
            } else {
                //used[i] = true;
                //used[j++] = true;
                j++;
                deceitfulWar++;
            }
        }
        // int j = 0;
        // for (int i = 0; i < n && j < n; i++) {
        //     if (used[i]) continue;
        //     if (a[i] > b[j]) {
        //         deceitfulWar++;
        //         j++;
        //     } else {
        //         break;
        //     }
        // }
        // for (int i = 0; i < n; i++) {
        //     printf("%.3lf ", a[i]);
        // }
        // puts("");
        // for (int i = 0; i < n; i++) {
        //     printf("%.3lf ", b[i]);
        // }
        // puts("");
        printf("%d %d\n", deceitfulWar, war);
    }
}