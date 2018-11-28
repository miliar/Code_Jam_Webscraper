#include <iostream>
#include <cstdio>
using namespace std;

int t;
int aaa=0;
double c, f, x;

int main()
{
    FILE *in = fopen("b.in", "r");
    FILE *out = fopen("b.out", "w");
    fscanf(in, "%d", &t);

    while (t>0)
    {
        aaa++;

        fscanf(in, "%lf %lf %lf", &c, &f, &x);
        double prod=2;
        double timedone=0;
        double time=x/prod;

        while (time>c/prod+x/(prod+f))
        {
            timedone+=c/prod;
            prod+=f;
            time=x/prod;
        }

        fprintf(out, "Case #%d: %.10f\n", aaa, time+timedone);

        t--;
    }
    fclose(out);
    return 0;
}
