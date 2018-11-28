#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>

using namespace std;

int pp_max = 0;

int f(int d, vector <int> p, int step) {
    if (step > pp_max) return pp_max * 1000;
    int f_min, i, max = -1, min = 2147483647, p_max = -1;
    for (i = 0; i < d; i++) {
        if (p[i] > max) { max = p[i]; p_max = i; }
    }
    if (!max) return 0;
    vector <int> p1, p2; p1.resize(d); p2.resize(d + 1); p2[d] = 0;
    for (i = 0; i < d; i++) { p1[i] = (p[i] ? p[i] - 1 : 0); p2[i] = p[i]; }
    min = f(d, p1, step + 1) + 1;
    for (i = 0; i < max / 2; i++) {
        p2[p_max]--; p2[d]++; f_min = f(d + 1, p2, step + 1) + 1;
        if (f_min < min) min = f_min;
    }
    return min;
}

int main()
{
    int cnt, d, i, j, res, t;
    vector <int> p;
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> d; pp_max = 0;
        p.resize(d); for (i = 0; i < d; i++) { cin >> p[i]; if (p[i] > pp_max) pp_max = p[i]; }

        res = f(d, p, 0);

        //display results
        cout << "Case #" << cnt << ": " << res << endl;
    }
    return 0;
}
