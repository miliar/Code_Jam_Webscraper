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
#include <bitset>
#define NL "\n"
typedef long long ll;
#define fillm(a, val) memset(a, val, sizeof(a))
using namespace std;
const double pi = acos(-1.0);
const ll mod = 1000000007;
const ll maxn = 60;
const ll inf = 1ll << 30;
vector<ll> facs[maxn];
vector<ll> nums;
ll isprime(ll n)
{
    ll lim = sqrt(n);
    for (int i = 2; i <= lim; ++i)
    {
        if (n % i == 0)
        {
            return i;
        }
    }
    return 0;
}
ll convert(ll num, ll base, ll len)
{
    ll val = 0;
    ll powr = 1;
    for (int i = 0; i < len; ++i)
    {
        if (num & (1 << i))
        {
            val += powr;
        }
        powr *= base;
    }
    return isprime(val);
}
void solve(ll n, ll j)
{
    ll cnt = 0;
    for (ll i = 0; i < (1 << (n - 2)); i++)
    {
        ll mask = (1 << (n - 1));
        mask |= (i << 1);
        mask |= 1;
        bool flag = 1;
        vector<ll> temp;
        for (ll j = 2; j <= 10; j++)
        {
            ll temp1 = convert(mask, j, n);
            if (temp1)
            {
                temp.push_back(temp1);
            }
            else
            {
                flag = 0;
                break;
            }
        }
        if (flag)
        {
            facs[cnt] = temp;
            nums.push_back(mask);
            cnt++;
            if (cnt == j)
            {
                break;
            }
        }
    }
}
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
    ll n, j;
    cin >> n >> j;
    solve(n, j);
    cout << "Case #1:\n";
    for (int i = 0; i < j; ++i)
    {
        bitset<16> b(nums[i]);
        string str = b.to_string();
        str.erase(0, str.find_first_not_of('0'));
        cout << str << " ";
        for (auto j : facs[i])
        {
            cout << j << " ";
        }
        cout << endl;
    }
    return 0;
}
