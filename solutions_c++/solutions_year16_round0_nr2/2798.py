#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        string s;
        cin >> s;
        int res = 0;
        while (true)
        {
            bool b = true;
            for (int i = 0; i < s.size(); i++) if (s[i] == '-') {b = false; break;}
            if (b) break;
            if (s[0] == '+')
            {
                int c = 0;
                while (s[c] == '+') s[c++] = '-';
            }
            else
            {
                int lm = s.size() - 1;
                while (s[lm] != '-') lm--;
                reverse(s.begin(), s.begin() + lm + 1);
                for (int i = 0; i <= lm; i++)
                    if (s[i] == '+') s[i] = '-';
                    else s[i] = '+';
            }
            res++;
        }
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
