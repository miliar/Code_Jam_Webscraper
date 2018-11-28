#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <math.h>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long
#define ld long double
#define chr unsigned char
#define uint unsigned int

ll lst[11];

ll div(ll n){
    for (ll i = 2; i * i <= n; ++i)
        if (n % i == 0)
            return i;
    return -1;
}


ll base(ll n, int b){
    ll m = 0, p = 1;
    while (n != 0){
        m += (n % 2) * p;
        p *= b;
        n /= 2;
    }
    return m;
}


int main()
{
    freopen("c.out", "w", stdout);

    int n = 16, j = 50;

    ll p = (1LL << (n - 2)), q = (1LL << (n - 1)) + 1;
    ll x, d;
    int cnt = 0;
    bool ans;

    cout << "Case #1:" << endl;
    for (ll mask = 0; mask < p; ++mask){
        x = q + (mask << 1LL);

        ans = true;
        for (int b = 2; b <= 10; ++b){
            d = div(base(x, b));
            lst[b] = d;
            if (d == -1){
                ans = false;
                break;
            }
        }

        if (ans){
            cnt++;
            for (int i = n - 1; i >= 0; --i)
                cout << ((x >> i) & 1LL);
            cout << ' ';
            for (int b = 2; b <= 10; ++b)
                cout << lst[b] << ' ';
            cout << endl;
            if (cnt == j)
                break;
        }
    }

    fclose(stdout);
    return 0;
}
