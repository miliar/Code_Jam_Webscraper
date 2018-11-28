#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, j;
    cin >> n >> j;
    for(int mask = 0; (mask < (1 << n - 2)) && j; mask++)
    {
        vector<int> divs;
        __int128 res;
        for(int k = 2; k <= 10; k++)
        {
            res = 1;
            int t = mask;
            __int128 pw = k;
            for(int i = 0; i < n - 2; i++)
            {
                res += pw * (t & 1);
                t >>= 1;
                pw *= k;
            }
            res += pw;
            for(int i = 2; i < 20; i++)
                if(res % i == 0)
                {
                    divs.push_back(i);
                    break;
                }
        }
        if(divs.size() == 9)
        {
            cout << 1 << bitset<30>(mask) << 1 << ' ';
            for(auto it: divs)
                cout << it << ' ';
            cout << "\n";
            j--;
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ":\n";
        solve();
    }
}
