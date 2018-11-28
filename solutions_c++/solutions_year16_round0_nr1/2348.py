#include "bits/stdc++.h"

using namespace std;

#define sz(a) int((a).size())
#define all(x) x.begin(), x.end()
#define pb push_back
#define F first
#define S second
typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
const int inf = 1e9 + 7;
const ld eps = 1e-8;


ll checker(ll n) {
    set<int> s;
    ll p = n;
    while (sz(s) != 10) {
        ll k = p;
        while (k) s.insert(k % 10), k /= 10;
        p += n;
    } return p - n;
}

int main() {
#ifdef DEBUG
   // freopen("/Users/rzmn/Documents/acm/acm/input.txt", "r", stdin);
   // freopen("/Users/rzmn/Documents/acm/acm/output.txt", "w", stdout);
#endif
    
    
    
    int Tcase; scanf("%d", &Tcase);
    for (int test = 1; test <= Tcase; ++test) {
        int t; scanf("%d", &t);
        if (!t) printf("Case #%d: INSOMNIA\n", test);
        else printf("Case #%d: %lld\n", test, checker(t));
    }
    
    
    
    
#ifdef DEBUG
    cerr << "\n == TIME : " << clock() / ld(CLOCKS_PER_SEC) << " == " << endl;
#endif
}

// 14 27













