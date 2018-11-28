//  O_o  =>  -_-
//
//  Created by shikhar thakur
//

#include <bits/stdc++.h>

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define gcd(a,b) __gcd(a,b)
#define fillm(v,val) memset(v,val,sizeof(v))
#define NL "\n"
#define _iosync ios_base::sync_with_stdio(false);cin.tie(0);
const ll mod = 1000000007ll;
const double pi = acos(-1.0);

using namespace std;

int main()
{
#ifdef LOCAL_SYS
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    _iosync
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++)
    {
        string str;
        cin >> str;
        int l = str.size();
        while (str[l - 1] == '+')
        {
            str.pop_back();
            l = str.size();
        }
        cout << "Case #" << tc << ": ";
        if (str.empty())
        {
            cout << "0\n";
            continue;
        }
        l = str.size();
        ll ans = 0;
        for (int i = 1; i < l; i++)
        {
            if (str[i] != str[i - 1])
                ans++;
        }
        ans++;
        cout << ans << NL;
    }
    return 0;
}