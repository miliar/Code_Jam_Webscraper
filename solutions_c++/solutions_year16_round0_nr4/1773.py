#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int q = 1, k, c, s;
    ifstream cin("D-small-attempt0.in");
    ofstream cout("output");
    cin >> q;
    for (int i = 0; i < q; ++i)
    {
        cin >> k >> c >> s;
        cout << "Case #" << i + 1 << ":";
        if (s < k / c)
            {cout << " IMPOSSIBLE\n";continue;}
        int q = (k + c - 1) / c;
        for (int i = 0; i < q; ++i)
        {
            int64_t ans = 0;
            for (int p = 0; p < c && (i != q || p < k); ++p)
                ans = ans * k + (i + q * p) % k;
            cout << ' ' << ans + 1;
        }
        cout << '\n';
    }
    return 0;
}
