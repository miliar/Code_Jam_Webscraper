#include <cstdio>
#include <math.h>

using namespace std;

double solve(double C, double F, double X) {
    if(C >= X) {
        return X / 2;
    }
    double L = (X-C) / X;
    double numberOfC = ceil((2 - L * 2 - L * F) / (F * (L - 1)));
    if(numberOfC < 0) {
        numberOfC = 0;
    }

    /*double numberOfC = 0; 
    while( (X / (2 + (numberOfC + 1) * F) + C / (2 + numberOfC * F) <= X / (2 + numberOfC * F)) ) {
        ++numberOfC;
    }*/

    double result = X / (2 + (numberOfC * F));
    for(int i = 0; i < numberOfC; ++i) {
        result += C / (2 + i * F);
    }

    return result;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) { 
        double C, F, X;
        scanf(" %lf", &C);
        scanf(" %lf", &F);
        scanf(" %lf", &X);

        double sol = solve(C, F, X);
        printf("Case #%d: %.7lf\n", t, sol);
    }

    return 0;
}
