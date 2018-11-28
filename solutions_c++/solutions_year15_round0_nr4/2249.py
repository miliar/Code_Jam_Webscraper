#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define BARSUK_ALEXEY_PSKOV

int tests;

int main()
{
#ifdef BARSUK_ALEXEY_PSKOV
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        int x, c, r;
        cin >> x >> c >> r;
        if (c > r) swap(c, r);
        string winner = "GABRIEL";
        if (x == 2) {
            if ((c * r) % 2 == 1)
                winner = "RICHARD";
        }
        else if (x == 3) {
            if (c == 1)
                winner = "RICHARD";
            if (c == 2 && r < 3)
                winner = "RICHARD";
            if (c == 2 && r == 4)
                winner = "RICHARD";
            if (c == 4)
                winner = "RICHARD";
        }
        else if (x == 4) {
            if (c == 1)
                winner = "RICHARD";
            if (c == 2)
                winner = "RICHARD";
            if (c == 3 && r < 4)
                winner = "RICHARD";
        }

        cout << "Case #" << t << ": " << winner << endl;
    }

    return 0;
}

