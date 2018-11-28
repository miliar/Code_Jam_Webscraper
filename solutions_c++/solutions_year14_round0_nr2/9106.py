#include <cstdio>

int main()
{
    FILE *arq;
    arq=fopen("B-large.in", "r");

    int n_teste, ind=1;
    fscanf(arq, "%d", &n_teste);
    while(ind<=n_teste)
    {
        double c, f, x;
        fscanf(arq, "%lf %lf %lf", &c, &f, &x);

        double t_total=0;
        double c_per_sec=2;
        while(x/c_per_sec>=c/c_per_sec+x/(c_per_sec+f))
        {
            t_total+=c/c_per_sec;
            c_per_sec+=f;
        }
        t_total+=x/c_per_sec;

        printf("Case #%d: %.7lf\n", ind++, t_total);
    }

    return 0;
}
