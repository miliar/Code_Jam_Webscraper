#include <stdio.h>
#define infinity 1000000000.0

void SolveTestcase(int TestCase){
    double C, F, X;
    double bonus = 2.0;
    scanf("%lf%lf%lf", &C, &F, &X);

    double total_build_time = 0.0;
    double prev_time = infinity;
    double new_time = X/bonus;

    while (new_time < prev_time){
        prev_time = new_time;
        double build_time = C/bonus;
        total_build_time += build_time;
        bonus += F;
        double to_finish = X/bonus;
        new_time = total_build_time + to_finish;
    }

    printf("Case #%d: %.7f\n", TestCase, prev_time);
}

int main(){
    int T;
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; testcase++)
        SolveTestcase(testcase);
    fclose(stdin);
    fclose(stdout);
    return 0;
}
