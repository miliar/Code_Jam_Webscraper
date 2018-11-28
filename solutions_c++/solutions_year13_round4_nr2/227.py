#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long ll;

#define FNAME "B-large"
ifstream in(FNAME ".in");
ofstream out(FNAME ".out");

#define GET(E) in >> E
#define PRINT(E) out << E; cout << E

#define FOR(i,n) for(int i=0;i<(n);i++)
#define ALL(A) A.begin(), A.end()

ll N;

ll _lp(ll n, ll r, int s, ll res) {
    if(n < r) return res;
    return _lp(n-r, r<<1, s+1, res+(1ll<<(N-s)));
}

ll lp(ll n) {
    return _lp(n, 1, 1, 1);
}

ll hp(ll n) {
    return (1ll<<N)+1-_lp((1ll<<N)-n-1, 1, 1, 1);
}

void do_case(int cn) {
    ll P;
    GET(N >> P);
    ll mi = 0, ma = (1ll<<N)-1;
    while(mi < ma) {
        ll mid = (mi + ma + 1) / 2;
        if(lp(mid) <= P) mi = mid;
        else ma = mid-1;
    }
    ll a = mi;
    mi = 0;
    ma = (1ll<<N)-1;
    while(mi < ma) {
        ll mid = (mi + ma + 1) / 2;
        if(hp(mid) <= P) mi = mid;
        else ma = mid-1;
    }
    ll b = mi;
    PRINT("Case #" << cn << ": " << a << " " << b << endl);
}

int main() {
    int T;
    in >> T;
    for(int it=1;it<=T;it++) do_case(it);
    out.close();
    return 0;
}

