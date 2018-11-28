#include <iostream>
#include <stdio.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0 ; i < t ; ++i)
    {
        cout << "Case #" << i+1 << ": ";
        double c, f, x;
        cin >> c >> f >> x;
        double ans = 1e18;
        double add = 2;
        double tm = 0;
        for(int i = 0 ; i < 10000000 ; ++i)
        {
            ans = min(ans, tm + x/add);
            tm += c / add;
            add += f;

            if(tm > ans + 0.0000001) break;
        }
        
        cout.precision(7);
        cout << fixed << ans << "\n";
    }
    return 0;
}
