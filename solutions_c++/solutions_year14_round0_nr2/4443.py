#include<cstdio>

int main()
{
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;t++)
    {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        int n = (F*X - 2*C)/(F*C);
        double ans = X/2.0;
        if(n > 0)
        {
            double total = 0;
            double speed = 2;
            for(int i=1;i<=n;i++)
            {
                total += C/speed;
                speed += F;
            }
            ans = total + X/(2 + n*F);
        }
        printf("Case #%d: %.7lf\n", t, ans);
    }
    return 0;
}
