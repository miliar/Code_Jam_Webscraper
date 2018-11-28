#include <iostream>
#include <stdio.h>
#define min(x,y) (x<y?x:y)

using namespace std;
double c, f, x, mini, r, a;

void sol()
{
    a=0;
    r=2;
    mini=x/r*1.0;
    for (;;)
    {
        a=a+c/r*1.0;
        r+=f;
        if (a+x/r*1.0<mini)
            mini=a+x/r*1.0;
        else
            break;
    }
    printf("%.7lf", mini);
}

int main()
{
    freopen("cookie.in", "r", stdin);
    freopen("cookie.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int r=1; r<=T; r++)
    {
        printf("Case #%d: ", r);
        scanf("%lf %lf %lf", &c, &f, &x);
        sol();
        printf("\n");
    }
    return 0;
}
