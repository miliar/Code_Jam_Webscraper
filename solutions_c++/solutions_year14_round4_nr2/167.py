#include <stdio.h>
int n, cas, inp[1010], l, r, mi, mv, ans;
int main() {
    scanf("%d", &cas);
    for (int ii=0; ii<cas; ii++) {
        scanf("%d", &n);
        for (int i=0; i<n; i++) scanf("%d", &inp[i]);
        l = 0;
        r = n;
        ans = 0;
        while (l < r) {
            mv = 2147483647;
            for (int i=l ; i<r; i++) {
                if (inp[i] < mv) {
                    mv = inp[i];
                    mi = i;
                }
            }
            if (mi - l <= r-1-mi) {
                ans += mi - l;
                for (int i=mi; i>l; i--) inp[i] = inp[i-1];
                l = l+1;
            } else {
                ans += r-1-mi;
                for (int i=mi; i<r-1; i++) inp[i] = inp[i+1];
                r = r-1;
            }
        }
        printf("Case #%d: %d\n", ii+1, ans);
    }
    return 0;
}