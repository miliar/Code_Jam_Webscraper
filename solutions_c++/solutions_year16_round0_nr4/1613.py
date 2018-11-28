#include <bits/stdc++.h>

using namespace std;

int main (void) {
    int T;
    scanf ("%d", &T);
    for (int v = 1; v <= T; ++v) {
        printf ("Case #%d: ", v);
        long long int k, c, s;
        scanf ("%lld %lld %lld", &k, &c, &s);
        long long int tot = k;
        for (int x = 1; x < c; ++x) tot *= k;
        if (s < k) {
            // Hugh
            printf ("IMPOSSIBLE\n");
        } else {
            long long int b = tot/k;
            long long int k = 0;
            int t = 0;
            while (t != s) {
                printf ("%lld ", k+1);
                k += b;
                t++;
            }
            printf( "\n");
        }
    }
}
