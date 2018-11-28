#include <iostream>

using namespace std;

double T, C, F, X;
double const D = 2.0;

int solve(int n, double C, double F, double X) {
    int N = 1;
    double top = X/D;
    double ans = top;
    double main = 0.0;
    double added = 0.0;
    while(true) {
        top = X/(D+N*F);
        added = C/(D+(N-1)*F);
        if(ans > main + added + top) {
            ans = main + added + top;
        } else {
            break;
        }
        N++;
        main = main + added;
    }

    printf("Case #%d: %.7f\n", n+1, ans);
    return 0;
}

int main() {
    cin >> T;
    for(int i = 0; i < T; i++) {
        cin >> C >> F >> X;
        solve(i, C, F, X);
    }
    return 0;
}
