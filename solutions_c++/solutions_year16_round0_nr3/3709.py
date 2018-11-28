using namespace std;

#include <cstdio>
#include <iostream>
#include <list>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <typeinfo>

#define ll long long 

ll make(ll x, ll base) {
    ll d = 1;
    ll res = 0;
    
    while (x > 0) {
        ll c = x % 2;
        res += c * d;
        d *= base;
        x /= 2;
    }
    
    return res;
}


ll isprime(ll x) {
    if (x == 2)
        return -1;
        
    for (ll j = 2; j * j <= x; j++) {
        if (x % j == 0)
            return j;
    }
    
    return -1;
}

vector < int > ans;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T, n, k;
    cin >> T >> n >> k;
    
    cout << "Case #" << T << ":\n";
    
    for (int i = 0; i < (1 << (n - 1)); i++) {
        if (k == 0)
            break;
        if ((i & 1) == 0)
            continue;
        ll x = (1 << (n - 1)) + i;
        ll q = -1;
        ll temp = 0;
        
        ans.clear();
        
        for (int j = 2; j <= 10; j++) {
            temp = make(x, j);
            q = isprime(temp);
            if (q == -1)
                break;
            ans.push_back(q);
        }
        
        if (q > 0) {
            k--;
            cout << temp << ' ';
            for (int j = 2; j <= 10; j++)
                cout << ans[j - 2] << ' ';
            cout << endl;
        }
    }
}
