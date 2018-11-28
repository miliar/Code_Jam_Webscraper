#include <stdio.h>

main()
{
    int t, cases;
    double c, f, x, i, temp, ans, ans2;
    scanf("%d", &cases);
    for(t=1; t<=cases; t++)
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        ans = x / 2;
        temp = 0;
        i = 0;
        while(1)
        {
            i++;
            temp += c / (2 + (i - 1) * f);
            ans2 = temp + x / (2 + i * f);
            if(ans2 < ans) ans = ans2;
            else break;
        }
        printf("Case #%d: %.7lf\n", t, ans);
    }
}
