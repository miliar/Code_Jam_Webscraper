#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int d[1001];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> d[i];
        sort(d, d + n);
        int ans = d[n - 1];
        for (int i = 1; i <= d[n - 1]; ++i)
        {
            int c = 0;
            for (int j = 0; j < n; ++j)
                c += (d[j] - 1) / i;
            ans = min(ans, i + c);
        }
        cout << "Case #" << t << ": " << ans << '\n';
    }


    return 0;
}
