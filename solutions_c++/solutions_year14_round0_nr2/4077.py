#include <cstdio>

int main(int argc, char *argv[]) {
    FILE *in = fopen("QualBLarge.in", "r");
    FILE *out = fopen("QualBLarge.out", "w");

    int T;
    fscanf(in, "%d", &T);

    int testCase;
    for (testCase = 1; testCase <= T; testCase++) {
        double C, F, X;
        fscanf(in, "%lf %lf %lf", &C, &F, &X);

        double cookieRate = 2.0f;
        double timePassed = 0.0f;
        double timeUntilFactory = C / cookieRate;
        double timeUntilFactoryWin = timeUntilFactory + (X / (cookieRate + F));
        double timeUntilWin = X / cookieRate;
        while (timeUntilFactoryWin < timeUntilWin) {
            cookieRate += F;
            timePassed += timeUntilFactory;

            timeUntilFactory = C / cookieRate;
            timeUntilFactoryWin = timeUntilFactory + (X / (cookieRate + F));
            timeUntilWin = X / cookieRate;
        }

        timePassed += timeUntilWin;
        fprintf(out, "Case #%d: %f\n", testCase, timePassed);
    }

    fclose(in);
    fclose(out);

    return 0;
}