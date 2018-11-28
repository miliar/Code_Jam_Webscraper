#include <bits/stdc++.h>

typedef long long int64;
#define sz(A) (int((A).size()))

using namespace std;

int d[1001][1001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int i = 2; i <= 1000; i++)
        for (int j = 1; j < i; j++)
        {
            d[i][j] = i - j;

            for (int k = 1; k < i; k++)
                d[i][j] = min(d[i][j], d[k][j] + d[i - k][j] + 1);
        }



    for (int tst = 0; tst < T; tst++)
    {
        int n;
        cin >> n;
        int best = 0;
        vector <int> A(n);

        for (int i = 0; i < n; i++)
        {
            cin >> A[i];
            best = max(best, A[i]);
        }
        int res = best;

        for (int i = 1; i <= best; i++)
        {
            int now = 0;

            for (int j = 0; j < n; j++)
                now += d[A[j]][i];
            res = min(res, now + i);
        }
        cout << "Case #" << tst + 1 << ": " << res << '\n';
    }
    return 0;
}
