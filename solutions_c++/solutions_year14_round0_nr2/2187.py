#include <cstdio>

double times;
double build;
double c, f, x;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int CAS1;
    scanf("%d", &CAS1);
    for (int CAS=1; CAS<=CAS1; CAS++)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        times = 0.0;
        build = x/2.0;
        double ans = x/2.0;
        for (int i=1; 1; i++)
        {
            times = times + c/((i-1)*f+2);
            build = times + x/(i*f+2);
            if (ans>build)
                ans = build;
            else if (ans<times)
                break;
        }
        printf("Case #%d: %.7f\n", CAS, ans);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
