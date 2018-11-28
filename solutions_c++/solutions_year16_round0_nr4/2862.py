#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

typedef unsigned long long int ll;

ll pow(ll a, ll b) {
    if (b == 0) {
        return 1;
    } else {
        ll tmp = pow(a, b/2);
        if (b % 2 == 0) {
            return tmp*tmp;
        } else {
            return tmp*tmp*a;
        }
    }
}

int main() {
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; ++kase) {
		ll k,c,s;
        cin >> k >> c >> s;
		printf("Case #%d:", kase);
        for (ll i = 1; i <= k; ++i) {
            cout << " " << i*pow(k, c-1);
        }
        cout << endl;
    }
    return 0;
}