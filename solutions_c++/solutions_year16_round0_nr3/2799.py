//Krzysztof Pieprzak
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef pair<long long, long long> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;

#define Size(x) (int)x.size()
#define VAR(v,n) auto v = (n)
#define FOR(i,a,b) for(VAR(i,a); i < (b); ++i)
#define FORE(i,a,b) for(VAR(i,a); i <= (b); ++i)
#define FORREV(i,a,b) for(VAR(i,b); i >= (a); --i)
#define FORSTEP(i,a,b,step) for(VAR(i,a); i < (b); i += (step))
#define FOREACH(i,c) for(auto i : (c))
#define FOREACHS(i,c,n) for(VAR(i,&(c)[0]); i-(c)<(n); ++i)
#define ALL(x) x.begin(),x.end()
#define CLEAR(t) memset(t, 0, sizeof(t))
#define F first
#define S second
#define MP make_pair
#define PUB push_back
#define POB pop_back
#define pieprzu ios_base::sync_with_stdio(0);

const int    INF = 1000000001;
const double EPS = 10e-9;

const int SIZE = 16;

int bits[SIZE+5];

void print(int x) {
    int n = 0;
    for (; x > 0; x >>= 1) {
        bits[n++] = (x&1);
    }

    FORREV (i, 0, n-1) {
        printf("%d", bits[i]);
    }
}

ll getVal(int str, int base) {
    ll val = 0;
    ll pow = 1;
    for (; str > 0; str >>= 1) {
        val += pow * (str&1);
        pow *= base;
    }

    return val;
}

ll getDiv(int str, int base) {
    ll x = getVal(str, base);
    for (ll d = 2; d * d <= x; ++d) {
        if (x % d == 0) {
            return d;
        }
    }

    return -1;
}

bool checkAndPrint(int str) {
    vector<ll> v;
    FORE (base, 2, 10) {
        ll d = getDiv(str, base);
        if (d == -1) {
            return false;
        }
        v.PUB(d);
    }

    print(str);
    FOREACH (el, v) {
        printf(" %I64d", el);
    }
    printf("\n");
    return true;
}

void rob(int test) {
    int n, k;
    scanf("%d %d", &n, &k);

    printf("Case #%d:\n", test);
    int xOrg = (1<<(n-1))|1;

    int mx = (1<<(n-2))-1;
    int cnt = 0;
    FORE (i, 0, mx) {
        if (checkAndPrint(xOrg | (i<<1))) {
            ++cnt;
            if (cnt == k) {
                return;
            }
        }
    }
}

int main() {
    int test = 1;
    scanf("%d", &test);

    FORE (i, 1, test) rob(i);

    return 0;
}
