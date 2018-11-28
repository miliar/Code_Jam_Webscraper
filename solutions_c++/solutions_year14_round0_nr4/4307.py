#include "stdio.h"
#include <algorithm>

int main() {
    int t;
    scanf("%i", &t);
    for (int ti=1; ti<=t; ti++) {
        int n;
        scanf("%i", &n);
        double x[n], y[n];
        for (int i=0; i<n; i++)
            scanf("%lf", x+i);
        for (int i=0; i<n; i++)
            scanf("%lf", y+i);
        std::sort(x, x+n);
        std::sort(y, y+n);
        int xi=0, yi=0, deceitScore=0;

        do {
            if (x[xi] < y[yi])
                xi++;
            else {
                xi++;
                yi++;
                deceitScore++;
            }
        } while (xi < n);

        int normalScore = n;
        xi=yi=0;
        do {
            if (y[yi] < x[xi])
                yi++;
            else {
                xi++;
                yi++;
                normalScore--;
            }
        } while (yi < n);
        printf("Case #%i: %i %i\n", ti, deceitScore, normalScore);
    }
    return 0;
}
