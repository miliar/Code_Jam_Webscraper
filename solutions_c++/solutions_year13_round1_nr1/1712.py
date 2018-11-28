#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
typedef long long int llint;

double space(llint r)
{
    return ( (r + 1)*(r + 1) - r*r );
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T; cin >> T;
    for (int tt = 0; tt < T; ++tt)
    {
        llint r;
        double t;
        cin >> r >> t;

        llint count = 0;
        while (t > 0)
        {
            t -= space( r );
            r += 2;
            ++count;
        }

        if (t < 0)
            --count;

        printf("Case #%d: %lld\n", tt + 1, count);
    }

    fclose(stdout);
    return 0;
}
