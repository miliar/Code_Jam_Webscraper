
#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define EACH(it,a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
using namespace std;

int f[1000111];

long long rev(long long i) {
    stringstream ss; ss << i;
    string s = ss.str();
    reverse(s.begin(), s.end());

    stringstream ss2 (s);
    long long res; ss2 >> res;
    return res;
}

long long get(long long n) {
    if (n <= 1000000) return f[n];
    long long res = n;
    for(long long mod = 10; mod * mod <= n * 100; mod *= 10LL)
        if (mod < n) {
            long long next = n - n % mod + 1;

            while (next > n) next -= mod;
            while (rev(next) == next) next -= mod;

            if (next <= n && rev(next) < next) res = min(res, get(rev(next)) + 1 + n - next);

            if (n == 10 && res == 2) {
                return res;
            }
        }
    return res;
}

int main() {
    ios :: sync_with_stdio(false);
    f[1] = 1;
    FOR(i,2,1000 * 1000) {
        f[i] = f[i-1] + 1;
        if (i % 10 && rev(i) < i) f[i] = min(f[i], f[rev(i)] + 1);
    }
//    cout << "OK" << endl;
//    DEBUG(get(99LL * 1000111 * 1000111));
//    DEBUG(get(100000000000000LL));

    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        long long n; cin >> n;
        cout << "Case #" << test << ": " << get(n) << endl;
        cerr << test << endl;
    }

    return 0;
}

