#include <cstdio>
int main()
{
    int t;
    scanf("%d", &t);
    double ans, c, f, x, r, nu;
    for(int i = 1; i <= t; i++)
    {
       scanf("%lf%lf%lf", &c, &f, &x);
       r = 2.0;
       ans =  x/r;
       nu = 0.0;
       do
       {
           nu += c/r;
           r += f;
           if(nu + x / r < ans)
                ans = nu + x / r;
           else
                break;

       }while(1);
       printf("Case #%d: %.7lf\n", i, ans);
    }
    return 0;
}
