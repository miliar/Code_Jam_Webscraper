#include <stdio.h>
#include <algorithm>
int cas, n, inp[100100], s, a, b;
int main() {
    scanf("%d", &cas);
    for (int iii=0; iii<cas; iii++) {
        scanf("%d%d", &n, &s);
        for (int i=0; i<n; i++)scanf("%d", &inp[i]);
        std::sort(inp, inp+n);
        a = 0;
        b = 0;
        for (int i=n-1; i>=a; i--) {
            if (inp[i] + inp[a] <= s)  {
                a ++;
                b ++;
            } else {
                b++;
            }
        }
        printf("Case #%d: %d\n", iii+1, b);
    }
    return 0;
}