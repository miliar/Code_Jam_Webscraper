#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("BB.out", "w", stdout);

    int t, casee = 0, n;
    string s;

    cin >> t;

    while (t--)
    {
        casee++;
        int res = 0;
        char p = '-';

        cin >> s;

        for (int i=s.length(); i >= 0; i--)
        {
            if (s[i] == p)
            {
                res++;
                if (p == '-') p = '+';
                else p = '-';
            }
        }

        cout << "Case #" << casee << ": " << res << endl;
    }
}
