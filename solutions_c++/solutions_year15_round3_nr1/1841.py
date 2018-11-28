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
    int c, c2, cnt, i, j, n, r, t, w;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> r; cin >> c; cin >> w;
        c2 = c / w; if (c % w) c2++;
        n = r * c2; n += (w - 1);
        cout << "Case #" << cnt << ": " << n << endl;
    }
    return 0;
}
