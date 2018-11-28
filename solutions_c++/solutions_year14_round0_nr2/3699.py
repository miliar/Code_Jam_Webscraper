#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>

#define int64 long long
#define sz(A) (int((A).size()))

using namespace std;

int main()
{
#ifdef shaoling
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        double c, f, x;
        cin >> c >> f >> x;
        double farm = 0;
        double now = 2;
        double res = 1e18;

        for (int i = 0; i <= 100010; i++)
        {
            res = min(res, farm + x / now);
            farm += c / now;
            now += f;
        }
        cout.precision(20);
        cout << fixed;
        cout << "Case #" << t + 1 << ": " << res << '\n';
    }
    return 0;
}