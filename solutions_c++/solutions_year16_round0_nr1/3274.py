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
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
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

bool vis[20];

bool check(ll x) {
    for (; x > 0; x /= 10) {
        vis[x%10] = 1;
    }

    FOR (i, 0, 10)
        if (!vis[i])
            return false;

    return true;
}

void rob(int test) {
    int n;
    scanf("%d" , &n);
    if (n == 0) {
        printf("Case #%d: INSOMNIA\n", test);
        return;
    }

    FOR (i, 0, 10) vis[i] = 0;

    ll nn = n;
    while (!check(nn)) {
        nn += n;
    }

    printf("Case #%d: %I64d\n", test, nn);
}

int main() {
    int test = 1;
    scanf("%d", &test);

    FORE (i, 1, test) rob(i);

    return 0;
}
