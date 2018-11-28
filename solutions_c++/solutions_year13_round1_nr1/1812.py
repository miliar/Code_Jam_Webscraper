#include <stdio.h>
typedef long long ll;

int main () {
    int nteste;
    scanf ("%d", &nteste);
    for (int teste = 0; teste < nteste; teste++) {
        ll t, r;
        scanf ("%lld %lld", &r, &t);
        ll ret = 0;
        while (1) {
            ll aux = ((r + 1)*(r + 1) - r*r);
            if (t < aux)
                break;
            t -= aux;
            r += 2;
            ret++;
        }
        printf ("Case #%d: %lld\n", teste + 1, ret);
    }
    return 0;
}
