#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int t;
int aaa=0;
double t1[2000];
double t2[2000];

int rendez(const void *a, const void *b)
{
    double aa=(*(double*)a)-(*(double*)b);
    if (aa<0) return -1;
    if (aa>0) return 1;
    return 0;
}

int main()
{
    FILE *in = fopen("d.in", "r");
    FILE *out = fopen("d.out", "w");
    fscanf(in, "%d", &t);

    while (t>0)
    {
        aaa++;
        int nyer1=0;
        int nyer2=0;
        int n;
        fscanf(in, "%d", &n);
        for (int i=1;i<=n;i++) fscanf(in, "%lf", &t1[i]);
        for (int i=1;i<=n;i++) fscanf(in, "%lf", &t2[i]);

        qsort(t1+1, n, sizeof(double), rendez);
        qsort(t2+1, n, sizeof(double), rendez);

        int a=1;
        int b=1;
        while (b<=n)
        {
            while (b<=n && t1[a]>t2[b]) b++;
            if (b<=n)
            {
                a++;
                b++;
            }
        }
        a--;
        nyer2=n-a;

        a=1;
        b=1;
        while (a<=n)
        {
            while (a<=n && t1[a]<t2[b]) a++;
            if (a<=n)
            {
                a++;
                b++;
            }
        }
        b--;
        nyer1=b;

        fprintf(out, "Case #%d: %d %d\n", aaa, nyer1, nyer2);

        t--;
    }
    fclose(out);
    return 0;
}
