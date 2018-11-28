#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
    FILE *fin = fopen("B-large.in", "r");
    FILE* fout = fopen("b-out.txt", "w");
    int T;
    fscanf(fin, "%d", &T);
    for (int i=1; i<=T; i++) {
        double C, F, X;
        fscanf(fin, "%lf %lf %lf", &C, &F, &X);
        double ans = 1e99;
        double rate = 2.0;
        double elapsed = 0.0;
        while (true) {
            if (elapsed + X/rate <= ans)
                ans = elapsed + X/rate;
            else
                break;
            elapsed += C/rate;
            rate += F;
        }
        fprintf(fout, "Case #%d: %.8f\n", i, ans);
    }
    return 0;
}
