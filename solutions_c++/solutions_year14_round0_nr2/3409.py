#include<iostream>
#include<stdio.h>
#include <iomanip>

using namespace std;

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    int T, n;
    double C, F, X, TotCookie, val, FirmTime, ReachTime,time;

    cin >> T;
    n = 1;
    while(n<=T)
    {
        cin >> C >> F >> X;

        TotCookie = 2.0;
        val = X/2;
        FirmTime = 0;
        while(1)
        {
            FirmTime += C/TotCookie;
            TotCookie += F;

            ReachTime = X/TotCookie;
            time = FirmTime + ReachTime;

            if(val <= time)
            {
                cout << fixed;
                cout << "Case #" << n << ": " << setprecision(7) << val << endl;
                break;
            }
            else
            {
                val = time;
            }
        }
        n++;
    }
    return 0;
}
