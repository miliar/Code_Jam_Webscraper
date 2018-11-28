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
    int cnt, c, r, t, x;
    string res;
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> x; cin >> r; cin >> c;

        // GABRIEL if can fill grid, RICHARD otherwise
        if (x == 1) res = "GABRIEL";
        if (x == 2) {
            if ((c * r) % 2) res = "RICHARD";
            else res = "GABRIEL";
        }
        if (x == 3) {
            res = "RICHARD";
            if ((r == 2) && (c == 3)) res = "GABRIEL";
            if ((r == 3) && (c == 2)) res = "GABRIEL";
            if ((r == 3) && (c == 3)) res = "GABRIEL";
            if ((r == 3) && (c == 4)) res = "GABRIEL";
            if ((r == 4) && (c == 3)) res = "GABRIEL";
        }
        if (x == 4) {
            res = "RICHARD";
            if ((r == 3) && (c == 4)) res = "GABRIEL";
            if ((r == 4) && (c == 3)) res = "GABRIEL";
            if ((r == 4) && (c == 4)) res = "GABRIEL";
        }

        //display results
        cout << "Case #" << cnt << ": " << res << endl;
    }
    return 0;
}
