#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main ()
{
    int cases; cin >> cases;

    for (int cas = 1; cas <= cases; ++cas)
    {
        double C, F, X, r=2, t=0;
        cin >> C >> F >> X;

        while (true)
        {
            // C/F is time until farm pays itself off
            // (X-C)/r is time remaining at time of choice
            if (C/F < (X-C)/r)
            {
                t += C/r;
                r += F;
            }
            else
            {
                t += X/r;
                break;
            }
        }

        printf("Case #%d: %.7f", cas, t);
        cout << endl;
    }

    return 0;
}