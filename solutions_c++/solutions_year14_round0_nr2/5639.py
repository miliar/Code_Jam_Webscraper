#include <cstdio>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; ++t){
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);

        double L = (X - C)*F/C;
        double time = 0.0;
        double deno;
        for (deno=2.0; deno<L; deno+=F){
            time += C / deno;
        }
        time += X / deno;

        printf("Case #%d: %.7f\n", t,  time);
    }

    return 0;
}
