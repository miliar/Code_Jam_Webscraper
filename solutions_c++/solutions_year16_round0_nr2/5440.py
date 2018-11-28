// Copyright 2016 Ricky_Saurav

/*
Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
Ricky_Saurav wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
*/

#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <set>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>
#define NL "\n"
typedef long long ll;
#define fillm(a, val) memset(a, val, sizeof(a))
using namespace std;
const double pi = acos(-1.0);
const ll mod = 1000000007;
const ll maxn = 100005;
const ll inf = 1ll << 30;

int main()
{
#ifdef LOCAL_SYS
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        string s;
        cin >> s;
        ll idx = s.length() - 1;
        while (s[idx] == '+')
        {
            s.pop_back();
            idx--;
        }
        if (s.size() == 0)
        {
            cout << "Case #" << i << ": " << 0 << endl;
            continue;
        }
        ll len = s.length();
        ll cnt = 1;
        for (int i = 1; i < len; ++i)
        {
            if (s[i] != s[i - 1])
            {
                cnt++;
            }
        }
        cout << "Case #" << i << ": " << cnt << endl;
    }
    return 0;
}
