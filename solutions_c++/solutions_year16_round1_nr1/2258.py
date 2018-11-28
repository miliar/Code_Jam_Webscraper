#include<bits/stdc++.h>

#define MOD 1000000007
#define MODSET(d) if ((d) >= MOD) d %= MOD;

using namespace std;

int main()
{
    #ifdef VSP4
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif // VSP4

    int t, T, i, j, n, k, curr;
    string ans, str;

    cin >> T;

    for (t = 1; t <= T; t++)
    {
        cin >> str;

        //a is original, b is temporary

        ans = "";

        for (i = 0; i < str.size(); i++)
        {
            if (ans + str[i] > str[i] + ans)
            {
                ans = ans + str[i];
            }
            else
            {
                ans = str[i] + ans;
            }
        }

        cout << "Case #" << t << ": " << ans << "\n";
    }

    return 0;
}
