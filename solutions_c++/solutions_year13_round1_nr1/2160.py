#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    int T;
    long long int r, t;
    long long int sup, inf, med;

    scanf("%d", &T);

    for (int i=1; i<=T; i++)
    {
        cin >> r >> t;
        inf = 1;
        if (r>1000000000)
            sup = 1000000000000000000/r;
        else
            sup = 1000000000;

        while (sup-inf > 1)
        {
            med = (sup+inf)/2;
            if (2*med*med + 2*r*med - med < t)
                inf = med;
            else if (2*med*med + 2*r*med - med > t)
                sup = med;
            else
            {
                inf = med;
                break;
            }
        }

        printf("Case #%d: %lld\n", i, inf);
    }

    return(0);
}
