#include <cstdio>

int main() {
    int T, TT;
    scanf("%d", &TT);
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        
        double speed = 2.0;
        double time = 0.0;
        while (X/speed > C/speed + X/(speed + F)) {
            time += C/speed;
            speed += F;
        }
        
        printf("%.8lf\n", time+X/speed);
    }
}    