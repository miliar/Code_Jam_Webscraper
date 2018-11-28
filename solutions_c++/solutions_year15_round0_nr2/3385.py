#include <bits/stdc++.h>
using namespace std;

int solve()
{
    int D;
    cin >> D;
    vector<int> v(D);
    for (int i = 0; i < D; i++)
        cin >> v[i];
    
    int best = 1000000000;

    for (int eat = 1; eat <= 1000; eat++)
    {
        int cur = 0;
        for (int j = 0; j < D; j++)
        {
            if (v[j] % eat == 0)
                cur += (v[j] / eat) - 1;
            else
                cur += (v[j] / eat);
        }
        cur += eat;
        best = min(best, cur);
    }
    return best;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++)
        printf("Case #%d: %d\n", test, solve());
}
