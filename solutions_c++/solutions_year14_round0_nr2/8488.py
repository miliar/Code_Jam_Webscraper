#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

double C, F, X;
typedef long double FF;
FF best;

int main() {
    int T; scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        
        scanf("%lf%lf%lf", &C, &F, &X);
        FF speed = 2.0f; // cookies per second
        FF timeUsed = 0;
        best = X / speed;
        while (timeUsed < best) {
            FF dt = C / speed;
            timeUsed += dt;
            speed += F;
            best = min(best, timeUsed + X / speed);
        }
        
        printf("Case #%d: %.9lf\n", t, (double)best);
    }
    
    return 0;
}
