#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main () {
    int T;
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    scanf ("%d", &T);
    for (int j = 1; j <= T; j++) {
        int n = -1;
        double least = 999999999;
        double C, F, X;
        scanf ("%lf %lf %lf", &C, &F, &X);
        while (1) {
              double tim = 0.0;
              n++;
              for (int i = 1; i <= n; i++)
                  tim += C / (2.0+F*double(i-1));
              tim += X / (2.0+F*double(n));
              if (least > tim)
                 least = tim;
              else
                  break;
        }
        printf ("Case #%d: %.7lf\n", j, least);
    }
    return 0;
}
