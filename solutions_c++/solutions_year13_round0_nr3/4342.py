#include <iostream>
#include <set>
#include <iterator>
#include <cmath>
#define LIM 10000000

using namespace std;

typedef long long ll;

set<ll> fs;

bool ispal(ll a) {
    int lim = log10(a) + 1;
    ll tmp = 0;
    for (int i = 0; i < lim/2; ++i) {
        tmp *= 10;
        tmp += a%10;
        a /= 10;
    }
    if (lim % 2) return tmp == a/10;
    return tmp == a;
}

ll f(ll a, ll b) {
    set<ll>::iterator l,h;
    l = fs.lower_bound(a);
    h = fs.upper_bound(b);
    return distance(l,h);
}

ll makepalindrome(ll a) {
    ll ret = 0;
    ll tmp = 1;
    ll orig = a;
    while (a) {
        ret += a%10;
        ret *= 10;
        tmp *= 10;
        a /= 10;
    }
    ret /= 10;
    orig /= 10;
    return ret + orig*tmp;
}
ll makepalindrome2(ll a) {
    ll ret = 0;
    ll tmp = 1;
    ll orig = a;
    while (a) {
        ret += a%10;
        ret *= 10;
        tmp *= 10;
        a /= 10;
    }
    ret /= 10;
    return ret + orig*tmp;
}

int main() {
    ll N, a, b;

    for (ll i = 1; i < LIM; ++i) {
        ll s = makepalindrome2(i);
        ll s2 = makepalindrome(i);
        if (ispal(s*s)) fs.insert(s*s);
        if (ispal(s2*s2)) fs.insert(s2*s2);
    }
    cin >> N;
    for (ll n = 0; n  < N; ++n) {
        cin >> a >> b;
        cout << "Case #" << n+1 << ": " << f(a,b) << endl;
    }
    return 0;
}
