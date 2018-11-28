#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("B-small-attempt0.in");
    ofstream cout("output_small");
    int t;
    cin >> t;
    cout.precision(30), cout << fixed;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        int n, k;
        cin >> n >> k;
        long double a[n];
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        long double ans = 0;
        for (int i = 0; i < (1 << n); ++i) if (__builtin_popcount(i) == k)
        {
            long double lans = 0;
            for (int j = i; j != -1; --j > 0? j &= i: 0) if (__builtin_popcount(j) == k / 2)
            {
                long double p = 1;
                for (int l = 0; l < n; ++l) if (i & (1 << l))
                    if (j & (1 << l))
                        p *= a[l];
                    else
                        p *= 1 - a[l];
                lans += p;
            }
            ans = max(ans, lans);
        }
        cout << ans << '\n';
    }
    return 0;
}
