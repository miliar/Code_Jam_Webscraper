#include <iostream>
#include <algorithm>

using namespace std;

int main()
{

    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++)
    {
        cout << "Case #" << tc + 1 << ": ";

        int d;
        cin >> d;
        vector<int> v(d);
        for (int i = 0; i < d; i++)
            cin >> v[i];

        int mx = *max_element(begin(v), end(v));
        int ans = mx;
       
        for (int i = 1; i < mx; i++)
        {
            int cur = i;
            for (int & x : v)
                cur += (x + i - 1) / i - 1;
            ans = min(ans, cur);
        }
        
        cout << ans << endl;
    }

    return 0;
}
