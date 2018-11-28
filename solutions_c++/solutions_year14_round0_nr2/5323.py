#include <stdio.h>

int cases, kejs;
double C, F, X, prod, total;

int main() {
    scanf("%d", &cases);
    for (kejs = 1; kejs <= cases; kejs++) {
        printf("Case #%d: ", kejs);
        scanf("%lf%lf%lf", &C, &F, &X);
				prod = 2; total = 0;
				while (true) {
					double tobuy = C / prod;
					double neednow = X / prod;
					double needafter = tobuy + X / (prod + F);
					if (neednow > needafter) {
						total += tobuy;
						prod += F;
					} else {
						total += neednow;
						break;
					}
				}
        printf("%.8lf\n", total);
    }
    return 0;
}
