#include <iostream>
#include <cstdio>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int ans = 0;
        int r, c, w;
        cin >> r >> c >> w;
        ans = (r - 1) * (c / w) + c / w + w + ((c % w == 0) ? -1 : 0);
        cout << "Case #" << tt << ": " << ans << '\n';
    }

    return 0;
}
