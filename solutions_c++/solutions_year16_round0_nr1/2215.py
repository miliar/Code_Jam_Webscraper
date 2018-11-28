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
    int cnt, i, j, n, nn, nn1, res, t, x1;
    vector <bool> x;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin >> t;
    x.resize(10);
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> n;

        if (!n) cout << "Case #" << cnt << ": INSOMNIA" << endl;
        else
        {
            res = n;
            for (i = 0; i < 10; i++) x[i] = false;

            nn = 0;
            while (true) {
                nn += n;
                nn1 = nn;
                while (nn1) {
                    x[nn1 % 10] = true;
                    nn1 /= 10;
                }
                x1 = 0;
                for (i = 0; i < 10; i++) if (x[i]) x1++;
                if (x1 == 10) {
                    res = nn;
                    break;
                }
            }

            //display results
            cout << "Case #" << cnt << ": " << res << endl;
        }
    }
    return 0;
}
