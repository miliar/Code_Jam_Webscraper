#include <iostream>
#include <cmath>
#include <bitset>

using namespace std;

#define ll long long

ll pow(ll b, ll e) {
    ll res = 1;
    for (int i = 0; i < e; i++) {
        res *= b;
    }
    return res;
}

ll is_prime(ll n, int b) {
    
    ll newn = n;
    ll e = 1;
    n = 0;
    while (newn > 0) {
        n += e * (newn%2);
        newn /= 2;
        e *= b;
    }
    
    ll sn = sqrt(n) + 1;
    if (sn == n) sn--;
    for (ll i = 3; i <= sn; i++) {
        if (n % i == 0) {
            return i;
        }
    }
    return 0;
}

int main() {
    
    int n, j;
    n = 16; j = 50;
    
    ll n2 = (1 << (n-1)) + 1;
    
    cout << "Case #1:" << endl;
    
    int found = 0;
    while (found < j) {
        bool jamcoin = true;
        for (int i = 2; i <= 10; i++) {
            if (!is_prime(n2,i)) {
                jamcoin = false;
                break;
            }
        }
        
        if (jamcoin) {
            cout << bitset<16>(n2).to_string();
            for (int i = 2; i <= 10; i++) {
                cout << " " << is_prime(n2,i);
            }
            cout << endl;
            found++;
        }
        
        for (int i = 2; i <= 10; i++) {
            n2 += 2;
        }
    }
}