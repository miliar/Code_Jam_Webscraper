
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long ll;

bool asleep(bool *v) {
    for (int i = 0; i <= 9; i++) {
        if (!v[i]) {
            return false;
        }
    }
    return true;
}

ll solve(ll n) {
    bool v[10] = { false };
    int i = 0;
    ll x;
    
    while (!asleep(v)) {
        x = n * ++i;
        
        while (x > 0) {
            v[x%10] = true;
            x /= 10;
        }
    }
    
    return n * i;
}

int main(void) {
    int t;
    ll n;
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    cin >> t;
    
    for (int c = 1; c <= t; c++) {

        cin >> n;
        
        if (n > 0) {
            cout << "Case #" << c << ": " << solve(n) << endl;
        } else {
            cout << "Case #" << c << ": INSOMNIA" << endl;
        }
    }

    return 0;
}
