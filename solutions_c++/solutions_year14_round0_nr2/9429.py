#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

FILE *in = fopen("input.in", "r");
FILE *out = fopen("f.out", "w");

double C, F, X;

int main(){

    int ntest;
    fscanf(in, "%d", &ntest);
    for(int TEST = 1; TEST <= ntest; TEST++){
        fscanf(in, "%lf %lf %lf", &C, &F, &X);
        double ans = X / 2, offset = 0;
        for(int q = 1; q <= 50000; q++){
            offset += C / (2 + (q - 1) * F);
            ans = min(ans, offset + X / (2 + q * F));
        }
        fprintf(out, "Case #%d: %lf\n", TEST, ans);
    }

    return 0;
}
