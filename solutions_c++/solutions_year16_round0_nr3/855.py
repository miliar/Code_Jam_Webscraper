
#include <bits/stdc++.h>
#define int long long
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i < _a; ++i)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR(A,n)  { cout << #A << " = "; FOR(_,1,n) cout << A[_] << ' '; cout << endl; }
#define PR0(A,n) { cout << #A << " = "; REP(_,n) cout << A[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
#define ll long long
#define __builtin_popcount __builtin_popcountll
#define SZ(x) ((int) (x).size())
using namespace std;

ll mulMod(ll x, ll y, ll p) {
    if (y == 0) return 0;
    if (x < 1000111000111000111LL / y) return x * y % p;
    ll mid = mulMod((x+x)%p, y>>1LL, p);
    if (y & 1) return (mid + x) % p;
    else return mid;
}
ll powMod(ll x, ll k, ll m) {
    if (k == 0) return 1;
    if ((k & 1)) return mulMod(x,powMod(x, k-1, m), m);
    else return powMod(mulMod(x,x,m), k/2, m);
}
bool suspect(ll a, ll s, ll d, ll n) {
    ll x = powMod(a, d, n);
    if (x == 1) return true;
    for (int r = 0; r < s; ++r) {
        if (x == n - 1) return true;
        x = mulMod(x, x, n);
    }
    return false;
}
// {2,7,61,-1}                      is for n < 4759123141 (= 2^32)
// {2,3,5,7,11,13,17,19,23,-1} is for n < 10^15 (at least)
bool isPrime(ll n) {
    if (n <= 1 || (n > 2 && n % 2 == 0)) return false;
    ll test[] = {2,3,5,7,11,13,17,19,23,-1};
    ll d = n - 1, s = 0;
    while (d % 2 == 0) ++s, d /= 2;
    for (int i = 0; test[i] < n && test[i] != -1; ++i)
        if (!suspect(test[i], s, d, n)) return false;
    return true;
}
long long brent(long long n) { 
    if (n == 1) return 1;
    if (!(n & 1)) return 2;
    if (!(n % 3)) return 3;

    const int p[3] = {1, 3, 5};
    long long y, q, x, ys, g, my = 3;
    int i, j, k, m, r, c;

    for (i = 0; i < my; ++i) {
        y = 1; r = 1; q = 1; m = 111; c = p[i];

        do {
            x = y; k = 0;
            for (j = 1; j <= r; ++j) y = (mulMod(y, y, n) + c) % n;
            do {
                ys = y;
                for (j = 1; j <= min(m, r-k); ++j) {
                    y = (mulMod(y, y, n) + c) % n;
                    q = mulMod(q, abs(x - y), n);
                }
                g = __gcd(q, n); k += m;
            } while (k < r && g < 2);
            r <<= 1;
        } while (g < 2);

        if (g == n)
            do {
                ys = (mulMod(ys, ys, n) + c) % n;
                g = __gcd(abs(x - ys), n);
            } while (g < 2);

        if (g != n) return g;
    }
    return n;
}


const int N = 16;
const int NEED = 50;

int convert(int mask, int base) {
    int res = 0;
    FORD(i,N-1,0) {
        res *= base;
        if ((mask >> i) & 1) res++;
    }
    return res;
}

#define TWO(X) (1<<(X))
#define CONTAIN(S,X) (S & TWO(X))

#undef int
int main() {
#define int long long
    ios :: sync_with_stdio(0); cin.tie(0);
    cout << (fixed) << setprecision(9);
    cout << "Case #1:" << endl;

    int cnt = 0;
    REP(mask,1<<16) if (CONTAIN(mask,0) && CONTAIN(mask,N-1)) {
        bool good = true;
        vector<int> proof;
        FOR(base,2,10) {
            int x = convert(mask, base);
            if (isPrime(x)) {
                good = false;
                break;
            }
            else {
                int b = brent(x);
                assert(x % b == 0);
                assert(1 < b && b < x);
                proof.push_back(b);
            }
        }
        if (good) {
            ++cnt;
            FORD(bit,N-1,0) if ((mask>>bit) & 1) cout << 1; else cout << 0;
            for(int x : proof) cout << ' ' << x; cout << endl;
        }
        if (cnt == NEED) break;
    }
}
