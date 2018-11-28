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
    int cnt, i, j, len, res, t;
    string s;
    vector <bool> p;
    vector <int> p0, p1;
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> s;
        len = s.length();

        p.resize(len);
        for (i = 0; i < len; i++) p[i] = ((s[i] == '+') ? true : false);

        p0.resize(len); p1.resize(len);
        p0[0] = (p[0] ? 1 : 0); p1[0] = (p[0] ? 0 : 1);
        for (i = 1; i < len; i++) {
            p0[i] = (p[i] ? p1[i - 1] + 1 : p0[i - 1]);
            p1[i] = (p[i] ? p1[i - 1] : p0[i - 1] + 1);
        }

        res = p1[len - 1];

        //display results
        cout << "Case #" << cnt << ": " << res << endl;
    }
    return 0;
}
