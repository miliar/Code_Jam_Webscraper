#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n, x;
    string s;
    cin >> n;
    for (int tc=1; tc<=n; tc++)
    {
        cin >> x >> s;
        int dePie = 0, ans = 0;
        for (int i=0; i<=x; i++)
        {
            if (s[i] == '0') continue;
            int val = s[i] - char('0');
            if (i > dePie)
            {
                ans += (i - dePie);
                dePie += (i - dePie);
            }
            dePie += val;
        }
        cout << "Case #" << tc << ": " << ans << endl;
    }
    fclose(stdout);
    return 0;
}

/*
(\_/)
(. .)
c(")(")
*/