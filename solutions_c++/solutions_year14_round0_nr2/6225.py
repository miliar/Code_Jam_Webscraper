#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("answer.txt", "w", stdout);
    double c,f,x,tem;
    int t;
    double sum;
    scanf("%d", &t);
    for(int cns = 1; cns <= t; cns++)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        sum = 0;
        tem = 2;
        while(c*(tem+f)+x*tem < x*(tem+f))
        {
            sum += c/tem;
            tem += f;
        }
        sum += x/tem;
        printf("Case #%d: %.7lf\n", cns, sum);
    }
    return 0;
}
