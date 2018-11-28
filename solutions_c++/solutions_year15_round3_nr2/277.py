#include <iostream>
#include <cstdio>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

string keys, str;

int give_me_period()
{
    vector <int> pr;
    pr.resize(str.size(), 0);
    int n = str.size();
    for (int i = 1; i < n; i++)
    {
        int j = pr[i - 1];
        while(j > 0 && str[j] != str[i])
            j = pr[j - 1];
        if(str[j] == str[i]) j++;
        pr[i] = j;
    }
    return n - pr[n - 1];
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("large-output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        bool flag = true;
        int k, l, s;
        cin >> k >> l >> s;
        cin >> keys >> str;
        long double ans = 1, mx = 0;
        for (int i = 0; i < l; i++)
        {
            bool fg = false;
            long double cnt = 0;
            for (int j = 0; j < k; j++)
            {
                if(str[i] == keys[j]) {cnt+=1; fg = true;}
            }
            ans *= cnt / k;
            flag = flag && fg;
        }
        ans *= ((long double)s - l + 1);
        int pr = give_me_period();
        if(pr == 0)
        {
            mx = s / l;
        }
        else
        {
            for (int i = 0; i + l <= s; i += pr)
                mx += 1;
        }
        if(!flag) mx = 0;
        cout.precision(10);
        cout << fixed;
        cout << "Case #" << tt << ": " << mx - ans << '\n';
    }
    return 0;
}
