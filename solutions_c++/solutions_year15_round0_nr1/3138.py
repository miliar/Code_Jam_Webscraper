#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int k;
        string s;
        cin >> k >> s;
        int ans = 0;
        int p = 0;
        for (int i = 0; i <= k; ++i)
            if (p >= i)
                p += s[i] - '0';
            else
            {
                if (p < i)
                {
                    ans += i - p;
                    p = i;
                }
                p += s[i] - '0';
            }
        cout << "Case #" << t << ": " << ans << '\n';
    }


    return 0;
}
