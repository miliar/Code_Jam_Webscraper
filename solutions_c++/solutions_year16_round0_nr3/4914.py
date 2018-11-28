#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define mp make_pair
#define pb push_back
#define pii pair <int, int>
#define piii pair<pii, int>
#define vi vector<int>
#define vpii vector<pii>

#define read1(a) int a; scanf("%d", &a)
#define read2(a, b) int a, b; scanf("%d %d", &a, &b)
#define read3(a, b, c) int a, b, c; scanf("%d %d %d", &a, &b, &c)

#define FOR(i, a, b) for (int i=a; i<b; i++)
#define F0R(i, a) for (int i=0; i<a; i++)

#define readgi(n) F0R(i, n) { scanf("%d", &arr[i]); }
#define readgs(n) F0R(i, n) { scanf(" %c", &arr[i]); }

#define f first
#define s second

#define usaco(in, out) freopen(in, "r", stdin); freopen(out, "w", stdout);

#define println1(a) printf("%d\n", a);
#define println2(a, b) printf("%d %d\n", a, b);
#define println3(a, b, c) printf("%d %d %d\n", a, b, c);
#define pv(v) for (int i : v) { printf("%d ", i); } printf("\n");

const int MOD = 1000000007;
const int MAX = 10000005;

vector<ll> ps;
int isPrime(ll x) {
    for (ll i : ps) {
        if (i*i>x) { return -1; }
        if (x%i==0) { return i; }
    }
}

ll poww(int i, int j) {
    ll k = 1;
    F0R(kek, j) { k *= (ll)i; }
    return k;
}

bool isok(int mask) {
    vi pows;
    F0R(i, 16) {
        if (mask & (1<<i)) { pows.pb(i); }
    }
    vi luvv;
    FOR(i, 2, 11) {
        ll luv = 0;
        for (int j : pows) { luv += poww((ll)i, (ll)j); }
        int kek = isPrime(luv);
        if (kek == -1) { return false; }
        else { luvv.pb(kek); }
    }
    for (int i=15; i>=0; i--){ cout << ((mask&(1<<i))>0); } cout << " ";
    pv(luvv);
    return true;
}
int main() {
    int i=9;
    ps.pb(2);
    for (ll i=3; i*i<=1111111111; i++) { if (isPrime(i)) { ps.pb(i); } }
    for (int i=1; i<(1<<16); i++) {
        if ((i%2==1) && (i&(1<<15))) {
            isok(i);
        }
    }
}
