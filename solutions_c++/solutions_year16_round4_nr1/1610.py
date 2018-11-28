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
    bool tie;
    int cnt, i, i1, j, n, n2, n3, nn, p, p1, r, r1, s, s1, t;
    string res, res0, res1, res2;
    vector <int> x;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> n; cin >> r; cin >> p; cin >> s;

        res = "IMPOSSIBLE";
        n2 = 1; for (i = 0; i < n; i++) n2 *= 2;
        n3 = 1; for (i = 0; i < n2; i++) n3 *= 3;
        x.resize(n2);

        //n2 players
        //n3 possible combinations
        for (i = 0; i < n3; i++)
        {
            //n2
            i1 = i;
            for (j = 0; j < n2; j++)
            {
                x[j] = i1 % 3;
                i1 /= 3;
            }
            p1 = 0; r1 = 0; s1 = 0;
            for (j = 0; j < n2; j++)
            {
                if (!x[j]) p1++;
                if (x[j] == 1) r1++;
                if (x[j] == 2) s1++;
            }
            //x[0] = right, x[n] = left
            if ((p == p1) && (r == r1) && (s == s1))
            {
                res0 = "";
                for (j = n2 - 1; j >= 0; j--)
                {
                    if (!x[j]) res0 += "P";
                    if (x[j] == 1) res0 += "R";
                    if (x[j] == 2) res0 += "S";
                }
                //cout << res0 << endl;
                nn = res0.length(); tie = false;
                res2 = res0;
                while ((nn > 1) && (!tie))
                {
                    res1 = "";
                    for (j = 0; j < nn; j += 2)
                    {
                        if ((res2[j] == 'P') && (res2[j + 1] == 'P')) tie = true;
                        if ((res2[j] == 'P') && (res2[j + 1] == 'R')) res1 += "P";
                        if ((res2[j] == 'P') && (res2[j + 1] == 'S')) res1 += "S";
                        if ((res2[j] == 'R') && (res2[j + 1] == 'P')) res1 += "P";
                        if ((res2[j] == 'R') && (res2[j + 1] == 'R')) tie = true;
                        if ((res2[j] == 'R') && (res2[j + 1] == 'S')) res1 += "R";
                        if ((res2[j] == 'S') && (res2[j + 1] == 'P')) res1 += "S";
                        if ((res2[j] == 'S') && (res2[j + 1] == 'R')) res1 += "R";
                        if ((res2[j] == 'S') && (res2[j + 1] == 'S')) tie = true;
                        if (tie) break;
                    }
                    if (!tie)
                    {
                        //cout << res1 << endl;
                        res2 = res1; nn /= 2;
                    }
                }
                //cout << nn << endl;
                if (nn == 1) { res = res0; break; }
            }
        }

        //display results
        cout << "Case #" << cnt << ": " << res << endl;
    }
    return 0;
}
