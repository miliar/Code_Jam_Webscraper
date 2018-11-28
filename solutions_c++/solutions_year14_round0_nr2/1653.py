#include <cstdio>
#include <cstring>

int main()
{
    FILE *fp = fopen("B-large.in", "r");
    FILE *fo = fopen("output.out", "w");
    //FILE *fp = stdin;
    //FILE *fo = stdout;
    int t;
    double c, f, x;
    fscanf(fp, "%d", &t);
    double time = 0;
    for (int i = 1; i <= t; i++)
    {
        time = 0;
        fscanf(fp, "%lf%lf%lf", &c, &f, &x);
        double nowv = 2;
        while (1)
        {
            if ((x-c)/nowv <= x/(nowv+f))
            {
                time += x / nowv;
                break;
            }
            else
            {
                time += c / nowv;
                nowv += f;
            }
        }
        fprintf(fo, "Case #%d: %.7lf\n", i, time);
    }
    return 0;
}
