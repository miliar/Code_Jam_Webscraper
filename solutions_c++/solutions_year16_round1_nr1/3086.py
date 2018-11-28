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
    char ch;
    int cnt, i, j, len, pos, t;
    string res, res_l, res_r, s;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> s;
        len = s.length();

        res = s[0];
        //cout << res << endl;

        for (i = 1; i < len; i++)
        {
            ch = res[0];
            if (s[i] < ch) res = res + s[i];
            if (s[i] > ch) res = s[i] + res;
            if (s[i] == ch)
            {
                res_l = s[i] + res;
                res_r = res + s[i];
                pos = 1;
                for (j = 0; j <= i; j++)
                {
                    if (res_l[j] < res_r[j]) { pos = 2; break; } // if left is smaller, choose right
                    if (res_l[j] > res_r[j]) { pos = 1; break; } // if right is smaller, choose left
                }
                if (pos == 1) res = res_l;
                if (pos == 2) res = res_r;
            }
            //cout << res << endl;
        }

        //display results
        cout << "Case #" << cnt << ": " << res << endl;
    }
    return 0;
}
