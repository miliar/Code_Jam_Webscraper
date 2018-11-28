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
        int c, d, v;
        vector <int> coins;
        vector <bool> used, is_coin;
        cin >> c >> d >> v;
        coins.resize(d);
        used.resize(v + 1, false);
        is_coin.resize(v + 1, false);
        for (int i = 0; i < d; i++) cin >> coins[i];
        int ans = 0;
        used[0] = true;
        int j = 0;
        while(true)
        {
            bool flag = true;
            for(int i = 0; i <= v; i++)
            {
                flag = flag && used[i];
            }
            if(flag)
            {
                break;
            }
            if (j == coins.size())
            {
                for (int i = 0; i <= v; i++)
                {
                    if(!used[i]) {coins.push_back(i); break;}
                }
                ans++;
            }
            is_coin[j] = true;
            for (int i = v - coins[j]; i >= 0; i--)
            {
                used[i + coins[j]] = used[i + coins[j]] || used[i];
            }
            j += 1;
        }
        cout << "Case #" << tt << ": " << ans << '\n';
    }
    return 0;
}
