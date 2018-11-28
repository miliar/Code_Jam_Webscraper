#include <cstdio>

using namespace std;

int main(int argc, char *argv[]) {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        double rate = 2;
        double time = 0;
        while (X / rate > C / rate + X / (rate + F)) {
            time += C/rate;
            rate += F;
        }
        time += X / rate;
        printf("Case #%d: %.7lf\n", i+1, time);
    }
    return 0;
}
