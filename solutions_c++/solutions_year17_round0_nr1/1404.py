#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
#ifdef ONPC
    freopen("lurge.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int k;
        string s;
        cin >> s >> k;
        int n = s.size();
        bool good = true;
        int ans = 0;
        for (int i = 0; i < (int) s.size(); i++)
        {
            if (s[i] == '-')
            {
                if (i + k - 1 >= (int) s.size())
                {
                    good = false;
                    break;
                }
                else
                {
                    for (int j = i; j < i + k; j++)
                    {
                        s[j] = (s[j] == '+' ? '-' : '+');
                    }
                    ans++;
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (good)
        {
            cout << ans << '\n';
        }
        else
        {
            cout << "IMPOSSIBLE\n";
        }
    }
}
