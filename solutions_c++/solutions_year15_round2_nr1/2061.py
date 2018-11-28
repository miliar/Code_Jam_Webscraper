#include <bits/stdc++.h>

using namespace std;

#define     mp              make_pair
#define     fs              first
#define     sc              second
#define     pob             pop_back
#define     pub             push_back
#define     eps             1E-7
#define     sz(a)           a.size()
#define     count_one       __builtin_popcount;
#define     count_onell     __builtin_popcountll;
#define     fastIO          ios_base::sync_with_stdio(false)
#define     PI              (acos(-1.0))
#define     linf            (1LL<<62)//>4e18
#define     inf             (0x7f7f7f7f)//>2e9

#ifndef ONLINE_JUDGE
ifstream fin("D:/C++/in");
ofstream fout("D:/C++/out");
#endif

typedef long long ll;
const int MAXN = 1e7 + 5;
int T;
ll n, x;
vector<ll> res;

ll revNr(ll a) {
    ll ret = 0;
    while(a) {
        ret = ret * 10 + a % 10;
        a /= 10;
    }
    return ret;
}

inline int minim(int a, int b) { if(a < b) return a; return b; }

void preGen() {
    res.resize(1e7, inf);
    ll rev = 0;
    for(int i = 1; i <= 20; ++i) {
        res[i] = i;
        rev = revNr(i);
        res[rev] = minim(rev, i + 1);
    }

    for(int i = 21, minLast = i; i <= 1e6; ++i, ++minLast) {
        if(res[i] < minLast)
            minLast = res[i];
        res[i] = minim(res[i], minLast);
        rev = revNr(i);
        res[rev] = minim(res[rev], minLast + 1);
    }
}

int solve() {
    fin >> n;
    return res[n];
}

int main() {

	fin >> T;
	preGen();
	for(int t = 1; t <= T; ++t) {
        fout << "Case #" << t << ": " << solve() << "\n";
	}

    return 0;
}
