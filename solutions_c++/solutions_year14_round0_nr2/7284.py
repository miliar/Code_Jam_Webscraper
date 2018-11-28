#include <iostream>
#include <cstdio>

using namespace std;

int N;

int main()
{
    FILE *fin = fopen("a.in", "r");
    FILE *fout = fopen("a.out", "w+");
    fscanf(fin, "%d", &N);
    for(int i=0; i<N; i++){
        double C, F, X, t = 0, r = 1;
        fscanf(fin, "%lf %lf %lf", &C, &F, &X);
        C /= 2;
        F /= 2;
        X /= 2;
        while((X/r) > ((C/r) + (X/(r+F)))){
            t += (C/r);
            r += F;
        }
        t += (X/(r));
        fprintf(fout, "Case #%d: %lf\n", i+1, t);
    }
    return 0;
}
