#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        string s;
        cin >> s;
        string best = "";
        best += s[0];
        for (int j = 1; j < s.size(); j++)
        {
            if (s[j] >= best[0])
                best = s[j] + best;
            else
                best += s[j];
        }
        cout << "Case #" << i << ": " << best << endl;
    }
    return 0;
}
