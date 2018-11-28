# include <math.h>
# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define PN printf("\n")
# define PI 3.1415926536
# define MAXINT 0x7fffffff
# define GetMax(a, b) ((a)>(b)?(a):(b))
# define GetMin(a, b) ((a)<(b)?(a):(b))

# define MAXN 9

bool judge(double current, double c, double f, double x,double product)
{
    double a, b;
    a = (x - current)/product;
    b = (x - current + c)/(product + f);
    if(b < a)
        return true;
    return false;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t,  cnt = 1;
    double c, f, x, current, time, product;
    scanf("%d", &t);
    while(cnt <= t)
    {
        printf("Case #%d: ", cnt++);
        scanf("%lf %lf %lf", &c, &f, &x);
        if(x > c)
        {
            for(current = c, product = 2, time = c/2; current < x;)
            {
                if(judge(current, c, f, x, product))
                {
                    product += f;
                    time += c / product;
                }
                else
                {
                    printf("%.7lf\n", time + (x - current)/product);
                    break;
                }
            }
        }
        else
        {
            printf("%.7lf\n", x/2);
        }
    }
    return 0;
}
