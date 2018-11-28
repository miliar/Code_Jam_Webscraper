#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

double c, f, x;
int T;

int main()
{
    scanf("%d", &T );
    for (int I = 1; I <= T; ++I )
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        double days = 0, minday = x / 2.0;
        double rate = 2.0;
        while ( true )
        {
            days += c / rate;
            rate += f;
            if ( days + x/rate < minday )
                minday = days + x / rate;
            else
                break;
        }
        printf( "Case #%d: %.7lf\n",I, minday);
    }
}
