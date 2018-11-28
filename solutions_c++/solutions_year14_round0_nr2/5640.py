#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
    double c, f, r, x, y, y0, y1;
    int cnt, i, j, n, t;
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> c; cin >> f; cin >> x;
        n = 0; r = 2.0; y = x / r; y0 = 0.0;
        while (1)
        {
            y0 += (c / r); n++; r += f;
            y1 = y0 + (x / r);
            if (y1 > y) break;
            y = y1;
        }
        printf("Case #%d: %.7f\n", cnt, y);
    }
    return 0;
}
