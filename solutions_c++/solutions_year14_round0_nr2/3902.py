#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int test, i, cs = 1;
    double mn, ft, temp, C, F, X;

    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    cin>>test;
    while(test--)
    {
        cin>>C>>F>>X;
        //printf("%lf %lf %lf\n", C, F, X);
        i = 0;
        mn = X/2.0;
        ft = C / (2.0 + i * F);
        temp = ft + X/(2.0 + (i+1) * F);
        //printf("ft: %lf, temp: %lf, mn: %lf\n", ft, temp, mn);
        while(temp < mn)
        {
            mn = temp;
            i++;
            ft = ft + C / (2.0 + i * F);
            temp = ft + X/(2.0 + (i+1) * F);

            //printf("temp: %lf, mn: %lf\n", temp, mn);
        }
        printf("Case #%d: %.7lf\n", cs++, mn);
    }
    return 0;
}
