#include <cstdio>

double solve(double c, double f, double x)
{
    double curTime = 0.0;
    double cps = 2.0;
    double nextFarm = c / cps;
    double nextFarmAndX = nextFarm + x / (cps + f);
    double nextX = x / cps;

    while (nextFarmAndX < nextX)
    {
        curTime += nextFarm;
        cps += f;
        nextFarm = c / cps;
        nextFarmAndX = nextFarm + x / (cps + f);
        nextX = x / cps;
    }

    return curTime + nextX;
}

int main()
{
    FILE *fin = fopen("B-large.in", "r");
    FILE *fout = fopen("B-large.out", "w");

    int t;
    double c, f, x;

    fscanf(fin, "%d", &t);

    for (int i = 1; i <= t; i++)
    {
        fscanf(fin, "%lf %lf %lf", &c, &f, &x);
        fprintf(fout, "Case #%d: %.7f\n", i, solve(c, f, x));
    }
    return 0;
}
