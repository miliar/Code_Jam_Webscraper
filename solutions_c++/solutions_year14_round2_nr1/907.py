#include <iostream>
#include <vector>
#include <set>
#include <cstdio>
#include <algorithm>

#define sz(A) (int(A.size()))

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        cout << "Case #" << t + 1 << ": ";
        int n;
        cin >> n;
        vector <vector <pair <char, int> > > A(n);

        for (int x = 0; x < n; x++)
        {
            string s;
            cin >> s;

            for (int i = 0; i < sz(s); i++)
            {
                if (i == 0 || s[i] != s[i - 1])
                    A[x].push_back(make_pair(s[i], 1));
                else
                    A[x].back().second++;
            }
        }
        bool bad = 0;

        for (int i = 1; i < n; i++)
        {
            if (sz(A[i]) != sz(A[0]))
            {
                bad = 1;
                break;
            }

            for (int j = 0; j < sz(A[i]); j++)
                if (A[i][j].first != A[0][j].first)
                {
                    bad = 1;
                    break;
                }
        }

        if (bad)
        {
            cout << "Fegla Won\n";
            continue;
        }
        int res = 0;

        for (int j = 0; j < sz(A[0]); j++)
        {
            int best = int(1e9);

            for (int num = 0; num <= 110; num++)
            {
                int sum = 0;

                for (int i = 0; i < n; i++)
                {
                    sum += abs(A[i][j].second - num);
                }
                best = min(best, sum);
            }
            res += best;
        }
        cout << res << '\n';
    }
    return 0;
}
