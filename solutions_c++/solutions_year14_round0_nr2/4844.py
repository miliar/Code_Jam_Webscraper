#include <stdio.h>

int main()
{
    double c, x, f, ti, cook, br;
    int test;

    freopen("test.in", "r", stdin);
    freopen("cookie.out", "w", stdout);

    scanf("%d",&test);

    for(int t=1;t<=test;t++)
    {
        c = 0; f = 0; x = 0;
        ti = 0; cook = 2; br = 1;

        scanf("%lf",&c);
        scanf("%lf",&f);
        scanf("%lf",&x);

        while(br)
        {
            if((x/cook) < (c/cook + x/(cook+f)))
            {
                ti += x/cook;
                br = 0;
            }
            else
            {
                ti += c/cook;
                cook += f;
            }
        }
        printf("Case #%d: %lf\n",t,ti);
    }
    return 0;
}
