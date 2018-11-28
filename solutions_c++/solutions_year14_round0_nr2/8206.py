#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int t,r;
    double c,f,x,time,inc,t1,t2;
    cin >> t;
    r = 1;
    while (t--) {
        time = 0.0;
        inc = 2.0;
        t1 = 0;
        t2 = 0;
        cin >> c;
        cin >> f;
        cin >> x;
        if (x <= c) {
            time = x / 2;
        }
        else {
                time = x/ inc;
        while (1) {
            t1 = t1 + (c / inc);
            inc = inc + f;
            t2 = x / inc;
            if (t1 + t2 < time)
                time = t1 + t2;
            else
                break;
        }
        }
        printf("Case #%d: %.7lf\n", r, time);
        r++;
    }

    return 0;
}
