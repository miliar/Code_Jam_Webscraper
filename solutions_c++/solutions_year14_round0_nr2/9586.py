#include <cstdio>

#define min(a,b)    ((a)<(b)?(a):(b))

double c, f, x;

double calc(double c_per_sec)
{
    if(x/c_per_sec<=c/c_per_sec+x/(c_per_sec+f))   return x/c_per_sec;

    double compro, n_compro;
    compro=calc(c_per_sec+f)+c/c_per_sec;
    n_compro=x/c_per_sec;

    return min(compro, n_compro);
}

int main()
{
    FILE *arq;    arq=fopen("B-small-attempt1.in", "r");

    int n_teste, ind=1;
    fscanf(arq, "%d", &n_teste);
    while(ind<=n_teste)
    {
        fscanf(arq, "%lf %lf %lf", &c, &f, &x);

        printf("Case #%d: %.7lf\n", ind++, calc(2));
    }

    return 0;
}
