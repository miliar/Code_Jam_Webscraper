#include <cstdio>
#include <iostream>

using namespace std;

int n, ans, sol, num[1010];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ": ";

        cin >> n;

        ans = 0;
        for (int i = 1; i <= n; ++i)
        {
            cin >> num[i];
            if (num[i] > ans) ans = num[i];
        }

        for (int i = 1, tmp = ans; i <= tmp; ++i)
        {
            sol = i;
            for (int j = 1; j <= n; ++j)
                if (num[j] > i)
                    sol += (num[j] - i - 1) / i + 1;
            if (sol < ans)
                ans = sol;
        }

        cout << ans << endl;
    }
    return 0;
}
