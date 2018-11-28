#include<cstdio>
#include<algorithm>
using namespace std;
double C,F,X,bes;
int sTT;
int main() {
    scanf("%d", &sTT);
    for (int TT = 1; TT <= sTT; ++TT) {
        printf("Case #%d: ", TT);
        scanf("%lf%lf%lf", &C, &F, &X);
        bes = X * 0.5;
        for (double tim = 0.0, rat = 2.0; tim < X; rat += F) {
            if (tim > bes) break;
            bes = min(bes, tim + X / rat);
            tim += C / rat;
        }
        printf("%.7lf\n", bes);
    }
    return 0;
}
