#include <cstdio>
#include <algorithm>
#include <limits>
#include <cmath>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int _t = 1; _t <= T; _t++) {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        double rate = 2;
        double answer = numeric_limits<double>::infinity();
        double elapsed = 0;
        double prev_answer = 0;
        int times = 0;
        while (abs(prev_answer - answer) > 1e-15) {
            prev_answer = answer;
            // もう買わない
            answer = min(answer, elapsed + X / rate);
            // 買う
            elapsed += C / rate;
            rate += F;
            times++;
        }
        //printf("%d\n", times);
        printf("Case #%d: %.14f\n", _t, answer);
    }
}
