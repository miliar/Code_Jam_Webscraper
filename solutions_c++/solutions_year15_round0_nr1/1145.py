#include <bits/stdc++.h>

typedef long long int64;
#define sz(A) (int((A).size()))

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++)
    {
        int n;
        string s;
        cin >> n >> s;
        int first = s[0] - '0';

        while (true)
        {
            int now = first;
            bool good = 1;

            for (int i = 1; i <= n; i++)
            {
                if (now >= i)
                    now += s[i] - '0';
                else
                    good = 0;
            }

            if (good)
                break;
            first++;
        }
        cout << "Case #" << tst + 1 << ": " << first - (s[0] - '0') << '\n';
    }

    return 0;
}
