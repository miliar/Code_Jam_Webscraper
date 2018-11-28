#include<cstdio>

int main()
{
    int t;
    double c, f, x, w, odp, a;
    scanf("%d", &t);
    for(int g = 1; g <= t; g++)
    {
        w = 2;
        scanf("%lf%lf%lf", &c, &f, &x);
        odp = x/2;
        a = 0;
        while(odp > a + c/w + x/(w+f))
        {
            a = a + c/w;
            w = w + f;
            odp = a + x/w;
        }
        printf("Case #%d: %.7lf\n", g, odp);
    }
    return 0;
}
    
