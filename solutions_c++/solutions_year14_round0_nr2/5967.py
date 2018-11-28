#include<cstdio>

int main()
{
    //freopen("A-small-attempt1.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    int T;
    double C, F, X, cost, init;
    scanf("%d", &T);
    FILE* p = fopen("out.txt", "a+");
    for(int casecnt = 1; casecnt <=T; ++casecnt)
    {
        scanf("%lf %lf %lf", &C, &F, &X);
        cost = 0.0;
        init = 2.0;
        while(X/init > C/init + X/(init+F))
        {
            cost += C/init;
            init += F;
        }
        cost += X/init;
        fprintf(p, "Case #%d: %.7lf\n", casecnt, cost);
    }
    fclose(p);
    return 0;
}