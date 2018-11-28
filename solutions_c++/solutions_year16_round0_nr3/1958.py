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

ll gcd(ll a, ll b) { return b ? gcd(b, a%b) : a; }

ll bp(ll n, ll p, ll m) {
    if (!p) return 1;
    ll g = bp(n, p>>1, m);
    g *= g; g %= m;
    if (p & 1) return (g * n) % m;
    return g;
}
bool ferma(ll x){
    if(x == 2)
        return true;
    for(int i=0;i<100;i++){
        ll a = (rand() % (x - 2)) + 2;
        if (gcd(a, x) != 1)
            return false;
        if(bp(a, x-1, x) != 1)
            return false;
    }
    return true;
}

string parse(ll mask) {
    string s = "";
    while (mask) s += ((mask&1)?'1':'0'), mask >>= 1LL;
    reverse(all(s)); return s;
}

ll recalc(ll mask, ll base) {
    ll ans = 0, pw = 1;
    while (mask) {
        if (mask & 1LL) ans += pw;
        pw *= base;
        mask >>= 1;
    }
    return ans;
}

ll fdiv(ll x) {
    for (ll i = 2; i < sqrt(x) + 10; ++i)
        if (!(x % i)) return i;
    return -1;
}

void lob(int N, int J, int test) {
    vector<ll> ans;
    for (ll i = (1LL << (N - 1LL)); i < (1LL << N); ++i) {
        if (!(i & 1LL)) continue;
        bool ok = true;
        for (int j = 2; j <= 10; ++j) {
            ok &= !(ferma(recalc(i, j)));
            ok &= (fdiv(recalc(i, j)) != -1);
        }
        if (ok) ans.pb(i);
        if (sz(ans) == J) break;
    }
    printf("Case #%d:\n", test);
    for (ll num : ans) {
        cout << parse(num) << ' ';
        for (ll i = 2; i <= 10; ++i)
            cout << fdiv(recalc(num, i)) << ' ';
        puts("");
    }
}

bool check(ll x) {
    ll odd = 0, even = 0, cnt = 0;
    while (x) {
        if (x & 1) (cnt & 1) ? ++odd : ++even;
        x >>= 1LL; ++cnt;
    } return (odd == even);
}

void bigdata(int N, int J, int test) {
    vector<ll> ans;
    for (ll i = (1LL << (N - 1LL)); i < (1LL << N); ++i) {
        if (!(__builtin_popcountll(i) & 1LL) && check(i) && (i & 1LL)) ans.pb(i);
        if (sz(ans) == J) break;
    }
    assert(sz(ans) == J);
    for (ll num : ans) {
        cout << parse(num) << ' ';
        for (int i = 2; i<=10; ++i) {
            if (i & 1) {
                assert(N > 18 || recalc(num, i) % ll(2) == 0);
                cout << 2 << ' ';
            }
            else {
                assert(N > 18 || recalc(num, i) % ll(i + 1) == 0);
                cout << i + 1 << ' ';
            }
        }
        puts("");
    }
}

int main() {
#ifdef DEBUG
    //freopen("/Users/rzmn/Documents/acm/acm/input.txt", "r", stdin);
    //freopen("/Users/rzmn/Documents/acm/acm/output.txt", "w", stdout);
#endif
    
    srand(unsigned(time(nullptr)));
    
    
    int Tcase; scanf("%d", &Tcase);
    
    for (int test = 1; test <= Tcase; ++test) {
        int N, J; scanf("%d%d", &N, &J);
        if (N < 14) lob(N, J, test);
        else bigdata(N, J, test);
    }
    
    
    
    
#ifdef DEBUG
    cerr << "\n == TIME : " << clock() / ld(CLOCKS_PER_SEC) << " == " << endl;
#endif
}

// 14 27













